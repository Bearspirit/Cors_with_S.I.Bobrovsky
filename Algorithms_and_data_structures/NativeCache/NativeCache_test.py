import unittest
from NativeCache import *


class TestOrderedListMethods(unittest.TestCase):
    def test_hash_fun(self):
        NC = NativeCache(19)
        self.assertEqual(NC.hash_fun('abc'), sum('abc'.encode('utf-8')) % NC.size)
        self.assertEqual(NC.hash_fun('ABC'), sum('ABC'.encode('utf-8')) % NC.size)

    def test_is_key(self):
        NC = NativeCache(19)
        NC.put('key1', 1)
        NC.put('key2', 2)
        self.assertEqual(NC.is_key('key1'), True)
        self.assertEqual(NC.is_key('key2'), True)

    def test_is_key_no_key_in_dict(self):
        NC = NativeCache(19)
        NC.put('key1', 1)
        NC.put('key2', 2)
        self.assertEqual(NC.is_key('key3'), False)

    def test_is_key_empty_dict(self):
        NC = NativeCache(19)
        self.assertEqual(NC.is_key('key3'), False)

    def test_put_full_dict(self):
        NC = NativeCache(19)
        for i in range(0, NC.size):
            NC.put('key'+str(i), i)
        for k in range(0, NC.size):
            self.assertEqual(NC.get('key'+str(k)), k)
        self.assertEqual(NC.get('key19'), None)
    
    def test_put_other_key_dict(self):
        NC = NativeCache(19)
        for i in range(0, NC.size):
            NC.put('key'+str(i), i)
        NC.put('key10', 20)
        self.assertEqual(NC.get('key10'), 20)
        self.assertEqual(NC.get('key11'), 11)

    def test_get_all_key_values_and_count_hits(self):
        NC = NativeCache(19)
        for i in range(0, NC.size):
            NC.put('key'+str(i), i)
        iter_count = 3
        while iter_count > 0:
            for i in range(0, NC.size):
                NC.get('key'+str(i))
            iter_count -= 1
        NC.put('key44', 44)
        self.assertIsNone(NC.get('key44'))
        self.assertEqual(NC.hits[NC.slots.index('key10')], 3)
        for i in range(0, NC.size-1):
                NC.get('key'+str(i))
        self.assertEqual(NC.hits[NC.slots.index('key18')], 3)
        self.assertEqual(NC.hits[NC.slots.index('key10')], 4)

    def test_replay(self):
        NC = NativeCache(19)
        for i in range(0, NC.size):
            NC.put('key'+str(i), i)
        iter_count = 3
        while iter_count > 0:
            for i in range(0, NC.size-1):
                NC.get('key'+str(i))
            iter_count -= 1
        NC.put('key44', 44)
        self.assertEqual(NC.get('key44'), 44)
        self.assertEqual(NC.hits[NC.slots.index('key44')], 1)


if __name__ == '__main__':
    unittest.main()