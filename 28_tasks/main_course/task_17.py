"""
Только в Изумрудном Сне существует Древо Жизни Андрассил. Племена фурболгов, живущие в гигантском пне Нордскола, 
из поколения в поколение передают легенду об этом дереве, которое когда-нибудь вернётся в реальность и очистит 
мирные земли от порчи Древних Богов.

Главный шаман фурболгов хранит манускрипт, описывающий схему развития Андрассила. Смоделируйте её на компьютере, 
чтобы всегда можно было узнать, на каком году в каком состоянии оно будет находиться.


Дерево описывается массивом размером HxW. Каждый элемент массива принимает значение либо 0 (пусто), либо 1 
(ветка дерева). При этом у каждого элемента-ветки имеется дополнительная характеристика, равная сроку её жизни в годах.

Исходные данные: размер массива, количество лет для моделирования, и начальная структура дерева в виде текстового 
изображения (списка текстовых строк).

Например, размер 3x4, моделируем 12 лет, каждый пустой элемент задаётся символом ".", каждая ветка -- символом "+" 
(её возраст считается равным 1 году):

3 4 12

.+..
..+.
.+..
Каждый год дерево перерождается по следующему алгоритму:
- в "первый" (чётный) год все ветки стареют на один год, и все пустые клетки заполняются новыми корнями с возрастом 
1 год (визуально всё заполнено символами "+");
- во "второй" (нечётный) год все ветки стареют на один год; ветки, возраст которых три или более лет, погибают, 
уничтожая также четыре окружающие ветки (если они существуют) -- по горизонтали и вертикали.

Процесс гибели веток с соседями происходит одновременно, т.е. надо учитывать, что каждая ветка с возрастом 3+ лет 
обязательно уничтожает окружающие ветки (нельзя удалять ветки-соседи простым перебором, потому что соседи тоже в 
свою очередь могут удалять своих соседей).

В примере для наглядности заменим ветки на числа с возрастом веток.

Исходное дерево:

.1..
..1.
.1..
Прошёл 1-й "чётный" год:

1211
1121
1211  
2-й "нечётный" год:

2322
2232
2322
Уничтожение:

...2
2...
...2
3-й "чётный" год (по чётным годам старые ветки не уничтожаются):

1113
3111
1113
4-й "нечётный" год:

2224
4222
2224
Уничтожение:

.2..
..2.
.2..
и т. д.

Напишите программу, которая моделирует N лет развития дерева, и выводит его результирующую форму -- 
список/массив строк (используются только символы "." и "+").

Функция

string [] TreeOfLife(int H, int W, int N, string [] tree) 
получает высоту H (количество строк) и ширину W (длина строк) дерева, количество лет моделирования N и 
сам список строк, задающий начальное дерево с помощью "." и "+".
Например, исходный пример:

TreeOfLife(3,4, 12, [".+..","..+.",".+.."])
"""

def TreeOfLife(H, W, N, tree):
    tree_list = []
    for x in range(0, H):
        tree_list.append([])
        for i in range(0, W):
            if tree[x][i] == ".":
                tree_list[x].append(0)
            else:
                tree_list[x].append(1)

    for year in range(0, N):
        if year%2 == 0:
            for chet_1 in range(0, H):
                for chet_2 in range(0, W):
                    tree_list[chet_1][chet_2] += 1
        else:
            for nechet_1 in range(0, H):
                for nechet_2 in range(0, W):
                    tree_list[nechet_1][nechet_2] += 1
            for k in range(0, H):
                for g in range(0, W):
                    if type(tree_list[k][g]) == str:
                        continue
                    elif tree_list[k][g] >= 3:
                        try:
                            if (type(tree_list[k-1][g]) != str) and (tree_list[k-1][g] < 3):
                                tree_list[k-1][g] = "++"
                            if (type(tree_list[k+1][g]) != str)  and (tree_list[k+1][g] < 3):
                                tree_list[k+1][g] = "++"
                            if (type(tree_list[k][g-1]) != str) and (tree_list[k][g-1] < 3):
                                tree_list[k][g-1] = "++"
                            if (type(tree_list[k][g+1]) != str) and  (tree_list[k][g+1] < 3):
                                tree_list[k][g+1] = "++"
                        except IndexError:
                            continue
            for p in range(0, H):
                for o in range(0, W):
                    if (tree_list[p][o] == "++") or (tree_list[p][o] >= 3):
                        tree_list[p][o] = 0

    for q in range(0, H):
        for w in range(0, W):
            if tree_list[q][w] == 0:
                tree_list[q][w] = "."
            else:
                tree_list[q][w] = "+"
    result_list = []
    for el in tree_list:
        result_list.append("".join(el))


            
    
        
    return result_list



print(TreeOfLife(3, 4, 4, [".+..","..+.",".+.."]))