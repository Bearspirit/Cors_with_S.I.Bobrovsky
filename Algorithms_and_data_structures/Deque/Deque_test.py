import unittest
from Deque import *

class TestLinkedListMethods(unittest.TestCase):
    def test_addFront(self):
        deq = Deque()
        deq.addFront(1)
        self.assertEqual(deq.size(), 1)
        deq.addFront(2)
        self.assertEqual(deq.size(), 2)
        deq.addFront(3)
        self.assertEqual(deq.size(), 3)
        self.assertEqual(deq.removeFront(), 3)
        self.assertEqual(deq.removeTail(), 1)
        self.assertEqual(deq.size(), 1)


    def test_addTail(self):
        deq = Deque()
        deq.addTail(1)
        self.assertEqual(deq.size(), 1)
        deq.addTail(2)
        self.assertEqual(deq.size(), 2)
        deq.addTail(3)
        self.assertEqual(deq.size(), 3)
        self.assertEqual(deq.removeTail(), 3)
        self.assertEqual(deq.removeFront(), 1)
        self.assertEqual(deq.size(), 1)
       


if __name__ == '__main__':
    unittest.main()