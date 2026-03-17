---
name: mm_hessian
description: 利用力场计算分子的hessian矩阵
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

调用craton包，基于分子力场，计算分子在某个构象下的hessian矩阵，hessian是能量对坐标的二阶导数组成，是一个3N维的矩阵



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `inputs` | string | 是 | 分子文件，可以是smiles, csv文件，或mol\sdf\pdb等格式的分子文件，或包含这些文件的路径 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件夹
```bash
craton mm calculate hessian -i {{inputs}} -o {{output_path}}

```

##如果没有输出文件夹
```bash
craton mm calculate hessian -i {{inputs}}

```