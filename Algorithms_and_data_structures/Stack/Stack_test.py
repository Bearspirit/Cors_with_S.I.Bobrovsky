import unittest
from Stack import *

class TestLinkedListMethods(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.size(), 1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)
        stack.push(3)
        self.assertEqual(stack.size(), 3)

    def test_peek(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        stack.peek()
        self.assertEqual(stack.size(), 3)

    def test_empy_peek(self):
        stack = Stack()   
        self.assertIsNone(stack.peek()) 

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.pop()
        self.assertEqual(stack.size(), 2)
        stack.pop()
        self.assertEqual(stack.size(), 1)
        stack.pop()
        self.assertEqual(stack.size(), 0)
        self.assertIsNone(stack.pop())

if __name__ == '__main__':
    unittest.main()