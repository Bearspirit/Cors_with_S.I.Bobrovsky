"""
Танковый раш
Разведчики выяснили, что неведомый клан готовит внезапный массивный прорыв премиум-танков. 
У нашей арты будет возможность произвести только один залп. Ваша задача: выявить местонахождение группировки танков на карте.


На входе два массива (карта и группировка танков), каждый описывается одинаково: количество строк, 
количество столбцов и набор строк, разделённых пробелом. Каждый символ строки описывает один элемент карты.

Например, дана карта:

1234
2345
0987
Этот массив размером 3*4 будет представлен на вводе так:

3 4 1234 2345 0987
Второй массив представляется аналогично первому.

Задача: проверить, входит ли второй массив в первый (в двумерном виде).

Например, второй массив может быть таким:

34
98
или

2 2 34 98
Он входит в состав первого массива.

Функция

bool TankRush(int H1, int W1, string S1, int H2, intW2, string S2) 
первыми тремя параметрами получает исходную карту, а следующими тремя -- карту, которая ищется в исходной.
TankRush возвращает true, если вторая карта содержится в первой.
"""

def TankRush(H1, W1, S1, H2, W2, S2):
    map_1 = S1.split()
    map_2 = S2.split()
    index = []
    for i in range(len(map_2)):
        for j in range(len(map_1)):
            try:
                if (map_2[i] in map_1[j]) and (map_2[i+1] in map_1[j+1]):
                    index.append(map_1[j])
                    index.append(map_1[j+1])
            except IndexError:
                continue
    if len(index) == 0:
        return False
    first_count = []
    second_count = []
    index = index[-len(map_2):]
    for k in range(len(index)):
        if index[k].count(map_2[k]) == 1:
            first_count.append(index[k].index(map_2[k]))
        else:
            for m in range(0, len(index[k])):
                try:
                    if index[k][m:m+len(map_2[k])] == map_2[k]:
                        second_count.append(m)
                except IndexError:
                    continue
    if len(second_count) == 0:
        if len(set(first_count)) == 1:
            return True
        else:
            return False
    elif len(second_count) > 0:
        if len(first_count) == 0:
            if len(set(second_count)) == 1:
                return True
            else:
                return False
        else:
            for dig in second_count:
                if dig in first_count:
                    return True
            return False  
