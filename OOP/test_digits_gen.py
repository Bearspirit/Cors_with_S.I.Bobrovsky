import unittest
import random
from vst import func
from digits_gen import string_gen

class func_test(unittest.TestCase):
    def test_podstroka_vhodit(self):
        self.assertTrue(func("abcdef","cde"))
        self.assertTrue(func("12345", "345"))

    def test_podstroka_ne_vhodit(self):
        self.assertFalse(func("abcdef","rty"))
        self.assertFalse(func("12345", "543"))

    def test_pustaya_stroka(self):
        self.assertEqual(func("", ""), "" in "")
        self.assertEqual(func("", "123"), "123" in "")
        self.assertEqual(func("123", ""), "" in "123")


    def test_proverka_pdstrk(self):
        for i in range(10000):
            a = string_gen(2000000)
            b = string_gen(random.randint(0, 5))
            self.assertEqual(func(a, b), b in a)

      
if __name__ == '__main__':
    unittest.main()