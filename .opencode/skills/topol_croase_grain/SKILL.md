---
name: topol_croas_grain
description: 通过拓扑分析，把分子分解成粗粒化的bead
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

调用craton包，把分子分解成粗粒化的bead，以进行粗粒化力场计算


### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `inputs` | string | 是 | 分子文件，可以是smiles, csv文件，或mol\sdf\pdb等格式的分子文件，或包含这些文件的路径 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件夹
```bash
craton stru topol cg -i {{inputs}} -o {{output_path}}

```

##如果没有输出文件夹
```bash
craton stru topol cg -i {{inputs}}

```