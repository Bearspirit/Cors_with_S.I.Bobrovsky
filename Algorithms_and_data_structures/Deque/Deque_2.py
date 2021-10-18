class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.insert(0,item)

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.size() > 0:
            return self.deque.pop(0)
        return None # если очередь пуста

    def removeTail(self):
        if self.size() > 0:
            return self.deque.pop()
        return None # если очередь пуста

    def size(self):
        return len(self.deque)

def Palindrom(text):
    deq_text = Deque()
    for i in range(0, len(text)):
        deq_text.addTail(text[i])
    while deq_text.size() > 1:
        if deq_text.removeFront() != deq_text.removeTail():
            return False
    return True
