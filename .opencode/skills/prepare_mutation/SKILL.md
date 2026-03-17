---
name: prepare_mutation
description: 将蛋白中某个氨基酸（残基）突变成另一种氨基酸
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

将蛋白中某个氨基酸（残基）突变成另一种氨基酸

### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `protein_file` | string | 是 | 输入的pdb文件 |
| `residue` | string | 是 | 被突变的残基（氨基酸），格式：127-ARG-H |
| `mutation` | string | 是 | 突变后的氨酸名称，如LEU |
| `output_file` | string | 否 | 突变后，输出的pdb文件的名称 |
| `output_dir` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件名，和输出的文件夹
```bash
craton prepare mutation -i {{input_file}} -r {{residue}} -m {{mutation}} -of {{output_file}} -o {{output_path}}

```

##有输出文件名，没有输出的文件夹
```bash
craton prepare mutation -i {{input_file}} -r {{residue}} -m {{mutation}} -of {{output_file}} 

```

##缺失输出文件名和输出的文件夹
```bash
craton prepare mutation -i {{input_file}} -r {{residue}} -m {{mutation}} 

```
