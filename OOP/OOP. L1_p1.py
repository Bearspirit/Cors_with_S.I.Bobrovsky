class Warrior:
    name = "Ranger"
    strong = 50
    intellect = 20
    speed = 60
    HP = 300
    armor = "Leight"
    dam_speed = 70
    power = 0
    vitality = 0

class Wizard:
    name = "Witch"
    strong = 25
    intellect = 60
    speed = 50
    HP = 200
    armor = "Robe"
    cast = 100
    power = 0
    vitality = 0

orc = Warrior()
elf = Wizard()
orc.power = orc.strong * orc.dam_speed
elf.power = elf.intellect * elf.cast
orc.vitality = orc.HP * orc.speed
elf.vitality = elf.HP * elf.speed
print(orc.power, orc.vitality)
print(elf.power, elf.vitality)

orc1 = orc
orc1.speed = 30
print(orc.speed)  #выведет присвоенный второму объекту параметр