import unittest
'''
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b

# assertEqual
#
class MyTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5,4),9)
    def test_subtract(self):
        self.assertEqual(subtract(5,4),1)

if __name__=='__main__':
    unittest.main()
'''


person = {'name':'Mark','age':20}
numbers = [1,3,2,88,7,44]
s = '优品课堂 codeclassroom.com'

class TestAssert(unittest.TestCase):
    def test_assert_method(self):
        self.assertEqual('Mark',person.get('name'))
        self.assertTrue('优品课堂' in s)
        self.assertIn('优品课堂',s)
        self.assertAlmostEqual(3.3,1.1+2.2)
        self.assertIs(True+1,2)
        self.assertIsNone(person.get('Name',None))
        self.assertIsInstance(s,str)
        self.assertGreater(7,numbers[0])

if __name__=='__main__':
    unittest.main()