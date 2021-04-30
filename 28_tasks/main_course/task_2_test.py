import unittest
import random
from task_2 import SumOfThe

class func_test(unittest.TestCase):  
    
    def test_summ(self):
        self.assertTrue(func("abcdef","cde"))
        self.assertTrue(func("12345", "345"))

    def test_podstroka_ne_vhodit(self):
        self.assertFalse(func("abcdef","rty"))
        self.assertFalse(func("12345", "543"))

    def test_pustaya_stroka(self):
        self.assertEqual(func("", ""), "" in "")
        self.assertEqual(func("", "123"), "123" in "")
        self.assertEqual(func("123", ""), "" in "123")

if __name__ == '__main__':
    unittest.main()