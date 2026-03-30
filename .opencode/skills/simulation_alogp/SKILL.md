---
name: simulation_alogp
description: 绝对油水分配系数 (logP)，单分子在溶剂相间的分配
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

绝对分配系数 (logP)：单分子在溶剂相间的分配。需提供分子（或依配置提供配体）。



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `molecules` | string | 否 | 分子输入，SMILES 或分子文件（或依配置） |
| `output_path` | string | 否 | 输出目录，默认 output |
| `simulation_time` | string | 否 | 模拟时间（与步长配合），可用 -t 指定 |
| `charge_method` | string | 否 | 电荷方法，可用 -c 指定 |
| `repeat` | number | 否 | 重复计算次数，默认 1 |

## Quick Start

##如果有分子和输出目录
```bash
craton simulation alogp --molecules {{molecules}} -o {{output_path}}

```

##仅指定输出目录
```bash
craton simulation alogp -o {{output_path}}

```
