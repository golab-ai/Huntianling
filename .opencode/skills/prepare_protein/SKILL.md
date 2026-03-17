---
name: prepare_protein
description: 对蛋白pdb文件，进行预处理，对N、C端进行封端，对特定残基进行离子化，弥补缺失的原子等。得到准备好的pdb文件
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

对蛋白pdb文件，进行预处理，对N、C端进行封端，对特定残基进行离子化，弥补缺失的原子等。得到准备好的pdb文件



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `input_file` | string | 否 | 输入的pdb文件 |
| `output_file` | string | 否 | 预处理后，输出的pdb文件 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件名，和输出的文件夹
```bash
craton prepare protein -i {{input_file}} -of {{output_file}} -o {{output_path}}

```

##有输出文件名，没有输出的文件夹
```bash
craton prepare protein -i {{input_file}} -of {{output_file}}

```

##缺失输出文件名和输出的文件夹
```bash
craton prepare protein -i {{input_file}}

```
