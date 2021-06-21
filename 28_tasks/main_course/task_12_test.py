import unittest
from task_12 import MisterRobot

class func_test(unittest.TestCase):
    def test_right_symbol(self):
        self.assertEqual(MisterRobot(7, [1,3,4,5,6,2,7]), False)
        self.assertEqual(MisterRobot(7, [1,3,4,2,5,6,7]), True)
        self.assertEqual(MisterRobot(10, [1,3,4,2,5,6,7,8,9,10]), True)
        self.assertEqual(MisterRobot(4, [1,3,4,2]), True)
        self.assertEqual(MisterRobot(4, [4,3,2,1]), False)
        self.assertEqual(MisterRobot(4, [1,2,4,3]), False)
        self.assertEqual(MisterRobot(4, [2,1,3,4]), False)

        

if __name__ == '__main__':
    unittest.main()