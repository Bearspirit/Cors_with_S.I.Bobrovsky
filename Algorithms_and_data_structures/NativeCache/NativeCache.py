class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.__hits = [0] * self.size

    def hash_fun(self, key):
        return sum(key.encode('utf-8')) % self.size
        # в качестве key поступают строки!
        # всегда возвращает корректный индекс слота

    def is_key(self, key):
        # возвращает True если ключ имеется,
        # иначе False
        return key in self.slots

    def put(self, key, value):
        if self.is_key(key):
            self.values[self.slots.index(key)] = value
            self.__hits[self.slots.index(key)] += 1 #увеличиваем количество обращений к ключу
        else:
            index = self.hash_fun(key)
            position_count = index
            iter_count = self.size
            step = 3
            while iter_count >= 0:
                if self.slots[position_count] == None:
                    self.slots[position_count] = key
                    self.values[position_count] = value
                    self.__hits[position_count] = 0
                    break
                position_count += step
                if position_count > (self.size-1):
                    position_count -= self.size
                iter_count -= 1
        if key not in self.slots:
            if min(self.__hits) != (sum(self.__hits)/len(self.__hits)):
                self.slots[self.__hits.index(min(self.__hits))] = key
                self.values[self.__hits.index(min(self.__hits))] = value
                self.__hits[self.__hits.index(min(self.__hits))] = 0
        # гарантированно записываем 
        # значение value по ключу key

    def get(self, key):
        if self.is_key(key):
            self.__hits[self.slots.index(key)] += 1 #добавляем новое обращение к ключу
            return self.values[self.slots.index(key)]
        # возвращает value для key, 
        # или None если ключ не найден
        return None