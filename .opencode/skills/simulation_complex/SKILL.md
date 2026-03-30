---
name: simulation_complex
description: 蛋白-配体复合物常规 MD，蛋白与配体一起建盒、跑 MD
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

蛋白-配体复合物常规 MD：蛋白与配体一起建盒、跑 MD。必须提供蛋白文件和配体文件；可选共配体。



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `protein` | string | 是 | 蛋白文件路径，如 .pdb |
| `ligands` | string | 是 | 配体文件，如 .sdf |
| `coligands` | string | 否 | 共配体文件 |
| `output_path` | string | 否 | 输出目录，默认 output |
| `simulation_time` | string | 否 | 模拟时间（与步长配合），可用 -t 指定 |
| `charge_method` | string | 否 | 电荷方法，可用 -c 指定 |
| `repeat` | number | 否 | 重复计算次数，默认 1 |

## Quick Start

##如果有输出目录，无共配体
```bash
craton simulation complex --protein {{protein}} --ligands {{ligands}} -o {{output_path}}

```

##如果有共配体
```bash
craton simulation complex --protein {{protein}} --ligands {{ligands}} --coligands {{coligands}} -o {{output_path}}

```

##仅必填参数
```bash
craton simulation complex --protein {{protein}} --ligands {{ligands}}

```
