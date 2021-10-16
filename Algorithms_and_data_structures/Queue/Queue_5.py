class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None 

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None 

class Queue:
    def __init__(self):
        self.queue_1 = Stack()
        self.queue_2 = Stack()

    def enqueue(self, item):
        self.queue_1.push(item)

    def dequeue(self):
        if self.queue_1.size() > 0:
            while self.queue_1.size() > 0:
                self.queue_2.push(self.queue_1.pop())
            a = self.queue_2.peek()
            self.queue_2.pop()
            while self.queue_2.size() > 0:
                self.queue_1.push(self.queue_2.pop())
            return a
        return None # если очередь пустая

    def size(self):
        return self.queue_1.size()

