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
    midle_dict = {}

    for i in range(0, M):
        matrix.append([])
        #midle_list.append([])
        for j in range(0, N):
            matrix[i].append(Matrix[i][j])
            #midle_list[i].append(Matrix[i][j])

    for k in range(0, M//2):
        midle_dict[k] = []
    
    for l in range(0, M//2):
        b = M - l - 1
        for m in range(l, b):
            if m == l:
                for d in range(l, N-l):
                    midle_dict[l].append(matrix[m][d])
            elif m == b-1:
                for p in range(-N, 0, -1):
                    midle_dict[l].append(matrix[m][p])
            



    """
    for k in range(0, T):
        for m in range(0, M//2):
            b = M - m - 1
            for p in range(m,b+1):
                f = p - m
                if p == m:
                    midle_list[p].insert(0,matrix[p+1][0])
                    del midle_list[p][-1]
                    del midle_list[b][0]
                    midle_list[b].append(matrix[b-1][-1])
                else:

            matrix.clear()
            for l in range(0, M):
                matrix.append([])
                for o in range(0, N):
                    matrix[l].append(midle_list[l][o])


                #for q in range(m, b):
                    #midle_list[q].insert(q-1,matrix[q+1][q-1])
                    #del midle_list[q][-1-q]
                    #del midle_list[b][0]
                    #midle_list[b].append(matrix[b-1][-1])
    """


    
    return midle_dict



print(MatrixTurn(["123456", "234567", "345678", "456789"], 4, 6, 1))

#print(MatrixTurn(["111111", "000000", "1111111", "000000", "111111", "000000"], 6, 6, 1))

"""
    for m in range(0, M//2):
        b = M - m - 1

        for k in range(m, b):
            offset = k - m

            top = matrix[m][k]
            right_side = matrix[k][b]
            bottom = matrix[b][b-offset]
            left_side = matrix[b-offset][m]

            matrix[m][k] = left_side
            matrix[k][b] = top
            matrix[b][b-offset] = right_side
            matrix[b-offset][m] = bottom


            if p == m:
                    midle_list[p].insert(0+p,matrix[p+1][0])
                    del midle_list[p][-1-p]
                    del midle_list[p][0+m]
                    midle_list[p].append(matrix[p-1][-1-m])

                else:
                    del midle_list[p][0]
                    midle_list[p].insert(0,matrix[p+1][0])
                    del midle_list[p][-1]
                    midle_list[p].append(matrix[p-1][-1])
"""