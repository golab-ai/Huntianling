---
name: simulation_solution
description: 溶液相模拟，溶质置于溶剂盒子中，进行溶剂化 MD
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

溶液相模拟：溶质置于溶剂盒子中，进行溶剂化 MD。需提供溶质分子（SMILES 或分子文件）。



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `molecules` | string | 是 | 溶质分子，SMILES 或分子文件（如 .sdf）或目录 |
| `output_path` | string | 否 | 输出目录，默认 output |
| `simulation_time` | string | 否 | 模拟时间（与步长配合），可用 -t 指定 |
| `charge_method` | string | 否 | 电荷方法，可用 -c 指定 |
| `repeat` | number | 否 | 重复计算次数，默认 1 |

## Quick Start

##如果有输出目录
```bash
craton simulation solution --molecules {{molecules}} -o {{output_path}}

```

##如果指定模拟时间
```bash
craton simulation solution --molecules {{molecules}} -o {{output_path}} -t {{simulation_time}}

```

##仅必填参数
```bash
craton simulation solution --molecules {{molecules}}

```
