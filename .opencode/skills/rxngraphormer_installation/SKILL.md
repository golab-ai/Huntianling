---
name: rxngraphormer_installation
description:  安装燧人反应预测模型的核心模型RXNGraphormer
license: MIT
---

# RXNGraphormer Installation

## Overview
This skill is used to install the core model RXNGraphormer for reaction prediction if there is no RXNGraphormer enviroment.

### Arguments
No arguments are required for this skill.

## Quick start

```bash
conda create -n rxngraphormer python=3.10
conda activate rxngraphormer
git clone -b pytorch2 https://github.com/licheng-xu-echo/RXNGraphormer.git
cd RXNGraphormer/
pip install -r requirements_pt221.txt -f https://data.pyg.org/whl/torch-2.2.0+cu121.html --extra-index-url https://download.pytorch.org/whl/cu121
pip install .
```
