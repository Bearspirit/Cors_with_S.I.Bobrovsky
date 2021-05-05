import unittest
import random
from task_2 import SumOfThe

class func_test(unittest.TestCase):  
    def test_izvestnaya_summa(self):
        self.assertEqual(SumOfThe(3, [1, 2, 3]), 3)
        self.assertEqual(SumOfThe(5, [1, 10, 3, 2, 4]), 10)
        self.assertEqual(SumOfThe(6, [-20, 10, 20, -30, -5, -15]), -20)

if __name__ == '__main__':
    unittest.main()