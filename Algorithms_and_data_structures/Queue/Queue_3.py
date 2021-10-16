class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        return None # если очередь пустая

    def size(self):
        return len(self.queue)

    def rotate(self, N):
        if (self.size() > 0) and (N > 0):
            while N > 0:
                self.queue.append(self.dequeue())
                N -= 1
        else:
            return None
             


