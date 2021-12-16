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
    size_of_squares_state = []
    occupied_territory =[]
    num_days_of_capture = 1
    for x in range(1, N+1):
        for y in range(1, M+1):
            size_of_squares_state.append((x,y))
    for n in range(0, len(battalion), 2):
        occupied_territory.append((battalion[n], battalion[n+1]))
              
    if set(size_of_squares_state).issubset(occupied_territory):
        return num_days_of_capture
    else:
        while True:
            for m in range(0, len(occupied_territory)):
                if occupied_territory[m][0]+1 <= N:
                    occupied_territory.append((occupied_territory[m][0]+1, occupied_territory[m][1]))
                if occupied_territory[m][0]-1 != 0:
                    occupied_territory.append((occupied_territory[m][0]-1, occupied_territory[m][1]))
                if occupied_territory[m][1]+1 <= M:
                    occupied_territory.append((occupied_territory[m][0], occupied_territory[m][1]+1))
                if occupied_territory[m][1]-1 != 0:
                    occupied_territory.append((occupied_territory[m][0], occupied_territory[m][1]-1))
            num_days_of_capture += 1
            if set(size_of_squares_state).issubset(occupied_territory):
                return num_days_of_capture

