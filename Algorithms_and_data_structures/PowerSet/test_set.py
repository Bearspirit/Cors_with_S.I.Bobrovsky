class PowerSet():

    def __init__(self):
        self.slots = []
        # ваша реализация хранилища

    def size(self):
        return len(self.slots)
        # количество элементов в множестве

    def put(self, value):
        if value not in self.slots:
            self.slots.append(value)
        # всегда срабатывает

    def get(self, value):
        if value in self.slots:
            return True
        # возвращает True если value имеется в множестве,
        # иначе False
        return False

    def remove(self, value):
        if value in self.slots:
            self.slots.pop(self.slots.index(value))
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

