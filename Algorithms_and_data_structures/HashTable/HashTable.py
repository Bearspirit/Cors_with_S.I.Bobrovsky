class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return sum(value.encode('utf-8')) % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        position_count = index
        iter_count = self.size
        while iter_count >= 0:
            if self.slots[position_count] == None:
                return position_count
            elif self.slots[position_count] == value:
                return position_count
            else:
                position_count += self.step
                if position_count > (self.size-1):
                    position_count -= self.size
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
