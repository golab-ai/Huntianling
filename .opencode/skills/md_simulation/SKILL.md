---
name: md_simulation
description: 当用户提供一个蛋白质文件（.pdb）、运行时间（ns)和输出路径时，进行md模拟
license: Proprietary. LICENSE.txt has complete terms
---

## Overview
When the user provides a protein structure file (.pdb), a simulation length (in ns), and an output path, run an MD simulation and write the results to the specified location.

### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `pdb_file` | string | 是 | 目标受体（Protein）文件路径，扩展名为 .pdb |
| `output_dir` | string | 否 | 文件输出的目录，默认输出到.output文件夹下 |
| `md_time` | float | 否 | 模拟步数，默认1ns |

## 执行
### 如果有输入模拟的步数，有文件输出目录
```bash
bash run_job.sh -t {{md_time}} -o {{output_dir}} {{pdb_file}} 
```

### 如果没有输入的模拟步数，有文件输出目录
```bash
bash run_job.sh -o {{output_dir}} {{pdb_file}} 
```

### 如果没有输入的模拟步数，没有文件输出目录，则默认输出到.output文件夹下
```bash
bash run_job.sh {{pdb_file}} 
```

