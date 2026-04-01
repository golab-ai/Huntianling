---
name: pdb-viewer
description: "Use this skill when user wants to view a PDB / SDF file in the 3D structure viewer. Trigger when user mentions: open pdb, open sdf, 3D structure, view protein, view molecule, or provides a local .pdb/.sdf file to view."
---

# PDB 3D Structure Viewer Skill

## Overview

Open a local PDB / SDF protein file in the 3D structure viewer. The viewer URL is read from the `PDB_VIEWER_URL` environment variable (default: `https://canvas.golab.chat`).

##  Workflow

1. check if the given pdf/sdf file exist:
2. copy the file into ./upload directory
3. construct the viewer hyperlink by replacing {{FILE_NAME}} and {{VIEWER_URL}} in the template with the actual file name and viewer URL.


## Hyperlink Template

```
<a href="{{VIEWER_URL}}/#/three-structure?path=/app/huntianling/uploads/{{FILE_NAME}}" target="_blank">Download Link: {{FILE_NAME}}</a>
```

For file: `/app/huntianling/uploads/01KKG0GM1X3MY196VW83EYA79G-Tyk2_protein.pdb`

Result hyperlink: `<a href="https://canvas.golab.chat/#/three-structure?path=/app/huntianling/uploads/01KKG0GM1X3MY196VW83EYA79G-Tyk2_protein.pdb" target="_blank">Download Link: {{FILE_NAME}}</a>`


