import unittest
from task_12_1 import MisterRobot

class func_test(unittest.TestCase):
    def test_right_symbol(self):
        self.assertEqual(MisterRobot(7, [1,3,4,5,6,2,7]), True)
        self.assertEqual(MisterRobot(10, [1,3,4,2,5,6,7,8,9,10]), True)
        self.assertEqual(MisterRobot(4, [1,3,4,2]), True)
        self.assertEqual(MisterRobot(4, [4,3,2,1]), False)
        self.assertEqual(MisterRobot(4, [1,2,4,3]), False)
        self.assertEqual(MisterRobot(4, [2,3,1,4]), True)
        self.assertEqual(MisterRobot(10, [1,3,4,9,5,6,7,8,2,10]), False)
        self.assertEqual(MisterRobot(10, [1,3,4,5,6,7,8,2,9,10]), True)
        self.assertEqual(MisterRobot(4, [1,4,2,3]), True)
        self.assertEqual(MisterRobot(7, [1,3,4,2,5,6,7]), True)
        self.assertEqual(MisterRobot(7, [1,7,4,2,5,6,3]), False)

        

if __name__ == '__main__':
    unittest.main()