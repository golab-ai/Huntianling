---
name: pdb-viewer
description: "Use this skill when user wants to view one or multiple PDB / SDF files in the 3D structure viewer. Trigger when user mentions: open pdb, open sdf, 3D structure, view protein, view molecule, or provides local .pdb/.sdf file(s) to view. Supports viewing multiple files simultaneously by chaining path parameters with '&'."
---

# PDB 3D Structure Viewer Skill

## Overview

Open one or multiple local PDB / SDF files in the 3D structure viewer. The viewer URL is read from the `PDB_VIEWER_URL` environment variable (default: `https://canvas.golab.chat`).

##  Workflow

1. check if the given pdb/sdf file(s) exist:
2. copy the file(s) into ./upload directory
3. construct the viewer hyperlink by:
   - For single file: use `path=/app/huntianling/uploads/{{FILE_NAME}}`
   - For multiple files: chain with `&`, e.g., `path=file1.pdb&path=file2.sdf`
4. replace {{VIEWER_URL}} with the actual viewer URL


## Hyperlink Template

### Single File
```
<a href="{{VIEWER_URL}}/#/three-structure?path=/app/huntianling/uploads/{{FILE_NAME}}" target="_blank">View: {{FILE_NAME}}</a>
```

### Multiple Files
```
<a href="{{VIEWER_URL}}/#/three-structure?path=/app/huntianling/uploads/{{FILE_NAME_1}}&path=/app/huntianling/uploads/{{FILE_NAME_2}}" target="_blank">View: {{FILE_NAME_1}} & {{FILE_NAME_2}}</a>
```

## Examples

### Single File
For file: `/app/huntianling/uploads/01KKG0GM1X3MY196VW83EYA79G-Tyk2_protein.pdb`

Result: `<a href="https://canvas.golab.chat/#/three-structure?path=/app/huntianling/uploads/01KKG0GM1X3MY196VW83EYA79G-Tyk2_protein.pdb" target="_blank">View: 01KKG0GM1X3MY196VW83EYA79G-Tyk2_protein.pdb</a>`

### Multiple Files (Protein + Ligand)
For files:
- `/app/huntianling/uploads/tyk2_protein.pdb`
- `/app/huntianling/uploads/ligand_docked.sdf`

Result: `<a href="https://canvas.golab.chat/#/three-structure?path=/app/huntianling/uploads/tyk2_protein.pdb&path=/app/huntianling/uploads/ligand_docked.sdf" target="_blank">View: tyk2_protein.pdb & ligand_docked.sdf</a>`

