class Warrior:
    def __init__(self, wr_name, wr_strong, wr_int, wr_speed, wr_hp, wr_ds):
        self.name = wr_name
        self.strong = wr_strong
        self.intellect = wr_int
        self.speed = wr_speed
        self.HP = wr_hp
        self.dam_speed = wr_ds

    def get_name(self):
        return self.name

    def set_strong(self, strong):
        assert strong >= 0
        self.strong += strong

    def get_strong(self):
        return self.strong




bers = Warrior("Berserk", 100, 50, 60, 300, 90)
print(bers.get_name()) 
bers.set_strong(100)
print(bers.get_strong())


