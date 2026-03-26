from pathlib import Path
from typing import Iterator

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from rdkit import Chem
from rdkit.Chem import AllChem

import os
import urllib.parse


"""
精简版 FastAPI 服务
目前提供两个接口：
1. GET /api/pdb-file?path=<绝对路径>   —— 读取本地/服务器上的 PDB 文件并以流形式返回
2. POST /smilesToMol                  —— 将 SMILES 转换为 MOL 文本（简化版，无需登录、无需数据库）
"""

app = FastAPI(
    title="Drug Design API",
    description="PDB 文件流 + SMILES 转 MOL 简化服务",
    version="1.0.0",
)


# ===== 路径白名单根目录（建议通过环境变量配置） =====
# 本地开发示例：
#   PDB_ROOT_DIR=C:\Users\23969_kyvkemb\Desktop
# Linux 服务器示例：
#   PDB_ROOT_DIR=/home/liujinkai/pdb-files
ROOT_DIR = Path(os.getenv("PDB_ROOT_DIR", "/home/liujinkai/pdb-files")).resolve()


def safe_resolve_path(raw_path: str) -> Path:
    """
    对传入路径做 URL 解码 + 安全校验，只允许在 ROOT_DIR 下的文件
    """
    if not raw_path:
        raise HTTPException(status_code=400, detail="path 参数不能为空")

    # 先做 URL 解码（前端会 encodeURIComponent）
    decoded = urllib.parse.unquote(raw_path)
    p = Path(decoded).expanduser().resolve()

    # 确保 p 在 ROOT_DIR 目录之内，防止越权访问其它文件
    try:
        p.relative_to(ROOT_DIR)
    except ValueError:
        raise HTTPException(status_code=400, detail="非法路径：不在允许的根目录下")

    return p


@app.get("/pdb-file")
@app.get("/api/pdb-file")
def get_pdb_file(path: str = Query(..., description="服务器上的 pdb 文件绝对路径（URL 编码后）")):
    """
    示例：
    GET /api/pdb-file?path=C%3A%5CUsers%5C23969_kyvkemb%5CDesktop%5Ctyk2.pdb
    """
    file_path = safe_resolve_path(path)

    if not file_path.exists() or not file_path.is_file():
        raise HTTPException(status_code=404, detail="文件不存在")

    def file_iterator() -> Iterator[bytes]:
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                yield chunk

    filename = os.path.basename(str(file_path))
    headers = {
        "Content-Disposition": f'inline; filename="{filename}"',
    }

    # molstar 对 pdb 一般可以使用 text/plain 或 chemical/x-pdb
    return StreamingResponse(
        file_iterator(),
        media_type="chemical/x-pdb",
        headers=headers,
    )


class SmilesToMolRequest(BaseModel):
    """SMILES 转 MOL 请求体（简化版，无需鉴权、无需数据库）"""

    smiles: str = Field(..., description="SMILES 字符串", example="CCO")
    conf_id: int = Field(0, description="构象 ID，默认为 0", ge=0)


@app.post("/smilesToMol")
def smiles_to_mol(request: SmilesToMolRequest):
    """
    将 SMILES 字符串转换为 MOL 文本，方便前端在 3D 页面展示。
    """
    try:
        if not request.smiles or not request.smiles.strip():
            raise HTTPException(status_code=400, detail="SMILES 字符串不能为空")

        mol = Chem.MolFromSmiles(request.smiles)
        if mol is None:
            raise HTTPException(
                status_code=400,
                detail=f"无法从 SMILES '{request.smiles}' 创建分子，请检查格式是否正确",
            )

        # 添加氢原子
        mol = AllChem.AddHs(mol)

        # 尝试生成 3D 坐标
        try:
            conf_id_result = AllChem.EmbedMolecule(mol, randomSeed=42)
            if conf_id_result < 0:
                # 如果 EmbedMolecule 失败，尝试使用随机坐标或 2D
                AllChem.EmbedMolecule(mol, useRandomCoords=True)
        except Exception:
            try:
                AllChem.Compute2DCoords(mol)
            except Exception:
                pass

        mol_block = Chem.MolToMolBlock(mol, confId=request.conf_id)
        if not mol_block:
            raise HTTPException(status_code=500, detail="MOL 文件生成失败")

        # 返回与前端现有调用兼容的结构
        return {
            "code": 200,
            "message": "SMILES 转 MOL 成功",
            "result": {
                "mol_content": mol_block,
                "smiles": request.smiles,
            },
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"SMILES 转 MOL 失败: {str(e)}")


@app.get("/", include_in_schema=False)
def root():
    return {
        "message": "PDB + SMILES 转 MOL 服务运行中",
        "pdb_root_dir": str(ROOT_DIR),
        "pdb示例": "/api/pdb-file?path=<urlencoded-absolute-path>",
        "smiles示例": "/smilesToMol",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
    )
