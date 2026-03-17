---
name: docking
description: 分子对接操作，需要提供蛋白的pdb文件，化合物的sdf文件。本空能包含口袋发现操作，也可以手动指定口袋位置
license: Proprietary. LICENSE.txt has complete terms
---

### Arguments

|选项 | 必填 |说明 |	默认值 |
|-p / --protein | 是 | 蛋白 PDB 文件 |	. |
|-i / --ligands | 是 | 配体文件（如 SDF）	| .| 
|-center / --center | 否 |结合口袋中心坐标 (x,y,z) | 不指定则自动用 dock pocket 分析得到|
|-box / --box_size | 否 | 对接盒子尺寸 (x,y,z) |不指定则同上，从口袋分析得到 |
|-charge / --charge_method	| 否 | 配体电荷方法 |binc（可选如 am1bcc）|
|-o / --output_dir | 否 | 结果输出目录 |. |

## Quick Start

使用方式：
未指定口袋将，自动用 dock pocket 分析
```bash
craton dock dock -p {{protein_file}} -i {{ligand_file}} -o {{output_dir}}
```

口袋中心和盒子尺寸（需按 要求的 x,y,z 格式，具体可为逗号分隔或列表，)
```bash
craton dock dock -p {{protein_file}} -i {{ligand_file}} -o {{output_dir}}  -center "10.0,20.0,15.0" -box "20,20,20" 
```
