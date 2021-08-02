import unittest
from task_18_1 import MatrixTurn

class SherlockValidString_test(unittest.TestCase):
    def test_Andrassil(self):
        self.assertEqual(MatrixTurn(["123456", "234567", "345678", "456789"], 4,6, 1), ['212345', '343456', '456767', '567898'])
        self.assertEqual(MatrixTurn(["123456", "234567", "345678", "456789"], 4,6, 3), ['432123', '565434', '676545', '789876'])
        self.assertEqual(MatrixTurn(["12", "34"], 2,2, 1), ['31', '42'])
        self.assertEqual(MatrixTurn(["12", "34"], 2,2, 4), ["12", "34"])
        self.assertEqual(MatrixTurn(["123456", "234567", "345678", "456789"], 4,6, 16), ["123456", "234567", "345678", "456789"])
        self.assertEqual(MatrixTurn(["000000", "111111", "000000", "111111", "000000", "111111"], 6,6, 1), ["100000", "001110", "111011", "001000", "100011", "111110"])

        

if __name__ == '__main__':
    unittest.main()