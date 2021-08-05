
class Player():

    def __init__(self, HP, weapon):
        self.HP = HP
        self.weapon = weapon
        self.damage = 0

    def set_HP(self, HP):
        if(self.HP > 0):
            self.HP = HP
        else:
            self.HP = 0

    def get_HP(self):
        return self.HP

    def set_weapon(self, weapon):
        self.weapon = weapon

    def get_weapon(self):
        return self.weapon

    def set_damage(self, weapon_name):

        if (weapon_name == "Dagger"):
            self.damage = 4
        elif(weapon_name == "Longsword"):
            self.damage = 5
        else:
            self.damage = 5

    def get_damage(self):
        return self.damage
