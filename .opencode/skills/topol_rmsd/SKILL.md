---
name: topol_rmsd
description: 计算两个分子间的RMSD
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

调用craton包，计算两个分子间的RMSD



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `inputs` | string | 是 | reference分子文件，可以是smiles, csv文件，或mol\sdf\pdb等格式的分子文件，或包含这些文件的路径 |
| `inputs2` | string | 是 | target分子文件，可以是smiles, csv文件，或mol\sdf\pdb等格式的分子文件，或包含这些文件的路径 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件夹
```bash
craton stru rmsd -i {{inputs}} -t {{inputs2}} -o {{output_path}}

```

##如果没有输出文件夹
```bash
craton stru rmsd -i {{inputs}} -t {{inputs2}}

```