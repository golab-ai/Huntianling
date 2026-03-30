---
name: simulation_yaml
description: 完全由 YAML 定义任务，适合复现或批量任务
license: Proprietary. LICENSE.txt has complete terms
---



## Overview

完全由 YAML 定义任务：在 YAML 中指定 simulation_type、蛋白、配体、共配体、输出目录等，适合复现或批量任务。需提供 YAML 任务文件。



### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `yaml_file` | string | 是 | YAML 任务文件路径，如 task.yaml |
| `output_path` | string | 否 | 输出目录（若 YAML 中已指定 output_directory 可省略） |

## Quick Start

##指定 YAML 文件
```bash
craton simulation yaml -f {{yaml_file}}

```

##YAML 示例（单任务）
```yaml
simulation_type: complex
protein: protein.pdb
ligands: ligands.sdf
coligands: cofactor.sdf
output_directory: ./output_complex
```

##YAML 示例（多任务 task0、task1...）
```yaml
task0:
  simulation_type: complex
  protein: protein.pdb
  ligands: ligands.sdf
  output_directory: ./output_0
task1:
  simulation_type: rbfe
  protein: protein.pdb
  ligands: series.sdf
  output_directory: ./output_rbfe
```
