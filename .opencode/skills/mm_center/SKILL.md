---
name: mm_center
description: 基于分子力学，计算分子的几何中心、质点、体积中心等
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

调用craton包，计算分子的几何中心、质心、体积中心以及分子的大小



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `inputs` | string | 是 | 分子文件，可以是smiles, csv文件，或mol\sdf\pdb等格式的分子文件，或包含这些文件的路径 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件夹
```bash
craton mm center -i {{inputs}} -p center -o {{output_path}}

```

##如果没有输出文件夹
```bash
craton mm center -i {{inputs}} -p center

```