---
name: simulation_protein
description: 仅蛋白的MD模拟，无配体，仅蛋白建盒与模拟
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

仅蛋白的 MD：无配体，仅蛋白建盒与模拟。必须提供蛋白文件。



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `protein` | string | 是 | 蛋白文件路径，如 .pdb |
| `output_path` | string | 否 | 输出目录，默认 output |
| `simulation_time` | string | 否 | 模拟时间（与步长配合，步长固定2fs），可用 -t 指定 |
| `charge_method` | string | 否 | 电荷方法，可用 -c 指定 |
| `repeat` | number | 否 | 重复计算次数，默认 1 |

## Quick Start

对于单个蛋白的模拟，请使用 craton simulation 的 protein 选项，将 PDB 文件传给 --molecules 参数（勿使用 --protein

##如果有输出目录
```bash
craton simulation protein --molecules {{protein}} -o {{output_path}}
```

##仅必填参数
```bash
craton simulation protein --molecules {{protein}} [ --charge_method {{charge_method}} --repeat {{repeat}} --simulation_time {{simulation_time}} ]
```
