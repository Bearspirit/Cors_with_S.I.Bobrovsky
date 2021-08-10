import unittest
from task_20 import white_walkers

class SherlockValidString_test(unittest.TestCase):
    def test_walkers_is_true(self):
        self.assertTrue(white_walkers("axxb6===4xaf5===eee5"))
        self.assertTrue(white_walkers("abc=7==hdjs=3gg1=======5"))
        self.assertTrue(white_walkers("9===1===9===1===9"))
        self.assertTrue(white_walkers("9=cd==1==ab=9=e==1=f=g=9"))
        self.assertTrue(white_walkers("axxb6===4xaf5===eee6"))
        self.assertTrue(white_walkers("axxb6===4"))
        self.assertTrue(white_walkers("6===4"))
        self.assertTrue(white_walkers("6===4xa===f5===eee6==afada=4"))

        
       
    def test_walkers_is_False(self):
        self.assertFalse(white_walkers("5==ooooooo=5=5"))
        self.assertFalse(white_walkers("aaS=8"))
        self.assertFalse(white_walkers("9abc1===9===1===9"))
        self.assertFalse(white_walkers(""))
        self.assertFalse(white_walkers("9==1===9===1===9"))
        self.assertFalse(white_walkers("9====1===9===1===9"))
        self.assertFalse(white_walkers("axxb6===4xaf6===eee5"))
        self.assertFalse(white_walkers("6====4"))
        self.assertFalse(white_walkers("6==4"))
        self.assertFalse(white_walkers("6===4xa===f5===eee6==afada4"))
       



if __name__ == '__main__':
    unittest.main()