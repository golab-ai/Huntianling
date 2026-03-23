---
name: forward_synthesis_USPTO_480k
description:  输入一个包含多个反应物组的smiles的文件，对所有的反应物组进行正向合成预测，预测可能的产物分子，模型基于USPTO_480k数据集训练
license: MIT
---

# Forward-synthesis

## Overview
This skill is used to perform forward synthesis on some given reactant sets. It uses the RXNGraphormer library to perform the forward synthesis. The environment is set up using Conda, the environment name is rxngraphormer (if this conda environment is not set up, see skills `rxngraphormer_installation`). The input file contain one or more SMILES. Run the script as the following example and it will predict synthesis route for all moluecules. The `vocab_smiles.txt` can be found in model_path/USPTO_480k.

### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `input_file` | string | 是 | 存放分子SMILES的文本文件路径，使用绝对路径 |
| `output_path` | string | 是 | 存放逆合成分析结果的目录路径，使用绝对路径 |

## Quick start

```bash
source "$(conda info --base)/etc/profile.d/conda.sh" && conda activate rxngraphormer && python .opencode/skills/forward_synthesis_USPTO_480k/scripts/forwardsynthesis.py --input_file {{input_file}} --output_path {{output_path}}
```
