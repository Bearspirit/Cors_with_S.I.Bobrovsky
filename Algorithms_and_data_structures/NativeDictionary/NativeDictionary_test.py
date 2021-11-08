import unittest
from NativeDictionary import *


class TestOrderedListMethods(unittest.TestCase):
    def test_hash_fun(self):
        ND = NativeDictionary(19)
        self.assertEqual(ND.hash_fun('abc'), sum('abc'.encode('utf-8')) % ND.size)
        self.assertEqual(ND.hash_fun('ABC'), sum('ABC'.encode('utf-8')) % ND.size)

    def test_is_key(self):
        ND = NativeDictionary(19)
        ND.put('key1', 1)
        ND.put('key2', 2)
        self.assertEqual(ND.is_key('key1'), True)
        self.assertEqual(ND.is_key('key2'), True)

    def test_is_key_no_key_in_dict(self):
        ND = NativeDictionary(19)
        ND.put('key1', 1)
        ND.put('key2', 2)
        self.assertEqual(ND.is_key('key3'), False)

    def test_is_key_empty_dict(self):
        ND = NativeDictionary(19)
        self.assertEqual(ND.is_key('key3'), False)

    def test_put_full_dict(self):
        ND = NativeDictionary(19)
        for i in range(0, ND.size):
            ND.put('key'+str(i), i)
        for k in range(0, ND.size):
            self.assertEqual(ND.get('key'+str(k)), k)
        self.assertEqual(ND.get('key19'), None)
    
    def test_put_other_key_dict(self):
        ND = NativeDictionary(19)
        for i in range(0, ND.size):
            ND.put('key'+str(i), i)
        ND.put('key10', 20)
        self.assertEqual(ND.get('key10'), 20)
        self.assertEqual(ND.get('key11'), 11)
       

if __name__ == '__main__':
    unittest.main()