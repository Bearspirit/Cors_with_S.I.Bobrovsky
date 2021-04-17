class Cat:
    def __init__(self, name, weight, fg):
        self.name = name
        self.weight = weight
        self.fg = fg

    def get_fg(self):
        print(self.name + " мурлычет с частотой " + str(self.fg) + "Гц")

cl_list = []
with open("classes.txt", "rt") as cl:
    try:
        for s in cl:
            cl_prom_list = s.split(" ")
            assert len(cl_prom_list) == 3
            new_obj = Cat(cl_prom_list[0], float(cl_prom_list[1]), int(cl_prom_list[2].rstrip()))
            cl_list.append(new_obj)
    except TypeError:
        print("Проверьте тип данных")  
    except AssertionError:
        print("Проверьте наличие и корректность данных в строке")
    except ValueError:
        print("Проверьте корректность типа данных")
    except SyntaxError:
        print("Ошибка в коде")
    

for k in cl_list:
    k.get_fg()