import unittest
from PowerSet import *

class TestPowerSetMethods(unittest.TestCase):
    def test_put_alot_elements(self):
        PS = PowerSet()
        for i in range(0, 20000):
            PS.put(str(i))
        self.assertEqual(PS.size(), 20000)

    def test_put_double_element(self):
        PS = PowerSet()
        PS.put('1')
        PS.put('1')
        PS.put('1')
        self.assertEqual(PS.size(), 1)

    def test_intersection_full_cross(self):
        set1 = PowerSet()
        set1.put('1')
        set1.put('2')
        set1.put('3')
        set2 = PowerSet()
        set2.put('1')
        set2.put('2')
        set2.put('3')
        cross_set = set1.intersection(set2)
        self.assertEqual(cross_set.size(), 3)

    def test_intersection_empty_cross(self):
        set1 = PowerSet()
        set1.put('1')
        set1.put('2')
        set1.put('3')
        set2 = PowerSet()
        set2.put('4')
        set2.put('5')
        set2.put('6')
        cross_set = set1.intersection(set2)
        self.assertEqual(cross_set.size(), 0)

    def test_intersection_part_cross(self):
        set1 = PowerSet()
        set1.put('1')
        set1.put('2')
        set1.put('3')
        set2 = PowerSet()
        set2.put('1')
        set2.put('3')
        set2.put('6')
        cross_set = set1.intersection(set2)
        self.assertEqual(cross_set.size(), 2)

    def test_union_for_same_sets(self):
        set1 = PowerSet()
        set1.put('1')
        set1.put('2')
        set1.put('3')
        set2 = PowerSet()
        set2.put('1')
        set2.put('2')
        set2.put('3')
        union_set = set1.union(set2)
        self.assertEqual(union_set.size(), 3)

    def test_union_for_empty_set(self):
        set1 = PowerSet()
        set1.put('1')
        set1.put('2')
        set1.put('3')
        set2 = PowerSet()
        union_set = set1.union(set2)
        self.assertEqual(union_set.size(), 3)

    def test_union_for_part_same_sets(self):
        set1 = PowerSet()
        set1.put('1')
        set1.put('2')
        set1.put('3')
        set2 = PowerSet()
        set2.put('1')
        set2.put('2')
        set2.put('4')
        set2.put('5')
        union_set = set1.union(set2)
        self.assertEqual(union_set.size(), 5)

    def test_union_for_absolutly_different_sets(self):
        set1 = PowerSet()
        set1.put('1')
        set1.put('2')
        set1.put('3')
        set2 = PowerSet()
        set2.put('6')
        set2.put('7')
        set2.put('4')
        set2.put('5')
        union_set = set1.union(set2)
        self.assertEqual(union_set.size(), 7)

    def test_difference_for_same_sets(self):
        set1 = PowerSet()
        set1.put('1')
        set1.put('2')
        set1.put('3')
        set2 = PowerSet()
        set2.put('1')
        set2.put('2')
        set2.put('3')
        diff_set = set1.difference(set2)
        self.assertEqual(diff_set.size(), 0)

    def test_difference_for_part_same_sets(self):
        set1 = PowerSet()
        set1.put('1')
        set1.put('2')
        set1.put('3')
        set2 = PowerSet()
        set2.put('4')
        set2.put('2')
        set2.put('6')
        diff_set = set1.difference(set2)
        self.assertEqual(diff_set.size(), 2)

    def test_difference_for_differents_sets(self):
        set1 = PowerSet()
        set1.put('1')
        set1.put('2')
        set1.put('3')
        set2 = PowerSet()
        set2.put('4')
        set2.put('5')
        set2.put('6')
        diff_set = set1.difference(set2)
        self.assertEqual(diff_set.size(), 3)

    def test_issubset_for_differents_sets(self):
        set1 = PowerSet()
        set1.put('1')
        set1.put('2')
        set1.put('3')
        set2 = PowerSet()
        set2.put('4')
        set2.put('5')
        set2.put('6')
        self.assertFalse(set1.issubset(set2))

    def test_issubset_for_all_set2elements_in_set1(self):
        set1 = PowerSet()
        set1.put('1')
        set1.put('2')
        set1.put('3')
        set1.put('4')
        set1.put('5')
        set1.put('6')
        set2 = PowerSet()
        set2.put('4')
        set2.put('5')
        set2.put('6')
        self.assertTrue(set1.issubset(set2))

    def test_issubset_for_all_set1elements_in_set2(self):
        set1 = PowerSet()
        set1.put('1')
        set1.put('2')
        set1.put('3')
        set2 = PowerSet()
        set2.put('1')
        set2.put('2')
        set2.put('3')
        set2.put('4')
        set2.put('5')
        set2.put('6')
        self.assertFalse(set1.issubset(set2))

def test_issubset_if_not_all_set2elements_in_set1(self):
        set1 = PowerSet()
        set1.put('1')
        set1.put('2')
        set1.put('3')
        set1.put('4')
        set1.put('5')
        set1.put('6')
        set2 = PowerSet()
        set2.put('4')
        set2.put('5')
        set2.put('6')
        set2.put('7')
        self.assertFalse(set1.issubset(set2))
 

if __name__ == '__main__':
    unittest.main()