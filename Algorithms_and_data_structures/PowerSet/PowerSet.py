class PowerSet():

    def __init__(self):
        self.__slots = []
        # ваша реализация хранилища

    def size(self):
        return len(self.__slots)
        # количество элементов в множестве

    def put(self, value):
        if value not in self.__slots:
            self.__slots.append(value)
        # всегда срабатывает

    def get(self, value):
        if value in self.__slots:
            return True
        # возвращает True если value имеется в множестве,
        # иначе False
        return False

    def remove(self, value):
        if value in self.__slots:
            self.__slots.pop(self.__slots.index(value))
            return True
        # возвращает True если value удалено
        # иначе False
        return False

    def intersection(self, set2):
        cross_set = PowerSet()
        for element in self.__slots:
            if set2.get(element):
                cross_set.put(element)
        return cross_set            
        # пересечение текущего множества и set2


    def union(self, set2):
        union_set = PowerSet()
        union_set.__slots = self.__slots.copy()
        for element in set2.__slots:
            union_set.put(element)
    
        return union_set
        # объединение текущего множества и set2

    def difference(self, set2):
        diff_set = PowerSet()
        diff_set.slots = self.__slots.copy()
        for element in set2.__slots:
            diff_set.remove(element)
        return diff_set
        # разница текущего множества и set2


    def issubset(self, set2):
        for elements in set2.__slots:
            if self.get(elements) == False:
                return False
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        return True

