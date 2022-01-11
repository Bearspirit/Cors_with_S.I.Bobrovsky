"""
Сама суть этой загадки и то возбужденное состояние, в котором пребывал клиент Холмса, 
придавали этому делу необычный характер. Да и, кроме предстоящего расследования, мастерство моего друга, 
его умение удивительно быстро овладевать ситуацией и на основании тщательных наблюдений и простой логики 
делать поразительные по своей точности выводы зачаровывали меня. Изучать систему его работы и приемы, 
с помощью которых он в два счета распутывал сложнейшие загадки, для меня было настоящим удовольствием.


Шерлок Холмс в свободное время упражняется в проверке валидных паролей к его новой механической шкатулке. 
Пароли строятся из латинских букв и считаются валидными, если в соответствующей строке пароля все буквы 
встречаются одинаковое количество раз. Кроме того, разрешается удалить одну любую букву, чтобы выполнилось 
условие равенства частоты всех букв.

Например, строка xyz будет валидна, и строка xyzaa будет валидна (можно удалить одну a), и строка xxyyz 
будет валидна (можно удалить z). А строка xyzzz, или строка xxyyza или строка xxyyzabc невалидны.

Напишите функцию, проверяющую строку на валидность.

Функция

boolean SherlockValidString(string s)
получает на вход исходную строку длиной 2 или более английских букв, и возвращает true, если строка валидна.
"""

def SherlockValidString(der_parol):
    main_list = []
    midle_list = []
    
    for i in range(0, len(der_parol)):
        main_list.append(der_parol[i])
    elements_set = set(main_list)

    midle_dict = {}
    for symbol in elements_set:
        midle_dict[symbol] = main_list.count(symbol)
    for value in midle_dict.values():
        midle_list.append(value)

    ONE = 1
    if ONE in midle_list: 
        if midle_list.count(1) == 1:
            midle_list.remove(1) #если буква встречается единожды, мы можем ее исключить, чтобы она не мешала проверять строку на валидность 
    result_set = set(midle_list)

    result_list = []
    if len(result_set) == 1:
        return True
    elif len(result_set) > 2:
        return False
    for sym in result_set:
        result_list.append(midle_list.count(sym))
    
    if ONE not in result_list:
        return False
    else:
        if abs(midle_list[0]-midle_list[1]) == 1:
            return True
        else:
            for el in result_set:
                if midle_list.count(el) == 1:
                    midle_list.remove(el)
                    if (el-1) == midle_list[0]:
                        return True    
                    else:
                        return False 
