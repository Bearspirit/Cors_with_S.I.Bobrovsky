import unittest
from task_9 import TankRush

class func_test(unittest.TestCase):
    def test_road_time(self):
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 2, 2, "34 98"), True)
        self.assertEqual(TankRush(3, 4, "1234 2334 0987", 2, 2, "34 98"), False)
        self.assertEqual(TankRush(3, 4, "1234 3456 9876", 2, 2, "34 98"), True)
        self.assertEqual(TankRush(3, 4, "1234 3498 9876", 2, 2, "34 98"), True)
        self.assertEqual(TankRush(3, 4, "3412 2334 0987", 2, 2, "34 98"), False)
        self.assertEqual(TankRush(3, 4, "3412 2335 0798", 2, 2, "34 98"), False)

        

        

if __name__ == '__main__':
    unittest.main()