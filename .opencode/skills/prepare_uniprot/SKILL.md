---
name: prepare_uniprot
description: 输入蛋白的名称，得到uniprot信息，包括sequence, PDB ID, fasta文件等
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

输入蛋白的名称，得到uniprot信息，包括sequence, PDB ID, fasta文件等



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `target` | string | 是 | 蛋白靶点的名称 |
| `uniprot_id` | string | 否 | uniprot ID号 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件夹
```bash
craton prepare uniprot -t {{target}} -o {{output_path}}

```

##如果没有输出文件夹
```bash
craton prepare uniprot -t {{target}}

```

##如果输入的是uniprot id
```bash
craton prepare uniprot -i {{uniprot_id}} -o {{output_path}}

```