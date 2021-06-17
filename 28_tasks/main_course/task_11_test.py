import unittest
from task_11 import LineAnalysis

class func_test(unittest.TestCase):
    def test_right_symbol(self):
        self.assertEqual(LineAnalysis("*..*..*..*..*..*..*"), True)
        self.assertEqual(LineAnalysis("*"), True)
        self.assertEqual(LineAnalysis("***"), True)
        self.assertEqual(LineAnalysis("*.......*.......*"), True)
        self.assertEqual(LineAnalysis("**"), True)
        self.assertEqual(LineAnalysis("*.*"), True)
        self.assertEqual(LineAnalysis("*..*...*..*..*..*..*"), False)
        self.assertEqual(LineAnalysis("*..*..*..*..*..**..*"), False)
        self.assertEqual(LineAnalysis("**..*..*..*..*..**..*"), False)
        self.assertEqual(LineAnalysis("**..*..*..*..*..**..**"), False)
        self.assertEqual(LineAnalysis("**..*"), False)
        self.assertEqual(LineAnalysis("**..***"), False)
        self.assertEqual(LineAnalysis("**.."), False) 
        self.assertEqual(LineAnalysis("*..**..**"), False)

  

if __name__ == '__main__':
    unittest.main()