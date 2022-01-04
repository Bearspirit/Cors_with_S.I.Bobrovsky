class Queue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        if self.size() > 0:
            return self.__queue.pop(0)
        return None # если очередь пустая

    def size(self):
        return len(self.__queue)

