"""
В рамках проекта тотального импортозамещения решено полностью с нуля переписать весь офисный софт в стране. 
Вы получили подряд с бюджетом миллион рублей по созданию оригинального текстового редактора "Лапоть". 
Закодируйте его максимально компактно!
"Лапоть" поддерживает пять операций:
1. Добавить(S) -- в конец текущей строки (исходно пустая) добавляется строка S;
2. Удалить(N) -- удалить N символов из конца текущей строки. Если N больше длины текущей строки, удаляем из неё все символы;
3. Выдать(i) -- выдать i-й символ текущей строки (индексация начинается с нуля) в формате строки (строковый тип). 
Если индекс за пределами строки, возвращайте пустую строку;
4. Undo() -- отмена последней операции 1 или 2; отмена должна уметь выполняться при необходимости неограниченное число раз;
5. Redo() -- выполнить заново последнюю отменённую с помощью Undo операцию; Redo должна уметь выполняться 
при необходимости неограниченное число раз.
Если после Undo выполняется операция 1 или 2, то
-- предыдущая цепочка операций для Undo обнуляется (откатить можно только последнюю операцию 1 или 2);
-- Redo более становится нечего откатывать.
На вход редактора подаётся одна строка, первый символ которой -- номер операции (1-5) и через пробел, 
при необходимости, параметр соответствующей операции.
Например:
1 Привет 
В текущей строке будет "Привет"
1  , Мир!
Привет, Мир!
1 ++ 
Привет, Мир!++
2 2
Привет, Мир!
4
Привет, Мир!++
4
Привет, Мир!
1 *
Привет, Мир!*
4
Привет, Мир!
4 
Привет, Мир!
4
Привет, Мир!
3 6
,
2 100

1 Привет 
Привет
1  , Мир!
Привет, Мир!
1 ++ 
Привет, Мир!++
4
Привет, Мир!
4
Привет
5
Привет, Мир!
4
Привет
5
Привет, Мир!
5
Привет, Мир!++
5
Привет, Мир!++
5
Привет, Мир!++
4
Привет, Мир!
4
Привет
2 2
Прив
4
Привет
5
Прив
5
Прив
5
Прив
Функция
string BastShoe(string command)          
получает на вход строку в формате "N параметр", где N -- код операции (1-5), и возвращает текущую строку, или символ 
в формате строки, если команда Выдать(), или пустую строку в случае её ошибки.
Например, BastShoe("1 Привет") = "Привет"
Если команда задана некорректно, Лапоть ничего не делает (просто возвращает текущую строку без изменений).
"""
string_list = []
deleted_elements = []
count_undo = 0
def BastShoe(command):
    global count_undo
    command_list = command.split(" ", maxsplit=1)

    if command_list[0] == "1": 
        if len(deleted_elements) > 0:
            deleted_elements.clear()
            del string_list[:-1]
            count_undo = 1
        elif len(deleted_elements) == 0:
            count_undo = 0
        if len(string_list) == 0:
            string_list.append(command_list[1])
            return string_list[0]
        else:
            string_list.append(string_list[-1] + command_list[1])
        return string_list[len(string_list)-1]

    elif command_list[0] == "2":
        if len(deleted_elements) > 0:
            deleted_elements.clear()
            del string_list[:-1]
            count_undo = 1
        elif len(deleted_elements) == 0:
            count_undo = 0
        if len(string_list) == 0:
            return ""
        elif len(string_list[-1]) >= int(command_list[1]):
            string_list.append(string_list[-1][:-int(command_list[1])])
            return string_list[-1]
        else:
            string_list.append("")
            return string_list[-1]


    elif command_list[0] == "3":
        try:
            return string_list[-1][int(command_list[1])]
        except IndexError:
            return ""

    elif command_list[0] == "4":
        if count_undo == 1:
            if len(deleted_elements) == 0:
                if len(string_list) > 1:
                    deleted_elements.append(string_list[-1])
                    del string_list[-1]
                    return string_list[-1]
                elif len(string_list) == 1:
                    deleted_elements.append(string_list[0])
                    del string_list[0]
                    return ""
                else:
                    return ""
            else:
                if len(string_list) > 0:
                    return string_list[-1]
                else:
                    return ""
        elif len(string_list) > 0:
            deleted_elements.append(string_list[-1])
            del string_list[-1]
            if len(string_list) == 0:
                return ""
            else:
                return string_list[-1]
        else: #len(string_list) == 0:
            return ""

    elif command_list[0] == "5":
        if len(deleted_elements) == 0:
            return string_list[-1]
        elif len(deleted_elements) > 0:
            string_list.append(deleted_elements[-1])
            del deleted_elements[-1]
            return string_list[-1]

    else:
        if len(string_list) > 0:
            return string_list[-1]
        else:
            return ""