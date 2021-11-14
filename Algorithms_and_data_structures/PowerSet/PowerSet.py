class HashTable:
    def __init__(self, sz, stp):
        self.sizex = sz
        self.step = stp
        self.slots = [None] * self.sizex

    def hash_fun(self, value):
        return sum(value.encode('utf-8')) % self.sizex

    def seek_slot(self, value):
        index = self.hash_fun(value)
        position_count = index
        iter_count = self.sizex
        while iter_count >= 0:
            if self.slots[position_count] == None:
                return position_count
            elif self.slots[position_count] == value:
                return position_count
            else:
                position_count += self.step
                if position_count > (self.sizex-1):
                    position_count -= self.sizex
            iter_count -= 1
        # находит индекс пустого слота для значения, или None
        return None

    def put(self, value):
        if self.seek_slot(value) != None:
            self.slots[self.seek_slot(value)] = value
            return self.seek_slot(value)
        return None
         # записываем значение по хэш-функции
         
         # возвращается индекс слота или None,
         # если из-за коллизий элемент не удаётся
         # разместить 

    def find(self, value):
        find_index = self.seek_slot(value)
        if find_index !=None:
            if self.slots[find_index] == value:
                return find_index
         # находит индекс слота со значением, или None
        return None

class PowerSet(HashTable):

    def __init__(self, sz, stp):
        super(PowerSet, self).__init__(sz, stp)
        # ваша реализация хранилища

    def size(self):
        count = 0
        for i in range(0, self.sizex):
            if self.slots[i] != None:
                count += 1
        return count
        # количество элементов в множестве

    #def put(self, value):
        # всегда срабатывает

    def get(self, value):
        if value in self.slots:
            return True
        # возвращает True если value имеется в множестве,
        # иначе False
        return False

    def remove(self, value):
        if value in self.slots:
            self.slots[self.slots.index(value)] = None
            return True
        # возвращает True если value удалено
        # иначе False
        return False

    def intersection(self, set2):
        cross_set = []
        for elements in set2:
            if elements in self.slots:
                cross_set.append(elements)
        return cross_set            
        # пересечение текущего множества и set2


    def union(self, set2):
        union_set = []
        for el in self.slots:
            if el != None:
                union_set.append(el)
        for elements in set2:
            if elements not in union_set:
                union_set.append(elements)
        if len(union_set) > 0:
            return union_set
        # объединение текущего множества и set2
        return None

    def difference(self, set2):
        diff_set = []
        for elements in self.slots:
            if (elements in set2) or (elements == None):
                continue
            diff_set.append(elements)
        return diff_set
        # разница текущего множества и set2


    def issubset(self, set2):
        for elements in set2:
            if elements not in self.slots:
                return False
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        return True

    def put(self, value):
        if not self.get(value):
            return self.seek_slot(value)

