---
name: ff_parameter
description: 为分子系统分配和管理力场参数，包括键、角、二面角和非键相互作用参数。支持力场拟合、验证和应用，用于分子力学模拟、能量计算和动力学模拟。可处理通用力场(GAFF)和经验力场(EMPI)，也支持基于量子力学数据拟合力场参数。
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

为分子的每个原子分配合适的原子类型。确认原子类型，后续才能获取相应的力场参数


@click.option("-i","--input_files",default=".",show_default=True,help="molecule files, such as smiles, *.mol, *.sdf, *.pdb et al",)
@click.option("-f", "--atom_type_file",default=None, show_default=True,help="the file of atom type define",)
@click.option("-o", "--output_directory",default=".", show_default=True,help="The directory of output",)
### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `input_file` | string | 是 | 输入的分子文件或smiles |
| `atom_type_file` | string | 否 | 原子类型定义文件 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果不指定原子类型定义文件
```bash
craton prepare ligand -i {{input_file}} -o {{output_path}}

```

##没有输出的文件夹
```bash
craton prepare ligand -i {{input_file}} 

```

##如果指定了原子类型定义文件
```bash
craton prepare ligand -i {{input_file}} -f {{atom_type_file}} -o {{output_path}}

```
