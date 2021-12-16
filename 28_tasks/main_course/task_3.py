"""
Итан Хант с невероятным трудом пробирается в секретное хранилище данных Синдиката, 
в подводный бункер под электростанцией. На добытой им флешке хранятся детали банковских 
счетов верхушки Синдиката на сумму несколько миллиардов долларов, однако она закрыта 
"красным портфелем" -- очень сложной технологией шифрования.

Ваша миссия: реализовать алгоритм шифрования "Красного портфеля", который не под силу даже специалистам MI-6.

На вход программы подаётся строка текста, состоящая из строчных букв и пробелов. Из строки удаляются все пробелы 
и определяется её длина N.

На основании N вычисляется размер матрицы, в которую будет упакован исходный текст: из N извлекается квадратный 
корень, и его нижняя граница берётся как число строк матрицы, а верхняя граница -- как число столбцов. 
Если их произведение меньше N, увеличивайте количество строк.

Например, есть строка текста

отдай мою кроличью лапку
Она преобразуется в

отдаймоюкроличьюлапку
Длина этой строки -- 21, квадратный корень -- 4.58.
21 элемент в матрицу размером 4x5 элементов не упаковывается, значит, берём матрицу 5x5:

отдай
моюкр
оличь
юлапк
у
И наконец выдаём зашифрованный результат, выдавая символы по столбцам сверху вниз и слева направо, 
и разделяя столбцы пробелами:

омоюу толл дюиа акчп йрьк
Напишите код, зашифровывающий текстовое сообщение, и декодировщик, расшифровывающий его.

Функция

string TheRabbitsFoot(string s, bool encode)
получает исходную строку s и либо зашифровывает её (encode = true), либо расшифровывает (encode = false), 
только конечно без исходных пробелов.
"""

def TheRabbitsFoot(s, encode):
    if encode == True:
        string_without_spaces = s.replace(" ", "")
        result_str = ""
        matrix_size = len(string_without_spaces)
        number_of_lines = int(matrix_size**0.5)
        number_of_columns = number_of_lines + 1
        if number_of_lines*number_of_columns < matrix_size:
            number_of_lines += 1
        line_list = []
        matrix_list = []
        prom_list = []
        for i in range(0, matrix_size, number_of_columns):
            line_list.append(string_without_spaces[i:i+number_of_columns])

        if len(line_list[-1]) < len(line_list[0]):
            for k in range(0, number_of_columns):
                for m in range(0, number_of_lines-1):
                    prom_list.append(line_list[m][k])
                matrix_list.append(prom_list)
                prom_list = [] 
            for j in range(0, len(line_list[-1])):
                matrix_list[j].append(line_list[-1][j])           

        elif len(line_list[-1]) == len(line_list[0]):
            for k in range(0, number_of_columns):
                for m in range(0, number_of_lines):
                    prom_list.append(line_list[m][k])
                matrix_list.append(prom_list)
                prom_list = []
        for words in matrix_list:
            res = "".join(words)
            result_str += res + " "
        result_str.rstrip(" ")
            

        return result_str.rstrip(" ")
    
    else:
        string_list = s.split()
        decode_string = ""
        try:
            for k in range(0, len(string_list[0])):
                for m in range(0, len(string_list)):
                    decode_string += string_list[m][k]
        except (IndexError):
            pass
    
        return decode_string
