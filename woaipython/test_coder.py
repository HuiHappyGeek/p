# ！ usr/bin/eny python3
# _*_ coding=utf-8 _*_

import unittest
from main import Coder

class mastering_skillTestCase(unittest.TestCase):
    def test_mastering_skill(self):
        Mark=Coder('Mark')
        Mark.mastering_skill('Python')
        Mark.mastering_skill('Java')
        Mark.mastering_skill('C')
        self.assertEqual(Mark.skills,['Python','Java','C'])
        self.assertEqual(Mark.name,'Mark')
if __name__=='__Coder__':
    unittest.main()






