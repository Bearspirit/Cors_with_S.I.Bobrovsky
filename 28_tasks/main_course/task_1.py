"""
Ваш стартап получил миллионные инвестиции на создание нового поискового движка.
Требуется срочно реализовать базовый алгоритм поиска, чтобы отчитаться перед инвесторами
На вход алгоритма поступает текстовая строка достаточно большой длины. Все слова в ней разделены 
ровно одним пробелом. Алгоритм обрабатывает строку в два шага:

1) строка разбивается на набор строк через выравнивание по заданной ширине.
Разбивать строку разрешается только в местах пробелов, слова надо переносить целиком, 
если они меньше или равны длине разбивки. Например, имеется строка

1) строка разбивается на набор строк через выравнивание по заданной ширине.
и задана ширина разбивки 12.

Тогда на первом шаге будет получена такая последовательность строк:

1) строка 
разбивается
на набор
строк через
выравнивание
по заданной
ширине.
Пустые строки в такой разбивке полностью исключаются. Если ширина разбивки меньше какого-то слова, 
то это слово разбивается на несколько (с переносом на следующую строку).

2) Каждая строка проверяется на наличие в ней заданного целого слова (ограниченного либо пробелами, 
либо началом/концом строки).

Результат работы алгоритма -- последовательность целых чисел 1 или 0, которые показывают, имеется ли 
в соответствующей строке запрошенное слово.

Например, для слова "строк" результат будет таким: 0 0 0 1 0 0 0

Функция

int [] WordSearch(int len, string s, string subs) 
получает параметром len ширину выравнивания, саму строку в параметре s, и проверяемое слово в параметре subs.
Возвращает функция массив целых чисел, содержащий 1 или 0 (признаки нахождения слова в соответствующей строке).
"""
def WordSearch(alignment_lenght, s, subs):
    sequence_of_lines = ""
    lenght_of_string = 0
    for i in s.split():
        lenght_of_string += len(i)
        if lenght_of_string == alignment_lenght:
            sequence_of_lines = sequence_of_lines + i + "\n"
            lenght_of_string = 0
        elif lenght_of_string > alignment_lenght:
            if len(i) >= alignment_lenght:
                sequence_of_lines = sequence_of_lines + "\n" + i[0:alignment_lenght]
                if len(i[alignment_lenght:len(i)+1]) <= alignment_lenght:
                    sequence_of_lines = sequence_of_lines+ "\n" + i[alignment_lenght:len(i)+1]
                    lenght_of_string = len(i[alignment_lenght:len(i)+1])
                elif len(i[alignment_lenght:len(i)+1]) > alignment_lenght:
                    m = 0
                    n = len(i[alignment_lenght:len(i)+1])
                    k = 2*alignment_lenght
                    while n > 0:
                        sequence_of_lines = sequence_of_lines + "\n" + i[m+alignment_lenght:k]
                        lenght_of_string = len(i[m+alignment_lenght:k])
                        m = m + alignment_lenght
                        k = k + alignment_lenght
                        n = n - alignment_lenght

            elif len(i) < alignment_lenght:
                sequence_of_lines = sequence_of_lines + "\n" + i + " "
                lenght_of_string = len(i) + 1
        else:
            sequence_of_lines = sequence_of_lines + i + " "
            lenght_of_string += 1
        if lenght_of_string > alignment_lenght:
            lenght_of_string = 0
            
    converted_list = sequence_of_lines.split("\n")
    for line in converted_list:
        if len(line) == 0:
            converted_list.remove(line)
    searching_word_list = []
    for words in converted_list:
        k = 0
        for word in words.split():
            if word == subs:
                k += 1
        if k > 0:
            searching_word_list.append(1)
        else:
            searching_word_list.append(0)

                       
    return searching_word_list
