"""
Задание.
Пункты, помеченные * реализуйте отдельно.

1.1. Добавьте в класс LinkedList метод удаления одного узла по его значению
delete(val, all=False)

где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.
1.2. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).

1.3. Добавьте в класс LinkedList метод очистки всего содержимого (создание пустого списка) -- clean()

1.4. Добавьте в класс LinkedList метод поиска всех узлов по конкретному значению (возвращается стандартный 
питоновский список найденных узлов).

find_all(val)
1.5. Добавьте в класс LinkedList метод вычисления текущей длины списка -- len()

1.6. Добавьте в класс LinkedList метод вставки узла newNode после заданного узла afterNode (из списка)
insert(afterNode, newNode)

Если afterNode = None, добавьте новый элемент первым в списке.
* 1.7. Напишите проверочные тесты для каждого из предыдущих заданий.

* 1.8. Напишите функцию, которая получает на вход два связанных списка, состоящие из целых значений, и если 
их длины равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков.

Рекомендации по тестированию.
Проверяйте случаи, когда список пустой, содержит много элементов и один элемент: как в таких ситуациях будет 
работать удаление одного и нескольких элементов, вставка, поиск. Особое внимание уделите корректности полей 
head и tail после всех этих операций.
"""


class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        find_list = []
        while node is not None:
            if node.value == val:
                find_list.append(node)
            node = node.next
        return find_list

    def delete(self, val, all=False):
        node = self.head
        prev_node = None
        while node is not None:
            if node.value == val:
                if prev_node == None:
                    self.head = node.next                                
                else:
                    prev_node.next = node.next
                if self.tail == node:
                    self.tail = prev_node
                if all == False:
                    break    
            else:
                prev_node = node
            node = node.next
               
    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        list_len = 0
        node = self.head
        while node is not None:
            list_len += 1
            node = node.next
        return list_len

    def insert(self, afterNode, newNode):
        node = self.head
        nx_node = node.next
        if afterNode == None:
            self.head = newNode
            self.head.next = node
        else:
            while node is not None:
                if node == afterNode:
                    if nx_node is None:
                        self.tail.next = newNode
                        self.tail = newNode
                    else:
                        node.next = newNode
                        newNode.next = nx_node
                    break
            
                node = node.next            
                if (nx_node == self.tail) or (nx_node == None): 
                    nx_node = None
                else:
                    nx_node = node.next


