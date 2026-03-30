---
name: simulation_vacuum
description: 气相中的分子模拟(单分子的MD模拟)，构建单分子或少量分子体系，无溶剂
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

气相中的分子模拟：构建单分子或少量分子体系，无溶剂。需提供分子（SMILES 或分子文件）。



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `molecules` | string | 是 | 分子输入，SMILES 或分子文件（如 .sdf） |
| `output_path` | string | 否 | 输出目录，默认 output |
| `simulation_time` | string | 否 | 模拟时间（与步长配合），可用 -t 指定 |
| `charge_method` | string | 否 | 电荷方法，可用 -c 指定 |
| `repeat` | number | 否 | 重复计算次数，默认 1 |

## Quick Start

##如果有输出目录
```bash
craton simulation vacuum --molecules {{molecules}} -o {{output_path}}

```

##如果指定模拟时间和电荷方法
```bash
craton simulation vacuum --molecules {{molecules}} -o {{output_path}} -t {{simulation_time}} -c {{charge_method}}

```

##仅必填参数
```bash
craton simulation vacuum --molecules {{molecules}}

```
