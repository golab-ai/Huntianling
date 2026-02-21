import unittest
import sys
import os
import subprocess
import threading
import glob

class BaseTestCase(unittest.TestCase):
    """所有测试用例可继承的基类，提供通用断言与 setUp/tearDown。"""

    @classmethod
    def setUpClass(cls):
        """整个测试类执行前调用一次。"""
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        """整个测试类执行后调用一次。"""
        super().tearDownClass()

    def setUp(self):
        """每个测试方法执行前调用。"""
        super().setUp()

    def tearDown(self):
        """每个测试方法执行后调用。"""
        super().tearDown()

    def run_opencode(
        self,
        prompt: str,
        model="zhipuai/glm-5", 
        timeout: float = 60,
        encoding: str = "utf-8"
    ):
        """
        执行命令，stdout/stderr 分别捕获并同时实时打印到当前终端。
        返回 (returncode, full_stdout, full_stderr)。
        """
        # cmd = " ".join()
        proc = subprocess.Popen(
            ["opencode", "-m", model, "run", prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=1,
            text=True,
            encoding=encoding,
        )
        stdout_lines = []
        stderr_lines = []

        def read_stdout():
            for line in proc.stdout:
                sys.stdout.write(line)
                sys.stdout.flush()
                stdout_lines.append(line)
            proc.stdout.close()

        def read_stderr():
            for line in proc.stderr:
                sys.stderr.write(line)
                sys.stderr.flush()
                stderr_lines.append(line)
            proc.stderr.close()

        t_out = threading.Thread(target=read_stdout)
        t_err = threading.Thread(target=read_stderr)
        t_out.daemon = True
        t_err.daemon = True
        t_out.start()
        t_err.start()
        try:
            proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
            raise
        t_out.join(timeout=1.0)
        t_err.join(timeout=1.0)
        full_stdout = "".join(stdout_lines)
        full_stderr = "".join(stderr_lines)
        return proc.returncode, full_stdout, full_stderr

    def save_stdout_stderr(self, stdout, stderr, path):
        with open(path + "/stdout", "w") as f:
            f.write(stdout)
        with open(path + "/stderr", "w") as f:
            f.write(stderr)

    # ---------- 常用断言扩展（按需使用） ----------

    def assertSequenceAlmostEqual(self, actual, expected, places=7, msg=None):
        """断言两个数值序列逐元素近似相等。"""
        self.assertEqual(len(actual), len(expected), msg=msg)
        for i, (a, e) in enumerate(zip(actual, expected)):
            self.assertAlmostEqual(a, e, places=places, msg=msg or f"index {i}")

    def assertFileExists(self, path, msg=None):
        """断言路径存在且为文件。"""
        self.assertTrue(os.path.isfile(path), msg or f"Not a file: {path}")

    def assertFileExistsPattern(self, path_pattern, msg=None):
        """断言路径模糊匹配的文件存在。"""
        paths = glob.glob(path_pattern)
        self.assertTrue(len(paths) > 0, msg or f"No files found matching pattern: {path_pattern}")

    def assertDirExists(self, path, msg=None):
        """断言路径存在且为目录。"""
        self.assertTrue(os.path.isdir(path), msg or f"Not a directory: {path}")
        
    def assertAnyKeywordInText(self, keywords, text, msg=None):
        """
        断言：keywords 中至少有一个子串出现在 text 中则通过。
        :param keywords: 字符串列表，如 ["model", "glm", "GLM"]
        :param text: 被检查的长字符串
        :param msg: 可选，失败时额外说明
        """
        if not keywords:
            self.fail(self._formatMessage(msg, "keywords 列表不能为空"))
        for kw in keywords:
            if kw in text:
                return  # 有一个出现即通过
        standard_msg = "text 中未出现任一 keyword。keywords=%s" % (keywords,)
        self.fail(self._formatMessage(msg, standard_msg))

    def assertAllKeywordInText(self, keywords, text, msg=None):
        """
        断言：keywords 中所有子串都出现在 text 中则通过。
        :param keywords: 字符串列表，如 ["model", "glm", "GLM"]
        :param text: 被检查的长字符串
        :param msg: 可选，失败时额外说明
        """
        if not keywords:
            self.fail(self._formatMessage(msg, "keywords 列表不能为空"))
        for kw in keywords:
            if kw not in text:
                standard_msg = "text 中未出现所有 keyword。keywords=%s" % (keywords,)
                self.fail(self._formatMessage(msg, standard_msg))

        