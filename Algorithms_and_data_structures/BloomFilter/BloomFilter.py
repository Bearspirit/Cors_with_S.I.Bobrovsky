class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.__bitarr_filter = 0
        # создаём битовый массив длиной f_len ...


    def hash1(self, str1):
        random_num = 17
        result = 0
        for c in str1:
            code = ord(c)
            result = (result*random_num + code) % self.filter_len
        return result
        # реализация ...

    def hash2(self, str1):
        random_num = 223
        result = 0
        for c in str1:
            code = ord(c)
            result = (result*random_num + code) % self.filter_len
        return result
        # 223 
        # ...

    def add(self, str1):
        self.__bitarr_filter = self.__bitarr_filter | self.hash1(str1) | self.hash2(str1)
        # добавляем строку str1 в фильтр

    def is_value(self, str1):
        test_mask = self.hash1(str1) | self.hash2(str1)
        return ((self.__bitarr_filter & test_mask) == test_mask)
        # проверка, имеется ли строка str1 в фильтре
