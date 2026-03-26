---
name: pdb-viewer
description: "Use this skill when user wants to view a PDB / SDF file in the 3D structure viewer. Trigger when user mentions: open pdb, open sdf, 3D structure, view protein, view molecule, or provides a local .pdb/.sdf file to view."
---

# PDB 3D Structure Viewer Skill

## Overview

Open a local PDB / SDF protein file in the 3D structure viewer at https://canvas.47.103.85.224.nip.io

##  Workflow

1. check if the given pdf/sdf file exist:
2. copy the file into ./upload directory
3. construct the viewer hyperlink by replacing {{FILE_NAME}} in the template with the actual file name.


## Hyperlink Template

```
<a href="https://canvas.47.103.85.224.nip.io/#/three-structure?path=/app/huntianling/uploads/{{FILE_NAME}}" target="_blank">Download Link: {{FILE_NAME}}</a>
```

For file: `/app/huntianling/uploads/01KKG0GM1X3MY196VW83EYA79G-Tyk2_protein.pdb`

Result hyperlink: `<a href="https://canvas.47.103.85.224.nip.io/#/three-structure?path=/app/huntianling/uploads/01KKG0GM1X3MY196VW83EYA79G-Tyk2_protein.pdb" target="_blank">Download Link: {{FILE_NAME}}</a>`

