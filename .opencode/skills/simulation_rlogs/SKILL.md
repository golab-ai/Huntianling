---
name: simulation_rlogs
description: 相对溶解度，分子间相对溶解度
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

相对溶解度：分子间相对溶解度。依流程提供 `--molecules` 或 `--protein` + `--ligands`。



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `molecules` | string | 否 | 分子输入（依流程） |
| `protein` | string | 否 | 蛋白文件（依流程） |
| `ligands` | string | 否 | 配体文件（依流程） |
| `output_path` | string | 否 | 输出目录，默认 output |
| `simulation_time` | string | 否 | 模拟时间（与步长配合），可用 -t 指定 |
| `charge_method` | string | 否 | 电荷方法，可用 -c 指定 |
| `repeat` | number | 否 | 重复计算次数，默认 1 |

## Quick Start

##使用分子输入
```bash
craton simulation rlogs --molecules {{molecules}} -o {{output_path}}

```

##使用蛋白与配体
```bash
craton simulation rlogs --protein {{protein}} --ligands {{ligands}} -o {{output_path}}

```
