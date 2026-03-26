#!/usr/bin/env bash
set -e

# 激活 conda 环境
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate canvas_api

# 设置 pdb 根目录（后端读取 pdb 的根目录）
export PDB_ROOT_DIR=/app/huntianling/uploads

# 启动后端到 4446（后台运行，日志写到 backend/backend.log）
cd "$(dirname "$0")/backend"
nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 > backend.log 2>&1 &

# 启动 nginx（前端 4445）
nginx -t
service nginx start

