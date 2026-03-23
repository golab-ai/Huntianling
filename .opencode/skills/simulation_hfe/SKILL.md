---
name: simulation_hfe
description: 绝对水合自由能，单分子的水合自由能
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

绝对水合自由能：单分子的水合自由能。需提供分子（SMILES 或分子文件）。



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `molecules` | string | 是 | 分子输入，SMILES 或分子文件 |
| `output_path` | string | 否 | 输出目录，默认 output |
| `simulation_time` | string | 否 | 模拟时间（与步长配合），可用 -t 指定 |
| `charge_method` | string | 否 | 电荷方法，可用 -c 指定 |
| `repeat` | number | 否 | 重复计算次数，默认 1 |

## Quick Start

##如果有输出目录
```bash
craton simulation ahfe --ligands {{molecules}} -o {{output_path}}

```

##仅必填参数
```bash
craton simulation ahfe --ligands {{molecules}}

```
