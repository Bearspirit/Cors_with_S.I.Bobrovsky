import unittest
from Linked_List import *


class TestLinkedListMethods(unittest.TestCase):

    def test_delete_one_element(self):
        L1 = LinkedList()
        L1.add_in_tail(Node(1))
        self.assertEqual(L1.head, L1.tail)
        self.assertEqual(L1.head.value, 1)
        L1.delete(1)
        self.assertIsNone(L1.head)
        self.assertIsNone(L1.tail)

    def test_delete_missing(self):
        L2 = LinkedList()
        L2.add_in_tail(Node(1))
        self.assertEqual(L2.head, L2.tail)
        self.assertEqual(L2.head.value, 1)
        L2.delete(3)
        self.assertEqual(L2.head, L2.tail)
        self.assertEqual(L2.head.value, 1)
        self.assertIsNone(L2.head.next)

    def test_delete_head_element(self):
        L3 = LinkedList()
        L3.add_in_tail(Node(1))
        L3.add_in_tail(Node(2))
        self.assertEqual(L3.head.value, 1)
        self.assertEqual(L3.tail.value, 2)
        L3.delete(1)
        self.assertEqual(L3.head, L3.tail)
        self.assertEqual(L3.head.value, 2)
        self.assertIsNone(L3.head.next)

    def test_delete_tail_element(self):
        L4 = LinkedList()
        L4.add_in_tail(Node(1))
        L4.add_in_tail(Node(2))
        self.assertEqual(L4.head.value, 1)
        self.assertEqual(L4.tail.value, 2)
        L4.delete(2)
        self.assertEqual(L4.head, L4.tail)
        self.assertEqual(L4.head.value, 1)
        self.assertIsNone(L4.head.next)

    def test_delete_middle_element(self):
        L5 = LinkedList()
        L5.add_in_tail(Node(1))
        L5.add_in_tail(Node(2))
        L5.add_in_tail(Node(3))
        self.assertEqual(L5.head.value, 1)
        self.assertEqual(L5.head.next.value, 2)
        self.assertEqual(L5.tail.value, 3)
        L5.delete(2)
        self.assertEqual(L5.head.value, 1)
        self.assertEqual(L5.head.next, L5.tail)
        self.assertEqual(L5.tail.value, 3)
        self.assertIsNone(L5.tail.next)

    def test_delete_all_elements(self):
        L6 = LinkedList()
        n1 = Node(1)
        n2 = Node(1)
        n3 = Node(1)
        L6.add_in_tail(n1)
        L6.add_in_tail(n2)
        L6.add_in_tail(n3)
        L6.delete(1, all=True)
        self.assertIsNone(L6.head)
        self.assertIsNone(L6.tail)

    def test_delete_all_nodes(self):
        L6_1 = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(1)
        n5 = Node(4)
        n6 = Node(1)
        L6_1.add_in_tail(n1)
        L6_1.add_in_tail(n2)
        L6_1.add_in_tail(n3)
        L6_1.add_in_tail(n4)
        L6_1.add_in_tail(n5)
        L6_1.add_in_tail(n6)
        L6_1.delete(1, all=True)
        self.assertEqual(L6_1.head, n2)
        self.assertEqual(L6_1.tail, n5)

    def test_delete_first_element(self):
        L7 = LinkedList()
        n1 = Node(1)
        n2 = Node(1)
        n3 = Node(1)
        L7.add_in_tail(n1)
        L7.add_in_tail(n2)
        L7.add_in_tail(n3)
        L7.delete(1, all=False)
        self.assertEqual(L7.head, n2)
        self.assertEqual(L7.tail, n3)
        self.assertEqual(L7.head.next, n3)
        self.assertIsNone(L7.tail.next)
    
    def test_delete_function_for_empty_list(self):
        L8 = LinkedList()
        L8.delete(1)
        self.assertIsNone(L8.tail)
        self.assertIsNone(L8.head)
        n1 = Node(1)
        n2 = Node(2)
        L8.add_in_tail(n1)
        L8.add_in_tail(n2)
        self.assertEqual(L8.len(), 2)
        L8.clean()
        self.assertEqual(L8.len(), 0)
        L8.delete(None)
        self.assertIsNone(L8.tail)
        self.assertIsNone(L8.head)


    def test_clean(self):
        L9 = LinkedList()
        n1 = Node(1)
        n2 = Node(1)
        n3 = Node(1)
        L9.add_in_tail(n1)
        L9.add_in_tail(n2)
        L9.add_in_tail(n3)
        L9.clean()
        self.assertIsNone(L9.head)
        self.assertIsNone(L9.tail)

    def test_find_all_elements(self):
        L10 = LinkedList()
        n1 = Node(1)
        n2 = Node(1)
        n3 = Node(2)
        L10.add_in_tail(n1)
        L10.add_in_tail(n2)
        L10.add_in_tail(n3)
        self.assertEqual(L10.find_all(1), [n1, n2])

    def test_find_all_missing_element(self):
        L11 = LinkedList()
        n1 = Node(1)
        n2 = Node(1)
        n3 = Node(1)
        L11.add_in_tail(n1)
        L11.add_in_tail(n2)
        L11.add_in_tail(n3)
        self.assertEqual(L11.find_all(2), [])

    def test_find_all_empty_list(self):
        L12 = LinkedList()
        self.assertEqual(L12.find_all(1), [])

    def test_len(self):
        L13 = LinkedList()
        self.assertEqual(L13.len(), 0)
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        L13.add_in_tail(n1)
        L13.add_in_tail(n2)
        L13.add_in_tail(n3)
        self.assertEqual(L13.len(), 3)

    def test_insert_in_middle(self):
        L14 = LinkedList()
        n1 = Node(1)
        n2 = Node(1)
        n3 = Node(2)
        L14.add_in_tail(n1)
        L14.add_in_tail(n2)
        L14.insert(n1, n3)
        self.assertEqual(L14.head, n1)
        self.assertEqual(L14.head.next, n3)
        self.assertEqual(L14.head.next.next, n2)
        self.assertEqual(L14.tail, n2)

    def test_insert_in_tail(self):
        L15 = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        L15.add_in_tail(n1)
        L15.add_in_tail(n2)
        L15.insert(n2, n3)
        self.assertEqual(L15.head, n1)
        self.assertEqual(L15.head.next, n2)
        self.assertEqual(L15.head.next.next, n3)
        self.assertEqual(L15.tail, n3)

    def test_insert_after_none(self):
        L16 = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        L16.add_in_tail(n1)
        L16.add_in_tail(n2)
        L16.insert(None, n3)
        self.assertEqual(L16.head, n3)
        self.assertEqual(L16.head.next, n1)
        self.assertEqual(L16.head.next.next, n2)
        self.assertEqual(L16.tail, n2)

    def test_insert_in_empty_llist(self):
        L17 = LinkedList()
        L17.insert(None, Node(1))
        self.assertEqual(L17.head.value, 1)

if __name__ == '__main__':
    unittest.main()