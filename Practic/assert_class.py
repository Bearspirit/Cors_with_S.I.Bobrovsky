class Warrior:
    def __init__(self, wr_name, wr_strong, wr_int, wr_speed, wr_hp, wr_ds, wr_armor):
        self.name = wr_name
        self.strong = wr_strong
        self.intellect = wr_int
        self.speed = wr_speed
        self.HP = wr_hp
        self.dam_speed = wr_ds
        self.armor = wr_armor


    def get_name(self):
        return self.name

    def set_strong(self, strong):
        assert strong >= 0
        self.strong += strong

    def get_strong(self):
        return self.strong

    def get_vitality(self):
        assert self.armor in ["light", "heavy", "robe"]
        if self.armor == "light":
            return self.HP + 200
        elif self.armor == "heavy":
            return self.HP + 400
        else:
            return self.HP


bers = Warrior("Berserk", 100, 50, 60, 300, 90, "robe")
print(bers.get_name()) 
bers.set_strong(100)
print(bers.get_strong())
print(bers.get_vitality())

