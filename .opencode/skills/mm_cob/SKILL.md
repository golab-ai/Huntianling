---
name: mm_cob
description: 基于分子力学，计算分子的体积中心
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

调用craton包，计算分子的体积中心，体积中心为分子所有原子的x,y,z最大值减最大小值形成的长方体盒子的中心点



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `inputs` | string | 是 | 分子文件，可以是smiles, csv文件，或mol\sdf\pdb等格式的分子文件，或包含这些文件的路径 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件夹
```bash
craton mm center -p cob -i {{inputs}} -o {{output_path}}

```

##如果没有输出文件夹
```bash
craton mm center -p cob -i {{inputs}}

```