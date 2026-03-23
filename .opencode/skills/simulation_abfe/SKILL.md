---
name: simulation_abfe
description: 绝对结合自由能，单配体在蛋白结合位点的结合自由能
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

绝对结合自由能：单配体在蛋白结合位点的结合自由能。必须提供蛋白文件和配体文件。



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `protein` | string | 是 | 蛋白文件路径，如 .pdb |
| `ligands` | string | 是 | 配体文件，如 .sdf |
| `output_path` | string | 否 | 输出目录，默认 output |
| `simulation_time` | string | 否 | 模拟时间（与步长配合），可用 -t 指定 |
| `charge_method` | string | 否 | 电荷方法，可用 -c 指定 |
| `repeat` | number | 否 | 重复计算次数，默认 1 |

## Quick Start

##如果有输出目录
```bash
craton simulation abfe --protein {{protein}} --ligands {{ligands}} -o {{output_path}}

```

##仅必填参数
```bash
craton simulation abfe --protein {{protein}} --ligands {{ligands}}

```
