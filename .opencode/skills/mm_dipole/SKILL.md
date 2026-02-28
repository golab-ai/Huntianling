---
name: mm_dipole
description: 利用力场和分子力学方法，计算分子的偶极矩
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

调用craton包，计算分子的偶极矩。偶极矩是原子坐标的电荷加权平均。偶极矩是反映分子极性的重在参数



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `inputs` | string | 是 | 分子文件，可以是smiles, csv文件，或mol\sdf\pdb等格式的分子文件，或包含这些文件的路径 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件夹
```bash
craton mm multipole -p dipole -i {{inputs}} -o {{output_path}}

```

##如果没有输出文件夹
```bash
craton mm multipole -p dipole -i {{inputs}}

```