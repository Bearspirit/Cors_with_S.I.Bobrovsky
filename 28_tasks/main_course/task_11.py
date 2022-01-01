"""
Олег получил инвестиции на стартап по машинному обучению, и занимается распознаванием закономерностей в тексте.

Его первый продукт будет анализировать текст, преобразованный из изображений точек и звёздочек, которые рисуют 
первоклассники в тетрадках. Последовательности всегда составлены по общему шаблону, но первоклассники пока часто 
ошибаются, и забывают поставить точку, рисуют лишнюю звёздочку, и т. п.

На вход программы поступают строки, состоящие из символов "." и "*", всегда начинающиеся и завершающиеся звёздочкой. 
В них всегда повторяется единый шаблон, например:

*..*..*..*..*..*..*
Такой пример считается корректным.

Однако первоклассники иногда ошибаются, и могут написать такие ошибочные строки:

*..*...*..*..*..*..*
*..*..*..*..*..**..*
Ещё примеры корректных строк:

*
***
*.......*.......*
**
*.*
Функция

bool LineAnalysis(string line)
получает на вход строку для анализа и возвращает логическое true/false, обозначающее корректность строки.
"""
def LineAnalysis(line):
    STAR = "*"
    SPACE = ""
    string_for_analys = line.lstrip(STAR)
    string_for_analys = string_for_analys.rstrip(STAR)
    line_list = string_for_analys.split(STAR)
    string_for_analys = '***ERROR***'

    ELEMENTS_LIST_LENGTH = len(line_list)
    ORIGINAL_STRING_LENGTH = len(line)
    FIRST_ELEMENT_LENGTH = len(line_list[0])

    is_first_not_star = line[0] != STAR
    is_last_not_star = line[-1] != STAR

    if is_first_not_star or is_last_not_star:
        return False
    
    elif (ELEMENTS_LIST_LENGTH == 1) and ((ORIGINAL_STRING_LENGTH- FIRST_ELEMENT_LENGTH)%2 != 0) and (ORIGINAL_STRING_LENGTH > 3):
        return False
    elif (ELEMENTS_LIST_LENGTH == 1) and (FIRST_ELEMENT_LENGTH == SPACE):
        return True
    else:
        count = 0
        empty_count = 0
        for el in line_list:
            if el == line_list[0]:
                count += 1
            if el == SPACE:
                empty_count += 1
        if count == ELEMENTS_LIST_LENGTH:
            return True
        else:
            return False
