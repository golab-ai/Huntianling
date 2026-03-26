---
name: helmholtz-energy-of-formation-predict
description: 预测分子的亥姆霍兹生成自由能
license: Proprietary. LICENSE.txt has complete terms
---

## Overview
When given a compound, predict its helmholtz energy of formation.


### Arguments
| 参数名 | 类型 | 必填 | 描述 |
| :--- | :--- | :--- | :--- |
| `smiles` | string | 是 | SMILES字符串或包含SMILES的文件路径（通过标准输入传递） |
| `output` | string | 否 | 输出文件路径，不指定时：单条SMILES输出到终端，CSV文件写回原文件 |
| `smiles-column` | string | 否 | CSV文件中SMILES列的名称，不指定时自动检测 |
| `batch-size` | integer | 否 | 推理批处理大小，默认32 |
| `device` | string | 否 | 推理设备：auto, cpu, cuda，默认auto |

## 执行

### 方法一：通过标准输入传递SMILES或文件路径
```bash
cd skills/helmholtz_energy_of_formation && python helmholtz_energy_of_formation_predict.py
```
运行后输入 SMILES 字符串或文件路径。

### 方法二：通过管道传递SMILES或文件路径
```bash
# 直接预测单个SMILES的亥姆霍兹生成自由能
echo "CCO" | cd skills/helmholtz_energy_of_formation && python helmholtz_energy_of_formation_predict.py

# 批量预测CSV文件中所有SMILES的亥姆霍兹生成自由能
echo "path/to/smiles.csv" | cd skills/helmholtz_energy_of_formation && python helmholtz_energy_of_formation_predict.py
```

### 可选参数
```bash
cd skills/helmholtz_energy_of_formation && python helmholtz_energy_of_formation_predict.py [--smiles-column COLUMN] [--batch-size SIZE] [--device {auto,cpu,cuda}] [--output OUTPUT_FILE]
```

### 示例
```bash
# 直接预测CCO的亥姆霍兹生成自由能
echo "CCO" | python helmholtz_energy_of_formation_predict.py

# 从csv文件批量预测亥姆霍兹生成自由能（相对路径）
echo "../../helmholtz_energy_of_formation.csv" | python helmholtz_energy_of_formation_predict.py

# 从csv文件批量预测亥姆霍兹生成自由能（绝对路径）
echo "D:/PythonProjects/skills_test/helmholtz_energy_of_formation.csv" | python helmholtz_energy_of_formation_predict.py

# 指定输出文件
echo "smiles.csv" | python helmholtz_energy_of_formation_predict.py --output predictions.csv
```

## 输出格式
- 单条 SMILES: 输出 JSON 格式的预测结果
- CSV 文件: 在原文件基础上追加 value 列，包含预测的结果