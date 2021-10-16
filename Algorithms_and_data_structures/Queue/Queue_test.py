import unittest
from Queue import *

class TestLinkedListMethods(unittest.TestCase):
    def test_enqueue_function(self):
        qu = Queue()
        qu.enqueue(1)
        qu.enqueue(2)
        qu.enqueue(3)
        self.assertEqual(qu.size(), 3)

    def test_dequeue_function(self):
        qu = Queue()
        qu.enqueue(1)
        qu.enqueue(2)
        qu.enqueue(3)
        self.assertEqual(qu.size(), 3)
        qu.dequeue()
        self.assertEqual(qu.size(), 2)
        qu.dequeue()
        self.assertEqual(qu.size(), 1)
        qu.dequeue()
        self.assertEqual(qu.size(), 0)
    
    def test_dequeue_empty(self):
        qu = Queue()
        self.assertIsNone(qu.dequeue())
    
    def test_print_dequeue(self):
        qu = Queue()
        qu.enqueue(1)
        qu.enqueue(2)
        qu.enqueue(3)
        self.assertEqual(qu.dequeue(), 1)
        self.assertEqual(qu.dequeue(), 2)
        self.assertEqual(qu.dequeue(), 3)
        

if __name__ == '__main__':
    unittest.main()    