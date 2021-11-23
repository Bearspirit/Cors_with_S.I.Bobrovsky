import unittest
from BloomFilter import *

class TestBloomFilterMethods(unittest.TestCase):
    def test_all_elements_into_filter(self):
        BF = BloomFilter(32)
        test_arr = ['0123456789', '1234567890', '2345678901', '3456789012', '4567890123', '5678901234',
        '6789012345', '7890123456', '8901234567', '9012345678']
        for element in test_arr:
            BF.add(element)
            self.assertTrue(BF.is_value(element))

    def test_element_not_into_filter(self):
        BF = BloomFilter(32)
        BF.add('0123456789')
        self.assertFalse(BF.is_value('Бобровский'))

    

            





if __name__ == '__main__':
    unittest.main()