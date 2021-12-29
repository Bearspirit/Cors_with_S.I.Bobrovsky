"""
Белые Ходоки снова готовят свою армию мертвецов для очередного штурма Стены. Но они подкрадываются к ней хитростью, 
стараясь незаметно затесаться среди мирных жителей окрестных деревень.
Для этого Ходоки принимают обличье крестьян, однако становятся различимыми, когда группируются в тройки -- температура 
вокруг них при этом понижается на 10 градусов.
Вы возглавляете Железный Трон Семи Королевств и посылаете разведчиков выявить всех врагов.

Дайте им подробные инструкции по определению вражеских сил в каждой деревне.

Каждая деревня задаётся ASCII-строкой (возможно, пустой).

В ней могут быть числа (жители, разбредшиется по полям), но только из одного символа (цифры от 0 до 9). 
То есть подряд несколько цифр не могут следовать.

Если в такой строке между каждой парой чисел (цифр), сумма которых равна 10, насчитываются ровно три Ходока (символ "="), 
значит, Ходоки успешно выявлены.

Функция

bool white_walkers(string village) 
получает параметром village строку, описывающую одну деревню, и возвращает true, если в ней выявляются все Ходоки.
Например:

"axxb6===4xaf5===eee5" => true
"5==ooooooo=5=5" => false
"abc=7==hdjs=3gg1=======5" => true
"aaS=8" => false
"9===1===9===1===9" => true
"""

def white_walkers(village):
    village_information_list = []
    WHITE_WALKER = '='
    for i in range(0, len(village)):
        if village[i].isdigit() == True:
            village_information_list.append(int(village[i]))
        elif village[i] == WHITE_WALKER:
            village_information_list.append(village[i])
    k = 0
    b = 0
    for j in range(0, len(village_information_list)-4):
        if type(village_information_list[j]) == int:
            k += village_information_list[j]
            if type(village_information_list[j+4]) == int:
                k += village_information_list[j+4]
                if k == 10:
                    b += 1
            k = 0
    midle_list = []
    num_of_couple = 0
    for q in range(0, len(village_information_list)):
        if type(village_information_list[q]) == int:
            midle_list.append(village_information_list[q])
    for p in range(0, len(midle_list)-1):
        if (midle_list[p] + midle_list[p+1]) == 10:
            num_of_couple += 1
    
    if (b == num_of_couple) and b != 0:
        return True
    else:
        return False    


