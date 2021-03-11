class Warrior:
    def __init__(self, wr_name, wr_strong, wr_int, wr_speed, wr_hp, wr_ds):
        self.name = wr_name
        self.strong = wr_strong
        self.intellect = wr_int
        self.speed = wr_speed
        self.HP = wr_hp
        self.dam_speed = wr_ds
    
    def Power(self):
        power = self.strong * self.dam_speed * self.HP
        return power

    def Damage(self, weapon):
        self.strong += weapon

    def Vitality(self):
        vitality = self.HP * self.speed * 10
        return vitality

class Wizard:
    def __init__(self, wz_name, wz_strong, wz_int, wz_speed, wz_hp, wz_cast):
        self.name = wz_name
        self.strong = wz_strong
        self.intellect = wz_int
        self.speed = wz_speed
        self.HP = wz_hp
        self.cast = wz_cast

    def Power(self):
        power = self.strong * self.cast * self.HP
        return power
    
    def Damage(self, weapon):
        self.strong += weapon

    def Vitality(self):
        vitality = self.HP * self.speed * 10
        return vitality

orc = Warrior("Berserk", 3, 50, 60, 50, 6)
elf = Wizard("Witch", 12, 4, 50, 30, 9)

print(orc.Power(), elf.Power())

orc.Damage(30)
elf.Damage(40)

print(orc.Power(), elf.Power())
print(orc.Vitality(), elf.Vitality())