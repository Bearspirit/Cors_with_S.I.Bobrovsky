"""Функция
int ConquestCampaign(int N, int M, int L, int [] battalion)

получает первыми двумя параметрами размер Государства Квадратов NxM, 
а battalion содержит массив из L*2 целых чисел (L >= 1) с индексацией с нуля, 
в котором каждый чётный (с чётным индексом) элемент содержит очередную координату 
области высадки по первому измерению N, а каждый нечётный (с нечётным индексом) элемент 
содержит очередную координату области высадки по второму измерению M.
Не исключено, что в связи с неразберихой в командовании координаты областей высадки могут дублироваться.
На примере с картинки параметры будут такими: N = 3, M = 4, L = 2, battalion = [2,2, 3,4]

Возвращает функция день, начиная с 1, когда все области будут взяты под контроль.
"""
def ConquestCampaign(N, M, L, battalion):
    square_coord = []
    attack_coord =[]
    day = 1
    for x in range(1, N+1):
        for y in range(1, M+1):
            square_coord.append((x,y))
    for n in range(0, len(battalion), 2):
        attack_coord.append((battalion[n], battalion[n+1]))
              
    if set(square_coord).issubset(attack_coord):
        return day
    else:
        while True:
            for m in range(0, len(attack_coord)):
                if attack_coord[m][0]+1 <= N:
                    attack_coord.append((attack_coord[m][0]+1, attack_coord[m][1]))
                if attack_coord[m][0]-1 != 0:
                    attack_coord.append((attack_coord[m][0]-1, attack_coord[m][1]))
                if attack_coord[m][1]+1 <= M:
                    attack_coord.append((attack_coord[m][0], attack_coord[m][1]+1))
                if attack_coord[m][1]-1 != 0:
                    attack_coord.append((attack_coord[m][0], attack_coord[m][1]-1))
            day += 1
            if set(square_coord).issubset(attack_coord):
                return day

