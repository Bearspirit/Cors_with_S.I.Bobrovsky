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
def WordSearch(num, s, subs):
    text = ""
    result = []
    word_len = 0
    for i in s.split():
        word_len += len(i)
        if word_len == num:
            text = text + i + "\n"
            word_len = 0
        elif word_len > num:
            if len(i) >= num:
                text = text + "\n" + i[0:num]
                if len(i[num:len(i)+1]) <= num:
                    text = text+ "\n" + i[num:len(i)+1]
                    word_len = len(i[num:len(i)+1])
                elif len(i[num:len(i)+1]) > num:
                    m = 0
                    n = len(i[num:len(i)+1])
                    k = 2*num
                    while n > 0:
                        text = text + "\n" + i[m+num:k]
                        word_len = len(i[m+num:k])
                        m = m + num
                        k = k + num
                        n = n - num

            elif len(i) < num:
                text = text + "\n" + i + " "
                word_len = len(i) + 1
        else:
            text = text + i + " "
            word_len += 1
        if word_len > num:
            word_len = 0
            
    st_list = text.split("\n")

    for line in st_list:
        if len(line) == 0:
            st_list.remove(line)
    for words in st_list:
        k = 0
        for word in words.split():
            if word == subs:
                k += 1
        if k > 0:
            result.append(1)
        else:
            result.append(0)

                       
    return result
