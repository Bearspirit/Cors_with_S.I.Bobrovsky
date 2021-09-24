class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class DummyLinkedList():
    def __init__(self, dummy_h=None, dummy_t=None):
        self.head = None
        self.tail = None
        self.dummy_h = dummy_h
        self.dummi_t = dummy_t

       

    def set_dummy(self, node=None):
        if node is None:
            return None
        else:
            self.dummy_h = Node(True)
            self.dummy_t = Node(True)
            self.dummy_h.next = self.head
            self.head.prev = self.dummy_h
            self.head = self.dummy_h
            self.tail.next = self.dummy_t
            self.dummy_t.prev = self.tail
            self.tail = self.dummy_t

    def del_dummy(self, l):
        if l <= 2:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.dummy_h = None
            self.dummi_t = None
            
            
class LinkedList2(DummyLinkedList):  
    def __init__(self):
        super().__init__()
    
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def delete(self, val, all=False):
        node = self.head
        DummyLinkedList.set_dummy(self, node)
        while node is not None:
            if node.value == val:
                node.next.prev = node.prev
                node.prev.next = node.next
                if all == False:
                    break
            if node.next.next is not None:
                node = node.next
            else:
                break
        l = self.len()
        DummyLinkedList.del_dummy(self, l)
            
    def insert(self, afterNode, newNode):
        node = self.head
        if afterNode is None:
            if self.len() == 0:
                self.head = newNode
                self.tail = newNode
            else:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
        
        else:
            DummyLinkedList.set_dummy(self, node)
            while node is not None:
                if node == afterNode:
                    node.next.prev = newNode
                    newNode.next = node.next
                    node.next = newNode
                    newNode.prev = node
                    l = self.len()
                    DummyLinkedList.del_dummy(self, l)
                    break
                node = node.next
        
        
    
    def len(self):
        node = self.head
        len_list = 0
        while node is not None:
            len_list += 1
            node = node.next
        return len_list
