---
name: ff_atom_type
description: 为分子的每个原子分配合适的原子类型。确认原子类型，后续才能获取相应的力场参数
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

为分子的每个原子分配合适的原子类型。确认原子类型，后续才能获取相应的力场参数

### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `input_file` | string | 是 | 输入的分子文件或smiles |
| `atom_type_file` | string | 否 | 原子类型定义文件 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

如果不指定原子类型定义文件
```bash
craton  craton ff atom_type -i  -i {{input_file}} -o {{output_path}}

```

##没有输出的文件夹
```bash
craton prepare ligand -i {{input_file}} 

```

##如果指定了原子类型定义文件
```bash
craton prepare ligand -i {{input_file}} -f {{atom_type_file}} -o {{output_path}}

```
