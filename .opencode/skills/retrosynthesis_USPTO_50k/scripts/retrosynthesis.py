import argparse,os,datetime
import pandas as pd
from rxngraphormer.eval import reaction_prediction
from modelscope import snapshot_download

def main():
    cur_dir = os.getcwd()
    #results_dir = "/".join(cur_dir.split("/")[:-1]) + "/results"
    model_tag = "model_path/USPTO_50k"
    model_path = f'./{model_tag}'
    model_dir = snapshot_download('XuLiCheng2025/Suiren-RXN',allow_patterns=f"{model_tag}/*",local_dir="./")

    parser = argparse.ArgumentParser(description="Retrosynthesis Planning using RXNGraphormer")
    parser.add_argument("--input_file", type=str, help="Path to input file containing SMILES strings")
    parser.add_argument("--output_path", type=str, default="./retrosynthesis", help="output directory")

    args = parser.parse_args()
    input_file = args.input_file
    output_path = args.output_path
    os.makedirs(output_path, exist_ok=True)
    #results_dir = args.results_dir
    with open(input_file, "r") as f:
        input_smiles = f.readlines()
    pdt_smiles_lst = [line.strip() for line in input_smiles]
    #pdt_smiles_lst = input_smiles.split(".")

    # Perform retrosynthesis prediction
    rct_preds = reaction_prediction(model_path, pdt_smiles_lst, task_type="retro-synthesis",device="cpu")
    rct_preds.columns = pdt_smiles_lst
    # Save predictions to CSV
    now = datetime.datetime.now()
    filename = "retrosynthesis_predictions_" + now.strftime("%Y%m%d_%H%M%S") + ".csv"
    rct_preds.to_csv(f"{output_path}/{filename}", index=False)
    print(f"results saved to {output_path}/{filename}")

if __name__ == "__main__":
    main()