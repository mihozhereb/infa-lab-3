import unittest
import re


# Вариант: 465887 % 8 = 7 , Л*П**Д case insensitive
def task_3(row: str) -> int:
    return re.findall(r'\b[^ЛПДлпд\s\d]*[Лл][^ЛПДлпд\s\d][Пп][^ЛПДлпд\s\d]{2}[Дд][^ЛПДлпд\s\d]*\b', row)


class TestTask3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(task_3('аЛыПкрДфм оыващшдвыа пав аЛыПкрДфм'), ['аЛыПкрДфм', 'аЛыПкрДфм'])
    def test_2(self):
        self.assertEqual(task_3('ЛаПааД'), ['ЛаПааД'])
    def test_3(self):
        self.assertEqual(task_3('ЛлПллД ЛпПппД ЛдПддД'), [])
    def test_4(self):
        self.assertEqual(task_3('ЛПД ЛффПффД ЛфПфД ЛфПффД'), ['ЛфПффД'])
    def test_5(self):
        self.assertEqual(task_3('ЛфПффДЛфПффДЛфПффД ЛфПффДЛфПффД ЛфПффД'), ['ЛфПффД'])


if __name__ == "__main__":
    unittest.main()