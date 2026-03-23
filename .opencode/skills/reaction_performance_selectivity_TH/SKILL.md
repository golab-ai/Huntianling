---
name: reaction_performance_selectivity_Thiol_Addition
description:  输入一个包含多个asymmetric thiol addition反应条目的smiles的文件，对所条目进行选择性预测，并输出预测结果
license: MIT
---

# Performance prediction

## Overview
This skill is used to perform reaction reactivity prediction on some given reaction sets. It uses the RXNGraphormer library to perform the regression prediction. The environment is set up using Conda, the environment name is rxngraphormer (if this conda environment is not set up, see skills `rxngraphormer_installation`). The input file contain one or more reaction SMILES. Run the script as the following example and it will predict reaction performance for all reactions.

### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `input_file` | string | 是 | 存放分子SMILES的文本文件路径，使用绝对路径 |
| `output_path` | string | 是 | 存放逆合成分析结果的目录路径，使用绝对路径 |

## Quick start

```bash
source "$(conda info --base)/etc/profile.d/conda.sh" && conda activate rxngraphormer && python .opencode/skills/reaction_performance_selectivity_TH/scripts/performance.py --input_file {{input_file}} --output_path {{output_path}}
```
