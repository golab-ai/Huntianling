---
name: topol_dihedral_rotation
description: 改变四个原子形成的二面角的角度，对键进行旋转操作
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

调用craton包，改变四个原子形成的二面角的角度，对键进行旋转操作



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `inputs` | string | 是 | 分子文件，可以是smiles, csv文件，或mol\sdf\pdb等格式的分子文件，或包含这些文件的路径 |
| `atom1` | int | 是 | 第一个原子 |
| `atom2` | int | 是 | 第二个原子 |
| `atom3` | int | 是 | 第三个原子 |
| `atom4` | int | 是 | 第四个原子 |
| `value` | float | 是 | 改变的数值 |
| `del_value` | boolean | 是 | 是否在现有参数上进行增减 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件夹
```bash
craton stru vary -i {{inputs}} -a {{atom1}}-{{atom2}}-{{atom3}}-{{atom4}} -v {{value}} -o {{output_path}}

```

##如果没有输出文件夹
```bash
craton stru vary -i {{inputs}} -a {{atom1}}-{{atom2}}-{{atom3}}-{{atom4}} -v {{value}}

```