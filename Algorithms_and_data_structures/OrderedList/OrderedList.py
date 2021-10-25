class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return +1
        else:
            return 0
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2

    def add(self, value):
        node = self.head
        new_node = Node(value)
        if self.len() == 0:
            self.head = new_node
            self.tail = new_node
        else:
            if self.__ascending:
                while node is not None:
                    if self.compare(node.value, value) == +1:
                        if node == self.head:
                            new_node.next = self.head
                            self.head.prev = new_node
                            self.head = new_node
                        else:
                            node.prev.next = new_node
                            new_node.prev = node.prev
                            new_node.next = node
                            node.prev = new_node
                        return
                    node = node.next
            else:
                while node is not None:
                    if self.compare(node.value, value) == -1:
                        if node == self.head:
                            new_node.next = self.head
                            self.head.prev = new_node
                            self.head = new_node
                        else:
                            node.prev.next = new_node
                            new_node.prev = node.prev
                            new_node.next = node
                            node.prev = new_node
                        return
                    node = node.next
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        # автоматическая вставка value 
        # в нужную позицию

    def find(self, val):
        node = self.head
        if self.__ascending:
            while node is not None:
                if node.value == val:
                    return node
                elif self.compare(node.value, val) == +1:
                    return None
                node = node.next
        else:
            while node is not None:
                if node.value == val:
                    return node
                elif self.compare(node.value, val) == -1:
                    return None
                node = node.next


    def delete(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                if self.head is node:
                    self.head = node.next
                    if node.next is not None:
                        node.next.prev = None
                    else:
                        self.head = None
                        self.tail = None
                elif self.tail is node:
                    self.tail = node.prev
                    node.prev.next = None
                else:
                    node.next.prev = node.prev
                    node.prev.next = node.next
                break
            node = node.next
        

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None
    

    def len(self):
        node = self.head
        len_list = 0
        while node is not None:
            len_list += 1
            node = node.next
        return len_list

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        s1 = v1.strip()
        s2 = v2.strip()
        if s1 < s2:
            return -1
        elif s1 > s2:
            return +1
        else:
            return 0

