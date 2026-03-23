---
name: simulation_autoqm
description: 自动 QM 计算流程，可指定分子数量
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

自动 QM 计算流程。可通过 -n 指定参与计算的分子数量。



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `molecule_number` | number | 否 | 参与计算的分子数量，用 -n 指定 |
| `output_path` | string | 否 | 输出目录，默认 output |

## Quick Start

##指定分子数量和输出目录
```bash
craton simulation autoqm -n {{molecule_number}} -o {{output_path}}

```

##仅指定分子数量
```bash
craton simulation autoqm -n {{molecule_number}}

```

##仅指定输出目录
```bash
craton simulation autoqm -o {{output_path}}

```
