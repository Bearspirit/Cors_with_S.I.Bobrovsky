import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.__array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.__array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.__array[i]
        self.__array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.__array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i != self.count:
            self.__getitem__(i)
        if self.count + 1 > self.capacity:
            new_capacity = (2 * self.capacity)
            self.resize(new_capacity)
        new_array = self.make_array(self.capacity)
        new_count = 0
        for k in range(self.count+1):
            if i == k:
                new_array[k] = itm
                continue
            new_array[k] = self.__array[new_count]
            new_count += 1
        self.__array = new_array
        self.count += 1

    def delete(self, i):
        self.__getitem__(i)
        new_array = self.make_array(self.capacity)
        count = 0
        for j in range(self.count):
            if j == i: 
                continue
            new_array[count] = self.__array[j]
            count += 1
        self.__array = new_array
        self.count -= 1
        if self.count < self.capacity // 2:
            if int(self.capacity / 1.5) <= 16:
                new_capacity = 16
            else:
                new_capacity = int(self.capacity / 1.5)
            self.resize(new_capacity)