import unittest
from task_5 import BigMinus

class func_test(unittest.TestCase):
    def test_pravilnost_raznizy(self):
        self.assertEqual(BigMinus("1000", "1"), "999")
        self.assertEqual(BigMinus("10000000000000000", "1"), "9999999999999999")
        self.assertEqual(BigMinus("1", "1000"), "999")
        self.assertEqual(BigMinus("1000", "1000"), "0")
        

if __name__ == '__main__':
    unittest.main()