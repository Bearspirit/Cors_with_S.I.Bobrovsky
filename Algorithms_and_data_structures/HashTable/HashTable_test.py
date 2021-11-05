import unittest
from HashTable import *


class TestOrderedListMethods(unittest.TestCase):
    def test_hash_fun(self):
        HT = HashTable(19, 3)
        self.assertEqual(HT.hash_fun('abc'), sum('abc'.encode('utf-8')) % HT.size)
        self.assertEqual(HT.hash_fun('ABC'), sum('ABC'.encode('utf-8')) % HT.size)

    def test_seek_slot(self):
        HT = HashTable(19, 3)
        self.assertEqual(HT.seek_slot('abc'), 9)
        self.assertEqual(HT.seek_slot('abbc'), 12)

    def test_seek_slot_in_full_table(self):
        HT = HashTable(19, 3)
        for i in range(0, HT.size):
            HT.slots[i] = 'abc' + str(i)      
        self.assertEqual(HT.seek_slot('abc'), None)
        self.assertEqual(HT.seek_slot('abbc'), None)
    
    def test_put(self):
        HT = HashTable(19, 3)
        self.assertEqual(HT.put('abc'), 9)
        self.assertEqual(HT.put('abbc'), 12)

    def test_find(self):
        HT = HashTable(19, 3)
        HT.put('abc')
        self.assertEqual(HT.find('abc'), 9)
        HT.put('abbc')
        self.assertEqual(HT.find('abbc'), 12)
    
    def test_global(self):
        HT = HashTable(19, 3)
        HT.put('abcdef')
        self.assertEqual(HT.find('abcdef'), 8)
        HT.put('bcdefa')
        self.assertEqual(HT.find('bcdefa'), 11)
        HT.put('cdefab')
        self.assertEqual(HT.find('cdefab'), 14)
        HT.put('defabc')
        self.assertEqual(HT.find('defabc'), 17)
        HT.put('efabcd')
        self.assertEqual(HT.find('efabcd'), 1)
        HT.put('fabcde')
        self.assertEqual(HT.find('fabcde'), 4)
        HT.put('fedcba')
        self.assertEqual(HT.find('fedcba'), 7)
        HT.put('edcbaf')
        self.assertEqual(HT.find('edcbaf'), 10)
        HT.put('dcbafe')
        self.assertEqual(HT.find('dcbafe'), 13)
        HT.put('cbafed')
        self.assertEqual(HT.find('cbafed'), 16)
        HT.put('bafedc')
        self.assertEqual(HT.find('bafedc'), 0)
        HT.put('afedcb')
        self.assertEqual(HT.find('afedcb'), 3)
        HT.put('acdefb')
        self.assertEqual(HT.find('acdefb'), 6)
        HT.put('adefbc')
        self.assertEqual(HT.find('adefbc'), 9)
        HT.put('aefbcd')
        self.assertEqual(HT.find('aefbcd'), 12)
        HT.put('afbcde')
        self.assertEqual(HT.find('afbcde'), 15)
        HT.put('abdefc')
        self.assertEqual(HT.find('abdefc'), 18)
        HT.put('abefcd')
        self.assertEqual(HT.find('abefcd'), 2)
        HT.put('abfcde')
        self.assertEqual(HT.find('abfcde'), 5)
        HT.put('abcefd')
        self.assertEqual(HT.find('abcefd'), None)
        HT.put('abefdc')
        self.assertEqual(HT.find('abefdc'), None)  


if __name__ == '__main__':
    unittest.main()