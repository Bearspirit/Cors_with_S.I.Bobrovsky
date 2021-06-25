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
        self.assertEqual(ShopOLAP(5,['dress1 5','handbug32 3','dress2 1','handbug23 2','handbug128 4']), 
        ['dress1 5','handbug128 4','handbug32 3','handbug23 2','dress2 1'])
        self.assertEqual(ShopOLAP(5,['dress1 5','handbug32 3','dress2 1','handbug23 3','handbug128 4']), 
        ['dress1 5','handbug128 4','handbug23 3','handbug32 3','dress2 1'])
       

        

if __name__ == '__main__':
    unittest.main()