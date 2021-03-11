import unittest
from vst import func

class func_test(unittest.TestCase):
    def test_podstroka_vhodit(self):
        self.assertTrue(func("abcdef","cde"))
        self.assertTrue(func("12345", "345"))

    def test_podstroka_ne_vhodit(self):
        self.assertFalse(func("abcdef","rty"))
        self.assertFalse(func("12345", "543"))


if __name__ == '__main__':
    unittest.main()