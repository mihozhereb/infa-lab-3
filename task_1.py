import unittest
import re


# Вариант: [<{= - emoticon, 465887 % 6 = 5, 465887 % 4 = 3, 465887 % 8 = 7
def task_1(row: str) -> int:
    return len(re.findall(r'\[<{=', row))


class TestTask1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(task_1('sdhjkf[<{=asdasd[<{=  [<{='), 3)
    def test_2(self):
        self.assertEqual(task_1(' [ < { = '), 0)
    def test_3(self):
        self.assertEqual(task_1('[<{=<{=<{=['), 1)
    def test_4(self):
        self.assertEqual(task_1('    [<{=[<{=[<{=[<{=    '), 4)
    def test_5(self):
        self.assertEqual(task_1('[<{ =[<{=[<{ =[ <{='), 1)


if __name__ == "__main__":
    unittest.main()