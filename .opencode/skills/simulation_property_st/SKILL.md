---
name: simulation_property_st
description: 模拟计算液相的表面张力(surface tension)，多分子堆积成液相盒子，在NPT系综下进行分子动力学（molecule dynamics, MD)计算。分子输入的格式可以是.sdf, .mol, .csv以及smiles等多种格式
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

纯液体模拟：多分子堆积成液相盒子。需提供液体分子文件。



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `molecules` | string | 是 | 液体分子文件，如 .sdf，.mol，.csv，smiles等 |
| `output_path` | string | 否 | 输出目录，默认 output |
| `simulation_time` | string | 否 | 模拟时间（与步长配合），可用 -t 指定 |
| `charge_method` | string | 否 | 电荷方法，可用 -c 指定 |
| `repeat` | number | 否 | 重复计算次数，默认 1 |

## Quick Start

##如果有输出目录
```bash
craton simulation liquid --molecules {{molecules}} -p st -o {{output_path}} -eng lmp

```

##仅必填参数
```bash
craton simulation liquid --molecules {{molecules}} -p st -eng lmp

```
