---
name: prepare_modify
description: 对蛋白中某个氨基酸（残基）进行修饰，如磷酸化、甲基化等
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

对蛋白中某个氨基酸（残基）进行修饰，如磷酸化、甲基化等


### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `protein_file` | string | 是 | 输入的pdb文件 |
| `residue` | string | 是 | 被突变的残基（氨基酸），格式：127-ARG-H |
| `modify` | string | 是 | 修改的类型，如pho |
| `output_file` | string | 否 | 突变后，输出的pdb文件的名称 |
| `output_dir` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件名，和输出的文件夹
```bash
craton prepare modify -i {{input_file}} -r {{residue}} -m {{modify}} -of {{output_file}} -o {{output_path}}

```

##有输出文件名，没有输出的文件夹
```bash
craton prepare modify -i {{input_file}} -r {{residue}} -m {{modify}} -of {{output_file}} 

```

##缺失输出文件名和输出的文件夹
```bash
craton prepare modify -i {{input_file}} -r {{residue}} -m {{modify}} 

```
