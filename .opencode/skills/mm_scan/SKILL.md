---
name: mm_scan
description: 利用力场，对分子的所有可旋转键(torsion)进行势能面扫描，得到torsion的势能面曲线
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

调用craton包，基于分子力场，对分子的所有可旋转键进行势能面扫描，可旋转键一般是非环内的单键，最终得到势能面曲线。势能面曲线对分析分子的构效关系非常重要



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `inputs` | string | 是 | 分子文件，可以是smiles, csv文件，或mol\sdf\pdb等格式的分子文件，或包含这些文件的路径 |
| `output_path` | string | 否 | 文件输出的目录，默认输出在当前文件下 |

## Quick Start

##如果有输出文件夹
```bash
craton mm scan -i {{inputs}} -o {{output_path}}

```

##如果没有输出文件夹
```bash
craton mm scan -i {{inputs}}

```