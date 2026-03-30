---
name: simulation_rhfe
description: 相对水合自由能，多个分子之间的相对水合自由能差
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

相对水合自由能：多个分子之间的相对水合自由能差。需提供多个分子（文件或目录）。



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `molecules` | string | 是 | 分子文件或目录（多个分子） |
| `output_path` | string | 否 | 输出目录，默认 output |
| `simulation_time` | string | 否 | 模拟时间（与步长配合），可用 -t 指定 |
| `charge_method` | string | 否 | 电荷方法，可用 -c 指定 |
| `repeat` | number | 否 | 重复计算次数，默认 1 |

## Quick Start

##如果有输出目录
```bash
craton simulation rhfe --ligands {{molecules}} -o {{output_path}}

```

##仅必填参数
```bash
craton simulation rhfe --ligands {{molecules}}

```
