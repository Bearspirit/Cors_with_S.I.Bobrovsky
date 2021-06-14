import unittest
from task_10 import MaximumDiscount

class func_test(unittest.TestCase):
    def test_road_time(self):
        self.assertEqual(MaximumDiscount(9, [300, 350, 400, 250, 200, 150, 100, 75, 50]), 500)
        self.assertEqual(MaximumDiscount(7, [300, 350, 400, 250, 200, 150, 100]), 450)
        self.assertEqual(MaximumDiscount(3, [300, 350, 400, ]), 300)
        self.assertEqual(MaximumDiscount(2, [300, 350,]), 0)
        self.assertEqual(MaximumDiscount(7, [300, 350, 400, 250, 100, 100, 100]), 400)
        self.assertEqual(MaximumDiscount(6, [300, 350, 400, 250, 200, 150]), 450)
        self.assertEqual(MaximumDiscount(8, [300, 350, 400, 250, 200, 150, 100, 75]), 450)
        self.assertEqual(MaximumDiscount(9, [200, 200, 200, 200, 200, 200, 200, 200, 200]), 600)
       
  

if __name__ == '__main__':
    unittest.main()