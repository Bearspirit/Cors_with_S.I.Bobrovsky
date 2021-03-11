import unittest
from vst import func

class func_test(unittest.TestCase):

    def test_podstroka_ne_vhodit(self):
        self.assertNotEqual(func("abcdef","rty"), True)

    def test_podstroki_net(self):
        self.assertFalse(func("12345", "543"))

if __name__ == '__main__':
    unittest.main()