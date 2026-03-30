############ STAGE 1: 使用 devel 镜像编译 GROMACS ###############
FROM nvidia/cuda:12.8.0-devel-ubuntu22.04 AS gromacs-builder

ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-c"]

# 仅安装编译 GROMACS 所需工具
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    git \
    cmake \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# 安装 Intel OneAPI（用于 MPI 编译）
RUN wget -O- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB \
    | gpg --dearmor | tee /usr/share/keyrings/oneapi-archive-keyring.gpg > /dev/null
RUN echo "deb [signed-by=/usr/share/keyrings/oneapi-archive-keyring.gpg] https://apt.repos.intel.com/oneapi all main" | tee /etc/apt/sources.list.d/oneAPI.list
RUN apt-get update && apt-get install -y intel-oneapi-base-toolkit && rm -rf /var/lib/apt/lists/*

# 下载并编译 GROMACS
# RUN wget https://ftp.gromacs.org/gromacs/gromacs-2023.tar.gz
RUN git clone https://github.com/golab-ai/gromacs-fep.git

RUN source /opt/intel/oneapi/setvars.sh --force && \
    cd gromacs-fep && \
    mkdir build && cd build && \
    cmake .. \
        -DGMX_BUILD_OWN_FFTW=ON \
        -DREGRESSIONTEST_DOWNLOAD=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/gromacs \
        -DGMX_MPI=ON \
        -DCMAKE_C_COMPILER=/opt/intel/oneapi/mpi/2021.17/bin/mpigcc \
        -DCMAKE_CXX_COMPILER=/opt/intel/oneapi/mpi/2021.17/bin/mpigxx \
        -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda \
        -DGMX_GPU=CUDA \
    && make -j$(nproc) && make install


############ STAGE 2: 基于 runtime 镜像打包其他功能 ###############
FROM nvidia/cuda:12.8.0-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/root/miniconda3/bin:${PATH}"
SHELL ["/bin/bash", "-c"]

# 从 builder 复制已编译的 GROMACS 和 Intel OneAPI 运行时
COPY --from=gromacs-builder /opt/gromacs /opt/gromacs

RUN apt-get update
RUN apt-get install -y --no-install-recommends wget gpg-agent
RUN wget -O- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB \
    | gpg --dearmor | tee /usr/share/keyrings/oneapi-archive-keyring.gpg > /dev/null
RUN echo "deb [signed-by=/usr/share/keyrings/oneapi-archive-keyring.gpg] https://apt.repos.intel.com/oneapi all main" | tee /etc/apt/sources.list.d/oneAPI.list
RUN apt update
RUN apt install -y intel-oneapi-mkl intel-oneapi-mpi
# COPY --from=gromacs-builder /opt/intel /opt/intel

############ INSTALL BASE TOOLS ###############
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    git \
    vim \
    libgomp1


############ INSTALL MINICONDA ###############
ARG CONDA_INSTALLER=Miniconda3-py310_23.11.0-1-Linux-x86_64.sh
ARG CONDA_URL=https://repo.anaconda.com/miniconda/${CONDA_INSTALLER}
ARG CONDA_SHA256=6581658486be8e700d77e24eccafba586a0fbafafadcf73d35ab13eaee4b80b1
RUN wget --quiet ${CONDA_URL} -O /root/miniconda.sh && \
    echo "${CONDA_SHA256}  /root/miniconda.sh" | sha256sum -c - && \
    /bin/bash /root/miniconda.sh -b -p /root/miniconda3 && \
    rm /root/miniconda.sh && \
    /root/miniconda3/bin/conda init bash && \
    /root/miniconda3/bin/conda config --set auto_update_conda false

############# INSTALL OPENCODE-AI ###############
#RUN curl -fsSL https://opencode.ai/install | bash

############ INSTALL CONDA ENV HUNTIANLING ###############
COPY environment.yaml .
RUN conda env create -f environment.yaml

# Install RXNG
RUN conda create -n rxngraphormer python=3.10 -y
RUN git clone -b pytorch2 https://github.com/licheng-xu-echo/RXNGraphormer.git
RUN conda run -n rxngraphormer pip install torch==2.2.1 --index-url https://download.pytorch.org/whl/cu121 && \
    conda run -n rxngraphormer pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.2.0+cu121.html && \
    conda run -n rxngraphormer pip install modelscope rdkit==2024.3.2 ipykernel pandas python-box OpenNMT-py==1.2.0 torchdata==0.7.1 torch_geometric rxnmapper localmapper transformers==4.30.0 numpy==1.26.4 scikit-learn && \
    cd RXNGraphormer/ && conda run -n rxngraphormer pip install .

RUN conda clean -afy

# 配置环境：GROMACS 与 Intel OneAPI 从 builder 复制，路径已变更
RUN echo "source /opt/gromacs/bin/GMXRC" >> /root/.bashrc && \
    echo "source /opt/intel/oneapi/setvars.sh --force" >> /root/.bashrc && \
    echo "conda activate huntianling" >> /root/.bashrc

############ Craton  ############
# RUN git clone https://github.com/CFL-lab/craton.git
COPY ./craton /opt/craton
RUN cd /opt/craton && conda run -n huntianling pip install -e .

############ Huntianling Skills ############
RUN apt install -y zip libxrender1 libxext6
# RUN curl -fsSL https://bun.sh/install | bash

############ INSTALL NGINX ###############
RUN apt-get update && apt-get install -y --no-install-recommends \
    nginx \
    && rm -rf /var/lib/apt/lists/*

COPY opencode_canvas.conf /etc/nginx/conf.d/opencode_canvas.conf

## canvas service ##
COPY opencode_canvas/backend/requirements.txt .
RUN conda create -n canvas_api python=3.10 -y && \
    conda run -n canvas_api pip install --no-cache-dir \
    -r requirements.txt \
    -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY ./ /app/huntianling

RUN chown -R www-data:www-data /app/huntianling/opencode_canvas/dist && \
    chmod -R 755 /app/huntianling/opencode_canvas/dist

## OPENCODE ##
# COPY ./opencode /app/service
# If you want the original version of opencode code, use the following command. 
# RUN curl -fsSL https://opencode.ai/install | bash

# RUN rm -rf /var/lib/apt/lists/*

##### Addition ##### (should add to environment.yaml later)
RUN conda run -n huntianling pip install modelscope 

RUN chmod +x /app/huntianling/start_all.sh
CMD ["/bin/bash", "/app/huntianling/start_all.sh"]

