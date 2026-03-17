---
name: topol_fragmentation
description: 通过拓扑分析，把整个分子分解成碎片，碎片可以成为一个独立的单元
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

调用craton包，把整个分子分解成碎片，碎片包括相对完整的化学环境。整个分子的性质可以近似的由所有碎片的性质加合而成



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `inputs` | string | 是 | 分子文件，可以是smiles, csv文件，或mol\sdf\pdb等格式的分子文件，或包含这些文件的路径 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件夹
```bash
craton stru topol frag -i {{inputs}} -o {{output_path}}

```

##如果没有输出文件夹
```bash
craton stru topol frag -i {{inputs}}

```