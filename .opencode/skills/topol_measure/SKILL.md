---
name: topol_measure
description: 测量任一原子间的结构参数，如长度、角度、二面角
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

调用craton包，测量任一原子间的结构参数，如长度、角度、二面角



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `inputs` | string | 是 | 分子文件，可以是smiles, csv文件，或mol\sdf\pdb等格式的分子文件，或包含这些文件的路径 |
| `atoms` | string | 是 | 原子序号的组合，如1-2，3-7-10，10-12-13-14 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件夹
```bash
craton stru measure -i {{inputs}} -a {{atoms}} -o {{output_path}}

```

##如果没有输出文件夹
```bash
craton stru measure -i {{inputs}} -a {{atoms}}

```