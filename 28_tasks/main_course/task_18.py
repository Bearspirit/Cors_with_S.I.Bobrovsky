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
        midle_list.append([])
        for j in range(0, N):
            matrix[i].append(Matrix[i][j])
            midle_list[i].append(Matrix[i][j])

    for k in range(0, T):
        l = -1
        for m in range(0, M//2):
            b = M - m - 1
            midle_list[m].insert(0,matrix[m+1][0])
            del midle_list[m][-1]
            del midle_list[b][0]
            midle_list[b].append(matrix[b-1][-1])
            


            

    """
    size = len(matrix)
    layer_count = size / 2

    for layer in range(0, int(layer_count)):
        first = layer
        last = size - first - 1

        for element in range(first, last):
            offset = element - first

            top = matrix[first][element]
            right_side = matrix[element][last]
            bottom = matrix[last][last-offset]
            left_side = matrix[last-offset][first]

            matrix[first][element] = left_side
            matrix[element][last] = top
            matrix[last][last-offset] = right_side
            matrix[last-offset][first] = bottom

    """
    
    return midle_list



print(MatrixTurn(["123456", "234567", "345678", "456789"], 4, 6, 1))