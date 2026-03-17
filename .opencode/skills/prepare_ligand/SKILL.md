---
name: prepare_ligand
description: 对化合物分子（ligand），进行预处理，如质子化等操作
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

对化合物分子（ligand），进行预处理，如质子化等操作



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `input_file` | string | 否 | 输入的分子文件或smiles |
| `output_file` | string | 否 | 预处理后，输出的分子文件 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件名，和输出的文件夹
```bash
craton prepare ligand -i {{input_file}} -of {{output_file}} -o {{output_path}}

```

##有输出文件名，没有输出的文件夹
```bash
craton prepare ligand -i {{input_file}} -of {{output_file}}

```

##缺失输出文件名和输出的文件夹
```bash
craton prepare ligand -i {{input_file}}

```
