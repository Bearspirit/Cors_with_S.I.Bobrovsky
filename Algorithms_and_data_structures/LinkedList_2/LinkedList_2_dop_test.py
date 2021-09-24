import unittest
from LinkedList_2_dop import *


class TestLinkedListMethods(unittest.TestCase):
    
    def test_delete_one_head_element(self):
        LL5 = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        LL5.add_in_tail(n1)
        LL5.add_in_tail(n2)
        LL5.add_in_tail(n3)
        LL5.delete(1)
        self.assertEqual(LL5.head, n2)
        self.assertEqual(LL5.tail, n3)

    def test_delete_one_tail_element(self):
        LL5 = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        LL5.add_in_tail(n1)
        LL5.add_in_tail(n2)
        LL5.add_in_tail(n3)
        LL5.delete(3)
        self.assertEqual(LL5.head, n1)
        self.assertEqual(LL5.tail, n2)

    def test_delete_one_middle_element(self):
        LL5 = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        LL5.add_in_tail(n1)
        LL5.add_in_tail(n2)
        LL5.add_in_tail(n3)
        LL5.delete(2)
        self.assertEqual(LL5.head, n1)
        self.assertEqual(LL5.tail, n3)

    def test_delete_all_head_and_tail_elements(self):
        LL5 = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(1)
        LL5.add_in_tail(n1)
        LL5.add_in_tail(n2)
        LL5.add_in_tail(n3)
        LL5.add_in_tail(n4)
        LL5.delete(1, all=True)
        self.assertEqual(LL5.head, n2)
        self.assertEqual(LL5.tail, n3)

    def test_delete_all_middle_elements(self):
        LL5 = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(2)
        n4 = Node(3)
        LL5.add_in_tail(n1)
        LL5.add_in_tail(n2)
        LL5.add_in_tail(n3)
        LL5.add_in_tail(n4)
        LL5.delete(2, all=True)
        self.assertEqual(LL5.head, n1)
        self.assertEqual(LL5.tail, n4)
        self.assertEqual(LL5.head.next, n4)
        self.assertEqual(LL5.tail.prev, n1)

    def test_delete_empty_element(self):
        LL5 = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(2)
        n4 = Node(3)
        LL5.add_in_tail(n1)
        LL5.add_in_tail(n2)
        LL5.add_in_tail(n3)
        LL5.add_in_tail(n4)
        LL5.delete(5, all=True)
        self.assertEqual(LL5.head, n1)
        self.assertEqual(LL5.tail, n4)
        self.assertEqual(LL5.head.next, n2)
        self.assertEqual(LL5.tail.prev, n3)

    def test_delete_all_elements_in_full_list(self):
        LL5 = LinkedList2()
        n1 = Node(1)
        n2 = Node(1)
        n3 = Node(1)
        n4 = Node(1)
        LL5.add_in_tail(n1)
        LL5.add_in_tail(n2)
        LL5.add_in_tail(n3)
        LL5.add_in_tail(n4)
        LL5.delete(1, all=True)
        self.assertEqual(LL5.len(), 0)
        self.assertEqual(LL5.head, None)
        self.assertEqual(LL5.tail, None)

    def test_delete_three_elements_from_four_head(self):
        LL5 = LinkedList2()
        n1 = Node(2)
        n2 = Node(1)
        n3 = Node(1)
        n4 = Node(1)
        LL5.add_in_tail(n1)
        LL5.add_in_tail(n2)
        LL5.add_in_tail(n3)
        LL5.add_in_tail(n4)
        LL5.delete(1, all=True)
        self.assertEqual(LL5.len(), 1)
        self.assertEqual(LL5.head, n1)
        self.assertEqual(LL5.tail, n1)

    def test_delete_three_elements_from_four_tail(self):
        LL5 = LinkedList2()
        n1 = Node(1)
        n2 = Node(1)
        n3 = Node(1)
        n4 = Node(2)
        LL5.add_in_tail(n1)
        LL5.add_in_tail(n2)
        LL5.add_in_tail(n3)
        LL5.add_in_tail(n4)
        LL5.delete(1, all=True)
        self.assertEqual(LL5.len(), 1)
        self.assertEqual(LL5.head, n4)
        self.assertEqual(LL5.tail, n4)
      
    def test_insert_in_empty_list_after_None(self):
        LL8 = LinkedList2()
        LL8.insert(None, Node(1))
        self.assertEqual(LL8.head.value, 1)
        self.assertEqual(LL8.tail.value, 1)
        self.assertEqual(LL8.len(), 1)

    def test_insert_in_not_empty_list_after_None(self):
        LL9 = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        LL9.add_in_tail(n1)
        LL9.add_in_tail(n2)
        LL9.add_in_tail(n3)
        LL9.insert(None, Node(4))
        self.assertEqual(LL9.head.value, 1)
        self.assertEqual(LL9.tail.value, 4)
        self.assertEqual(LL9.len(), 4)

    def test_isert_after_head_of_list(self):
        LL10 = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        LL10.add_in_tail(n1)
        LL10.add_in_tail(n2)
        LL10.add_in_tail(n3)
        LL10.insert(n1, n4)
        self.assertEqual(LL10.len(), 4)
        self.assertEqual(LL10.head, n1)
        self.assertEqual(LL10.tail, n3)

    def test_isert_in_tail_of_list(self):
        LL11 = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        LL11.add_in_tail(n1)
        LL11.add_in_tail(n2)
        LL11.add_in_tail(n3)
        LL11.insert(n3, n4)
        self.assertEqual(LL11.len(), 4)
        self.assertEqual(LL11.head, n1)
        self.assertEqual(LL11.tail, n4)

    def test_isert_in_middle_of_list_1(self):
        LL12 = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        LL12.add_in_tail(n1)
        LL12.add_in_tail(n2)
        LL12.add_in_tail(n3)
        LL12.insert(n2, n4)
        self.assertEqual(LL12.len(), 4)
        self.assertEqual(LL12.head, n1)
        self.assertEqual(LL12.tail, n3)

    def test_isert_in_middle_of_list_2(self):
        LL13 = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        LL13.add_in_tail(n1)
        LL13.add_in_tail(n2)
        LL13.add_in_tail(n3)
        LL13.insert(n1, n4)
        self.assertEqual(LL13.len(), 4)
        self.assertEqual(LL13.head, n1)
        self.assertEqual(LL13.tail, n3)


    def test_only_insert_in_list(self):
        LL = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(5)
        LL.insert(None, n1)
        LL.insert(n1, n2)
        self.assertEqual(LL.tail, n2)
        LL.insert(n2, n3)
        LL.insert(n3, n4)
        self.assertEqual(LL.head, n1)
        self.assertEqual(LL.tail, n4)
        self.assertEqual(LL.len(), 4)
 


if __name__ == '__main__':
    unittest.main()