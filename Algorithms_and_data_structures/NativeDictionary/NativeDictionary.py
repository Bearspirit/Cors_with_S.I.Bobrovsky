class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        return sum(key.encode('utf-8')) % self.size
        # в качестве key поступают строки!
        # всегда возвращает корректный индекс слота

    def is_key(self, key):
        if key in self.slots:
            return True
        # возвращает True если ключ имеется,
        # иначе False
        return False

    def put(self, key, value):
        if self.is_key(key):
            self.values[self.slots.index(key)] = value
        else:
            index = self.hash_fun(key)
            position_count = index
            iter_count = self.size
            step = 3
            while iter_count >= 0:
                if self.slots[position_count] == None:
                    self.slots[position_count] = key
                    self.values[position_count] = value
                elif self.slots[position_count] == key:
                    self.values[position_count] = value
                else:
                    position_count += step
                    if position_count > (self.size-1):
                        position_count -= self.size
                iter_count -= 1

        # гарантированно записываем 
        # значение value по ключу key

    def get(self, key):
        if self.is_key(key):
            return self.values[self.slots.index(key)]
        # возвращает value для key, 
        # или None если ключ не найден
        return None