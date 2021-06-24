import unittest
from task_13 import ShopOLAP

class func_test(unittest.TestCase):
    def test_right_symbol(self):
        self.assertEqual(ShopOLAP(5, ["платье1 5", "сумка32 2", "платье1 1", "сумка23 2", "сумка128 4"]), 
        ['платье1 6', 'сумка128 4', 'сумка23 2', 'сумка32 2'])
        self.assertEqual(ShopOLAP(5, ["платье1 5", "платье1 5", "платье1 1", "платье1 5", "платье1 5"]), 
        ['платье1 21'])
        self.assertEqual(ShopOLAP(5, ["платье123 5", "платье12 5", "платье132 1", "платье1 5", "платье1 5"]), 
        ['платье1 10', "платье12 5", "платье123 5", "платье132 1"])
       

        

if __name__ == '__main__':
    unittest.main()