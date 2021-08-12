import unittest
from task_21 import Football

class SherlockValidString_test(unittest.TestCase):
    def test_walkers_is_true(self):
        self.assertTrue(Football([1,3,2], 3))
        self.assertTrue(Football([3,2,1], 3))
        self.assertTrue(Football([1,7,5,3,9], 5))
        self.assertTrue(Football([1,4,3,2,5], 5))
        self.assertTrue(Football([0], 1))
        self.assertTrue(Football([4,3,2,5], 4))
        self.assertTrue(Football([4,3,2,5,6,7,8], 7))
        self.assertTrue(Football([1,2,3,8,7,6], 6))
        self.assertTrue(Football([1,2,3,8,7,6,5,4], 8))

        
       
    def test_walkers_is_False(self):
        self.assertFalse(Football([9,5,3,7,1], 5))
        self.assertFalse(Football([4,3,2,5,10,9,8,7], 8))
        self.assertFalse(Football([1,3,5,4,8,6,7,9], 8))
        self.assertFalse(Football([1,2,3,5,6,4,7,9], 8))
       
       



if __name__ == '__main__':
    unittest.main()