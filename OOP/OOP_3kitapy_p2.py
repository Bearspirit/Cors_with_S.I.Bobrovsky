"""Наглядный пример принципа полиморфизма. Заносим в список объекты разных подклассов и вызываем
переопределнный в подклассах метод.
"""

import random

class Cinema:
    def __init__(self, time=150):
        self.time = time

    def get_time(self):
        print("Средняя длительность картины составляет " + str(self.time) + " минут.")
       

class Movie(Cinema):
    def __init__(self, time=90):
        super().__init__(self)
        self.time = time

    def get_time(self):
        print("Средняя длительность фильма составляет " + str(self.time) + " минут.")


class Serial(Cinema):
    def __init__(self, time=20):
        super().__init__(self)
        self.time = time

    def get_time(self):
        print("Средняя длительность сериала составляет " + str(self.time) + " минут.")

cin_list = []

for i in range(10):
    if random.randint(1, 2) == 1:
        mov = Movie()
    else:
        mov = Serial()
    cin_list.append(mov)

for j in cin_list:
    j.get_time()



#полученный вывод показывает нам, что, согласно принципам полиморфизма, если метод родительского класса
#был переопредел в дочернем, то вызываться будет переопределенный метод
