import unittest
from task_8 import Unmanned

class func_test(unittest.TestCase):
    def test_road_time(self):
        self.assertEqual(Unmanned(10, 2, [[2,2,2], [4,2,2]]), 12)
        self.assertEqual(Unmanned(10, 2, [[3,5,5], [5,2,2]]), 12)
        self.assertEqual(Unmanned(10, 2, [[11,5,5], [15,2,2]]), 10)
        self.assertEqual(Unmanned(10, 2, [[11,5,5], [15,2,2], [18,3,3]]), 10)
        self.assertEqual(Unmanned(10, 2, [[4,2,2], [7,3,3]]), 12)
        self.assertEqual(Unmanned(10, 1, [[10,2,2]]), 10)
        self.assertEqual(Unmanned(10, 1, [[9,2,2]]), 11)
        self.assertEqual(Unmanned(10, 2, [[4,1,1],[10,3,3]]), 11)

        

if __name__ == '__main__':
    unittest.main()