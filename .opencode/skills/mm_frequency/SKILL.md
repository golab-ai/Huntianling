---
name: mm_frequency
description: 利用力场计算分子的振动频率
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

调用craton包，基于分子力场，计算分子的振动频率，振动频率是hessian矩阵的迹，共3N(N是原子的数目)个值，其中6个数值接近零，代表三个平动、三个转动，剩下3N-6个振动频率



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `inputs` | string | 是 | 分子文件，可以是smiles, csv文件，或mol\sdf\pdb等格式的分子文件，或包含这些文件的路径 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件夹
```bash
craton mm calculate freq -i {{inputs}} -o {{output_path}}

```

##如果没有输出文件夹
```bash
craton mm calculate freq -i {{inputs}}

```