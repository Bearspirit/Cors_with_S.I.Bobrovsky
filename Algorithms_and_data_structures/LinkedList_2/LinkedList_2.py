"""
Задания.
2.1. Добавьте в класс LinkedList2 метод поиска первого узла по его значению.
find(val)
2.2. Добавьте в класс LinkedList2 метод поиска всех узлов по конкретному значению 
(возвращается список найденных узлов).

find_all(val)
2.3. Добавьте в класс LinkedList2 метод удаления одного узла по его значению.
delete(val, all=False)
где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.

2.4. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).

2.5. Добавьте в класс LinkedList2 метод вставки узла после заданного узла.
insert(afterNode, newNode)
Если afterNode = None и список пустой, добавьте новый элемент первым в списке.
Если afterNode = None и список непустой, добавьте новый элемент последним в списке.

2.6. Добавьте в класс LinkedList2 метод вставки узла самым первым элементом.
add_in_head(newNode)
2.7. Добавьте в класс LinkedList2 метод очистки всего содержимого (создание пустого списка) -- clean()

2.8. Добавьте в класс LinkedList2 метод вычисления текущей длины списка -- len()

2.9. Напишите проверочные тесты для каждого из предыдущих заданий.

* 2.10. Существует интересный финт, обсуждаемый на курсе Стэнфордского университета CS106B -- фиктивный/пустой 
(dummy) узел. Пока нам при любых модификациях списка (добавление/удаление узла) приходится рассматривать три 
отдельные ситуации: работа с серединой списка, с его головой и с его хвостом. Фиктивный узел позволяет избавиться 
от этих краевых ситуаций, оставив только по одной универсальной операции на добавление и удаление. Идея в том, 
что мы добавляем в список два искусственных узла -- голову и хвост, которые пользователю класса не видны 
(они отличаются от видимых узлов, например, булевым флажком, а лучше всего это делать через наследование и 
перегрузку). Теперь, добавляя или удаляя узлы, мы всегда будем уверены, что у каждого из них имеется и 
предыдущий узел, и последующий, и от дополнительных проверок и модификаций полей head и tail можно избавиться.
В реализации для тестов на сервере такую схему применять не надо, сделайте отдельную реализацию, бонус до +500.
"""

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None 

    def find_all(self, val):
        find_list = []
        node = self.head
        while node is not None:
            if node.value == val:
                find_list.append(node)
            node = node.next
        return find_list

    def delete(self, val, all=False):
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
                if all == False:
                    break
            node = node.next


    def clean(self):
        self.head = None
        self.tail = None
        

    def len(self):
        node = self.head
        len_list = 0
        while node is not None:
            len_list += 1
            node = node.next
        return len_list

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
            while node is not None:
                if node == afterNode:
                    if self.head is node:
                        newNode.next = self.head.next   
                        newNode.prev = self.head                     
                        self.head.next = newNode
                        if self.len() == 2:
                            self.tail = newNode
                    elif self.tail is node:
                        self.tail.next = newNode
                        newNode.prev = self.tail
                        self.tail = newNode
                    else:
                        node.next.prev = newNode
                        newNode.next = node.next
                        node.next = newNode
                        newNode.prev = node

                    break
                node = node.next


    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
