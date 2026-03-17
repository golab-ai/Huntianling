---
name: topol_chiral
description: 通过拓扑分析，确认分子内包括的手性原子
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

调用craton包，分析分子包括的手性原子。手性是分子非常重要的特性，不同手性的同一种化合物，生物性质往往差别非常大



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `inputs` | string | 是 | 分子文件，可以是smiles, csv文件，或mol\sdf\pdb等格式的分子文件，或包含这些文件的路径 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件夹
```bash
craton stru topol chiral -i {{inputs}} -o {{output_path}}

```

##如果没有输出文件夹
```bash
craton stru topol chiral -i {{inputs}}

```