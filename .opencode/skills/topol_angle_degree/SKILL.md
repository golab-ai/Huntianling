---
name: topol_angle_degree
description: 计算分子内三个原子的角度
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

调用craton包，计算分子内三个原子的角度



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `inputs` | string | 是 | 分子文件，可以是smiles, csv文件，或mol\sdf\pdb等格式的分子文件，或包含这些文件的路径 |
| `atom1` | int | 是 | 第一个原子 |
| `atom2` | int | 是 | 第二个原子 |
| `atom3` | int | 是 | 第三个原子 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件夹
```bash
craton stru measure -i {{inputs}} -a {{atom1}}-{{atom2}}-{{atom3}} -o {{output_path}}


```

##如果没有输出文件夹
```bash
craton stru measure -i {{inputs}} -a {{atom1}}-{{atom2}}-{{atom3}}

```