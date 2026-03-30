from base_test import BaseTestCase, test_level
import unittest

"""
run test like:
TEST_MIN_LEVEL=1 python -m unittest discover test
"""

class TestGmxProc(BaseTestCase):

    @test_level(0)
    def test_01_recommend_pdb(self):
        prompt = "example/craton/ligand1prepped.sdf'看一下这个分子合适的原子类型，输出到./runjob/craton/atom_type"
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=120)
        self.save_stdout_stderr(out, err, "runjob/craton/atom_type")

        outputfile = "./runjob/craton/atom_type/atom_type.txt"
        self.assertFileExists(outputfile)
        with open(outputfile, "r") as f:
            content = f.read()
        self.assertAllKeywordInText(["18 C c_3an2~5", "39 H h_1", "51 C c_3a~6"], content)

    @test_level(0)
    def test_02_mm_force(self):
        prompt = "example/craton/ligand1prepped.sdf'基于分子力学，利用力场计算分子中每个原子所受的力，输出到./runjob/craton/force"
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=120)
        self.save_stdout_stderr(out, err, "runjob/craton/force")

        outputfile = "runjob/craton/force/energy/compound.mtx"
        self.assertFileExists(outputfile)

    @test_level(0)
    def test_03_mm_energy(self):
        prompt = "example/craton/ligand1prepped.sdf'利用力场，进行结构优化计算，输出到runjob/craton/optimize"
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=120)
        self.save_stdout_stderr(out, err, "runjob/craton/optimize")

        outputfile = "runjob/craton/optimize/optimized_structure/compound.sdf"
        self.assertFileExists(outputfile)


    @test_level(1)
    def test_04_md_simulation(self):
        prompt = "example/pdb/8S99.pdb'利用力场，进行分子动力学模拟，模拟0.05ns，输出到runjob/craton/md"
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=7200)
        self.save_stdout_stderr(out, err, "runjob/craton/md")

        # outputfile = "runjob/craton/md/md.log"
        # self.assertFileExists(outputfile)
        # with open(outputfile, "r") as f:
        #     content = f.read()
        # self.assertAllKeywordInText(["Step", "Time"], content)


    @test_level(0)
    def test_05_atom_type_abs_path(self):
        prompt = "'./example/craton/ligand1prepped.sdf'确认此分子适合的原子类型用于后续力场参数获取。"
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=120)
        self.save_stdout_stderr(out, err, "runjob/craton/atom_type_abs_path")

        outputfile = "./runjob/atom_type.txt"
        self.assertFileExists(outputfile)
        with open(outputfile, "r") as f:
            content = f.read()
        self.assertAllKeywordInText(["18 C c_3an2~5", "39 H h_1", "51 C c_3a~6"], content)

    @test_level(0)
    def test_06_mm_center_abs_path(self):
        prompt = "'./example/craton/ligand1prepped.sdf'基于分子力学，计算分子的几何中心、质点、体积中心，结果保存在/runjob/craton"
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=120)
        self.save_stdout_stderr(out, err, "runjob/craton/center_abs_path")

        outputfile = "./runjob/craton/center.txt"
        self.assertFileExists(outputfile)

    @test_level(0)
    def test_07_mm_dipole_abs_path(self):
        prompt = "'./example/craton/ligand1prepped.sdf'利用力场和分子力学方法，计算分子的偶极矩，输出文件保存在/runjob/craton中"
        code, out, err = self.run_opencode(prompt, model="zhipuai/glm-5", timeout=120)
        self.save_stdout_stderr(out, err, "runjob/craton/dipole_abs_path")

        outputfile = "./runjob/craton/dipole.txt"
        self.assertFileExists(outputfile)

if __name__ == "__main__":
    unittest.main()