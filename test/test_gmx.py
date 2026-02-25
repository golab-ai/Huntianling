from base_test import BaseTestCase, test_level
import unittest

"""
run test like:
python -m unittest discover test
"""

class TestMyFeature(BaseTestCase):

    @test_level(0)
    def test_00_glm_which_model(self):
        code, out, err = self.run_opencode("which model are you", model="zhipuai/glm-5", timeout=60)
        print(f"code: {code}, out: {out}, err: {err}")
        self.assertAnyKeywordInText(["glm-5", "GLM-5"], out)

    @test_level(0)
    def test_01_recommend_pdb(self):
        prompt = "调研 TYK2 的 UniProt ID 和 PDB 信息，并推荐一个 PDB（输出到 ./runjob/uniprot）"
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=300)
        self.save_stdout_stderr(out, err, "runjob/uniprot")

        self.assertFileExists("./runjob/uniprot/P29597_info.txt")
        with open("./runjob/uniprot/P29597_info.txt", "r") as f:
            content = f.read()
        self.assertAllKeywordInText(["P29597", "TYK2", "8S99"], content)

    @test_level(0)
    def test_03_download_pdb(self):
        prompt = "下载 8S99 的 PDB（存为 .pdb，输出到 ./runjob/pdb）"
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=120)
        self.assertFileExists("./runjob/pdb/8S99.pdb")
        with open("./runjob/pdb/8S99.pdb", "r") as f:
            content = f.read()
        self.assertAllKeywordInText(["HEADER    TRANSFERASE                             27-MAR-23   8S99   ", ], content)

    @test_level(0)
    def test_04_pdb_prepare(self):
        prompt = "准备蛋白（输入 ./runjob/pdb/8S99.pdb，输出到 ./runjob/pdb）"
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=240)
        self.save_stdout_stderr(out, err, "runjob/pocket")

        self.assertFileExists("./runjob/pdb/protein_A_apo.pdb")

    @test_level(1)
    def test_05_run_gmx_md(self):
        code, out, err = self.run_opencode(
            "运行MD模拟（1000 步；输入 ./runjob/pdb/protein_A_apo.pdb；输出到 ./runjob/md）", 
            model="zhipuai/glm-5", 
            timeout=300)
        self.save_stdout_stderr(out, err, "runjob/md")
        keywords = """           Step           Time
           1000        2.00000"""
        with open("./runjob/md/md.log", "r") as f:
            content = f.read()   
        self.assertAllKeywordInText(keywords, content)

    @test_level(0)
    def test_06_pocket_prediction(self):
        prompt = "预测结合口袋（输入 ./runjob/pdb/protein_A_apo.pdb；输出到 ./runjob/pocket/）"
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=300)
        self.save_stdout_stderr(out, err, "runjob/pocket")

        self.assertFileExists("./runjob/pocket/pockets_summary.csv")
        with open("./runjob/pocket/pockets_summary.csv", "r") as f:
            content = f.read()
        self.assertAllKeywordInText(["KAE,6", "A595LEU; A596GLY; A597GLN; A598GLY; A599THR;"], content)
        
    @test_level(0)
    def test_07_molecule_generation(self):
        """环境不对，还得改"""
        prompt = "分子生成（蛋白 + 口袋；输出到 ./runjob/generation）, 输入：./runjob/pdb/protein_A_apo.pdb ./runjob/pocket/pockets_summary.csv"
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=300)
        self.save_stdout_stderr(out, err, "runjob/generation")
        
    @test_level(0)
    def test_08_lig_prep(self):
        prompt = "小分子准备（输入 ./example/generation/SMILES.csv；输出到 ./runjob/lig_prep）"
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=300)
        self.save_stdout_stderr(out, err, "runjob/lig_prep")

        self.assertFileExists("./runjob/lig_prep/ligands.sdf")
        with open("./runjob/lig_prep/ligands.sdf", "r") as f:
            content = f.read()
        self.assertAllKeywordInText(["YITUGUNLCGLOII-GXTWGEPZSA-N", "BBDKLLAGPXCLIH-UHFFFAOYSA-N"], content)

    @test_level(0)
    def test_09_docking(self):
        prompt = """分子对接（蛋白 + 口袋 + 小分子；输出到 ./runjob/docking）
输入：
./runjob/pdb/protein_A_apo.pdb
./runjob/pocket/pockets_summary.csv
./runjob/lig_prep/ligands.sdf
        """
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=600)
        self.save_stdout_stderr(out, err, "runjob/docking")

        self.assertFileExists("./runjob/docking/output/ligands_docking.sdf")
        
    @test_level(0)
    def test_10_fep(self):
        """大概率不对，还得改"""
        prompt = """做 FEP（输入蛋白 + ligands_docking.sdf；输出到 ./fep）
输入：
./pdb/_A_apo.pdb.pdb
./docking/output/ligands_docking.sdf"""
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=120)


    @test_level(0)
    def test_11_admet(self):
        prompt = "预测 ./example/generation/SMILES.csv 的 admet （输出到 ./runjob/admet）"
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=120)
        self.save_stdout_stderr(out, err, "runjob/admet")

        self.assertFileExists("./runjob/admet/admet.csv")


    @test_level(0)
    def test_12_synthesis(self):
        prompt = "预测合成路线（输入 ./example/generation/SMILES.csv；输出到 ./runjob/synthesis）"
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=300)
        self.save_stdout_stderr(out, err, "runjob/synthesis")

        self.assertFileExistsPattern("./runjob/synthesis/retrosynthesis_predictions_*.csv")

    @test_level(0)
    def test_22_compound_database(self):
        """依赖crtaon, 未测试"""
        prompt = "化合物录入到数据库"
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=120)
