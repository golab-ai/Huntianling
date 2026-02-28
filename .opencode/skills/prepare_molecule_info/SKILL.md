---
name: prepare_molecule_info
description: 获取化合物分子（ligand）的信息，包含IUPAC name, smiles, cas-no等。如果输入的是smiles, in_type参数为"smiles"；如果输入的是IUPAC name, in_type参数为“name"; 如果输入的是cas-no号，in_type参数为“cas-no"
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

获取化合物分子（ligand）的信息，包含IUPAC name, smiles, cas-no等

### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `input_file` | string | 是 | 输入的分子文件或smiles |
| `in_type` | string | 否 | 查询字符的类型 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出目录
```bash
craton prepare mol_info -i {{input_file}} -t {{in_type}} -o {{output_path}}

```

##没有输出目录
```bash
craton prepare mol_info -i {{input_file}} -t {{in_type}}

```


