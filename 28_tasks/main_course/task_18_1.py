"""
К сожалению, никто не может объяснить, что такое Матрица.
Ты должен сам увидеть это.
На вход поступает Матрица размером MxN:
1 2 3 4 5 6 
2 3 4 5 6 7
3 4 5 6 7 8
4 5 6 7 8 9
Ты должен научиться вращать Матрицу относительно её центра по часовой стрелке.
Например, вращение на один шаг:
2 1 2 3 4 5 
3 4 3 4 5 6
4 5 6 7 6 7
5 6 7 8 9 8
Функция
void MatrixTurn(string Matrix[], int M, int N, int T)
получает на вход (по ссылке) массив строк (M строк, каждая длиной N; M >= 2, N >= 2), и вращает его 
относительно центра по часовой стрелке на T шагов (T >= 1), как описано выше.
То есть результат поворота (повёрнутая матрица) оказывается в исходном массиве Matrix, переданном в 
функцию по ссылке как аргумент.
Минимальное значение из чисел M,N обязательно чётно.
Пример вызова:
MatrixTurn(["123456", "234567", "345678", "456789"], 4,6, 3)
"""

def MatrixTurn(Matrix, M, N, T):
    matrix = []
    midle_list = []
    for i in range(0, M):
        matrix.append([])
        for j in range(0, N):
            matrix[i].append(Matrix[i][j])
            
    
    if not len(matrix):
        return

    """
        top : индекс начальной строки
        bottom : индекс конечной строки
        left : индекс начального столбца
        right : индекс конечного столбца
    """



    for k in range(0, T):
        top = 0
        bottom = len(matrix)-1

        left = 0
        right = len(matrix[0])-1


        while left < right and top < bottom:

            # Обозначаем первый элемент следующей строки,
            # который должен заменить первый элемент текущей строки
            prev = matrix[top+1][left]

            # Перемещаем элемент верхнего ряда на один шаг вправо
            for i in range(left, right+1):
                curr = matrix[top][i]
                matrix[top][i] = prev
                prev = curr

            top += 1

            # Перемещаем элемент крайнего правого ряда на один шаг вниз
            for i in range(top, bottom+1):
                curr = matrix[i][right]
                matrix[i][right] = prev
                prev = curr

            right -= 1

            # Перемещаем элемент нижнего ряда на один шаг влево
            for i in range(right, left-1, -1):
                curr = matrix[bottom][i]
                matrix[bottom][i] = prev
                prev = curr

            bottom -= 1

            # Перемещаем один элемент кайнего левого ряда на один элемент вверх
            for i in range(bottom, top-1, -1):
                curr = matrix[i][left]
                matrix[i][left] = prev
                prev = curr

            left += 1

    for j in range(0, M):
        midle_list.append(''.join(matrix[j]))

    return midle_list
