names_1 = ['Sasha', 'Vera', 'Admin', 10, 'Troll', 'Kolyan']
if names_1:
    for name in names_1:
        assert type(name) == str
        if name == 'Admin':
            print(name + ", Dobro pozhalovat'!")
        else:
            print(name + ", " +"Hello")
else:
    print("Tut pusto")
    
