import argparse
import json
import sys
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

import pandas as pd
import torch
from torch_geometric.data import Data
from torch_geometric.loader import DataLoader

from models.finetune_model import standard_finetune
from suiren_datasets.org_mol2d import from_smiles

# 设置标准输出编码为UTF-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8')


PROJECT_ROOT = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_ROOT / "solubility_of_gas_in_water_regression.pt"
ALLOWED_ELEMENTS = {1, 6, 7, 8, 9, 15, 16, 17, 35, 53}

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Predict the solubility of gas in water of a molecule"
    )
    parser.add_argument(
        "--smiles-column",
        type=str,
        default=None,
        help="CSV column name containing SMILES. If omitted, the script auto-detects it.",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=32,
        help="Inference batch size for CSV input.",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="auto",
        choices=["auto", "cpu", "cuda"],
        help="Inference device.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Optional output file path. If not provided, the result will be printed to the terminal.",
    )

    args = parser.parse_args()
    args.input = None

    return args


def resolve_device(device_arg: str) -> torch.device:
    if device_arg == "cpu":
        return torch.device("cpu")
    if device_arg == "cuda":
        if not torch.cuda.is_available():
            raise RuntimeError("There is no CUDA device available in the current environment.")
        return torch.device("cuda")
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def load_torch_file(path: Path):
    try:
        return torch.load(path, map_location="cpu", weights_only=False)
    except TypeError:
        return torch.load(path, map_location="cpu")


def normalize_state_dict(checkpoint_obj) -> Tuple[Dict[str, torch.Tensor], Dict[str, object]]:
    if isinstance(checkpoint_obj, dict) and "state_dict" in checkpoint_obj:
        state_dict = checkpoint_obj["state_dict"]
        meta = checkpoint_obj
    elif isinstance(checkpoint_obj, dict):
        state_dict = checkpoint_obj
        meta = checkpoint_obj
    else:
        raise TypeError("Unsupported checkpoint format.")

    normalized = {}
    for key, value in state_dict.items():
        new_key = key[7:] if key.startswith("module.") else key
        normalized[new_key] = value
    return normalized, meta


def to_float(value) -> float:
    if isinstance(value, torch.Tensor):
        return float(value.item())
    return float(value)


def download_model_from_modelscope(model_path: Path) -> bool:
    """
    尝试从 ModelScope 下载模型文件。
    
    Args:
        model_path: 模型文件路径
        
    Returns:
        True 如果下载成功，False 如果下载失败
    """
    if model_path.is_file():
        return True
    
    model_dir = model_path.parent
    model_name = model_path.name
    
    print(f"Model file not found: {model_path}")
    print(f"Attempting to download model from ModelScope...")
    
    try:
        cmd = [
            "modelscope", "download",
            "--model", "ajy112/Suiren-Model-Set",
            model_name,
            "--local_dir", str(model_dir)
        ]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300
        )
        
        if result.returncode == 0 and model_path.is_file():
            print(f"Model downloaded successfully to: {model_path}")
            return True
        else:
            print(f"Download command failed with return code: {result.returncode}")
            if result.stderr:
                print(f"Error output: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"Download timed out after 300 seconds.")
        return False
    except FileNotFoundError:
        print("modelscope command not found. Please ensure modelscope is installed.")
        return False
    except Exception as e:
        print(f"Unexpected error during download: {str(e)}")
        return False


def load_model(model_path: Path, device: torch.device):
    if not model_path.is_file():
        # 尝试从 ModelScope 下载
        if not download_model_from_modelscope(model_path):
            error_msg = (
                f"{model_path.parent}目录下不存在模型文件，且下载失败，"
                f"需要从\"https://modelscope.cn/models/ajy112/Suiren-Model-Set\"手动下载"
            )
            print(error_msg)
            raise FileNotFoundError(error_msg)

    checkpoint_obj = load_torch_file(model_path)
    state_dict, meta = normalize_state_dict(checkpoint_obj)

    model = standard_finetune(class_flag=False, class_num=2)
    model.load_state_dict(state_dict, strict=True)
    model = model.to(device)
    model.eval()

    norm_factor = None
    if isinstance(meta, dict) and "norm_factor" in meta:
        norm_values = meta["norm_factor"]
        if isinstance(norm_values, (list, tuple)) and len(norm_values) == 2:
            mean, std = norm_values
            norm_factor = (to_float(mean), to_float(std))

    return model, norm_factor


def detect_smiles_column(df: pd.DataFrame, preferred: Optional[str] = None) -> str:
    if preferred:
        if preferred not in df.columns:
            raise ValueError(f"The specified column does not exist in the CSV: {preferred}")
        return preferred

    exact_candidates = [
        "SMILES",
        "smiles",
        "Smiles",
        "canonical_smiles",
        "Canonical_SMILES",
    ]
    for column in exact_candidates:
        if column in df.columns:
            return column

    fuzzy_candidates = [column for column in df.columns if "smiles" in str(column).lower()]
    if len(fuzzy_candidates) == 1:
        return fuzzy_candidates[0]

    if len(df.columns) == 1:
        return df.columns[0]

    raise ValueError(
        "Unable to automatically identify the SMILES column. Please specify it explicitly using --smiles-column."
    )


def looks_like_csv_path(input_value: str) -> bool:
    return Path(input_value).suffix.lower() == ".csv"


def load_inputs(input_value: str, smiles_column: Optional[str]) -> Tuple[str, pd.DataFrame, str, Optional[Path]]:
    input_path = Path(input_value).expanduser()

    if input_path.is_file():
        df = pd.read_csv(input_path)
        smiles_col = detect_smiles_column(df, smiles_column)
        return "csv", df.copy(), smiles_col, input_path.resolve()

    if looks_like_csv_path(input_value):
        raise FileNotFoundError(f"Input CSV not found: {input_path.resolve()}")

    df = pd.DataFrame({"SMILES": [input_value]})
    return "smiles", df, "SMILES", None


def build_graph(smiles: str) -> Tuple[Optional[Data], Optional[str]]:
    if pd.isna(smiles):
        return None, "empty_smiles"

    smiles = str(smiles).strip()
    if not smiles:
        return None, "empty_smiles"

    graph_tuple, mol_flag = from_smiles(smiles)
    if not mol_flag:
        return None, "invalid_smiles"

    x, edge_index, edge_attr, edge_index_all = graph_tuple
    atom_types = set(x[:, 0].tolist())
    if not atom_types.issubset(ALLOWED_ELEMENTS):
        return None, "unsupported_elements"

    data = Data(
        x=x.to(torch.long),
        edge_index=edge_index.to(torch.long),
        edge_attr=edge_attr.to(torch.long),
        edge_index_all=edge_index_all.to(torch.long),
        smiles=smiles,
    )
    return data, None


def run_inference(
    model: torch.nn.Module,
    norm_factor: Optional[Tuple[float, float]],
    data_list: Sequence[Data],
    device: torch.device,
    batch_size: int,
) -> List[Dict[str, object]]:
    loader = DataLoader(list(data_list), batch_size=batch_size, shuffle=False)
    outputs: List[Dict[str, object]] = []

    with torch.no_grad():
        for batch in loader:
            batch = batch.to(device)
            logits = model(batch)

            preds = logits.view(-1).detach().cpu()
            if norm_factor is not None:
                mean, std = norm_factor
                preds = preds * std + mean
            for pred in preds:
                outputs.append({"prediction": float(pred.item())})

    return outputs


def attach_predictions(
    df: pd.DataFrame,
    records: List[Optional[Dict[str, object]]],
) -> pd.DataFrame:
    result_df = df.copy()
    result_df["status"] = "invalid"
    result_df["error"] = None

    discovered_columns: List[str] = []
    for record in records:
        if record:
            for key in record.keys():
                if key not in {"status", "error"} and key not in discovered_columns:
                    discovered_columns.append(key)

    for column in discovered_columns:
        result_df[column] = None

    for idx, record in enumerate(records):
        if not record:
            continue
        result_df.at[idx, "status"] = record.get("status", "invalid")
        result_df.at[idx, "error"] = record.get("error")
        for key, value in record.items():
            if key in {"status", "error"}:
                continue
            result_df.at[idx, key] = value

    return result_df


def main() -> None:
    args = parse_args()

    if args.input is None:
        try:
            args.input = input().strip()
        except EOFError:
            raise ValueError("No input provided.")
        if not args.input:
            raise ValueError("Input cannot be empty.")

    device = resolve_device(args.device)

    print(f"Loading model: {MODEL_PATH}")
    model, norm_factor = load_model(MODEL_PATH, device)
    print("Model loading complete.")

    input_kind, input_df, smiles_column, input_path = load_inputs(args.input, args.smiles_column)

    data_list: List[Data] = []
    valid_indices: List[int] = []
    records: List[Optional[Dict[str, object]]] = [None] * len(input_df)

    for idx, smiles in enumerate(input_df[smiles_column].tolist()):
        graph, error = build_graph(smiles)
        if graph is None:
            records[idx] = {"status": "invalid", "error": error}
            continue

        data_list.append(graph)
        valid_indices.append(idx)

    if data_list:
        predictions = run_inference(
            model=model,
            norm_factor=norm_factor,
            data_list=data_list,
            device=device,
            batch_size=args.batch_size,
        )
        for row_idx, pred in zip(valid_indices, predictions):
            pred["status"] = "ok"
            pred["error"] = None
            records[row_idx] = pred

    result_df = attach_predictions(input_df, records)

    if input_kind == "smiles":
        row = result_df.iloc[0]
        result = {"SMILES": row.get(smiles_column)}
        prediction = row.get("prediction")
        result["prediction"] = None if pd.isna(prediction) else float(prediction)

        message = json.dumps(result, ensure_ascii=False, indent=2)
        if args.output:
            output_path = Path(args.output).expanduser().resolve()
            output_path.write_text(message, encoding="utf-8")
            print(f"Results saved to: {output_path}")
        else:
            print(message)
        return

    value_column: List[Optional[object]] = []
    for _, row in result_df.iterrows():
        value = row.get("prediction")
        if pd.isna(value):
            value_column.append(None)
        else:
            value_column.append(float(value))

    output_df = input_df.copy()
    output_df["value"] = value_column

    output_path = Path(args.output).expanduser().resolve() if args.output else input_path
    if output_path is None:
        raise ValueError("No source file path found in CSV input to write back to.")

    output_df.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"Task: solubility_of_gas_in_water")
    print(f"Type: regression")
    print(f"Total entries:{len(output_df)}")
    print(f"Result file:{output_path}")


if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, ValueError, RuntimeError, TypeError) as exc:
        print(str(exc))
        raise SystemExit(1)