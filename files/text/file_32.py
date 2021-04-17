import random

name1 = str(random.randint(1, 10)) + ".txt"
name2 = str(random.randint(1, 10)) + ".txt"
def get_sum(fl):
    try: 
        with open(fl, "rt") as nf:
            a = 0
            for s in nf:
                a += int(s.rstrip())
            return a
    except TypeError:
        print("Некорректный тип данных")
    except SyntaxError:
        print("Ошибка в коде") 
    except ValueError:
        print("Проверьте корректность данных, наличие пустой строки")
       

print(get_sum(name1) + get_sum(name2))