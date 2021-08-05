from tkinter import END, INSERT

from weapon import *

class Goblin():

    def __init__(self):
        self.HP = 3
        self.damage = 1
        self.weapon = "Dagger"

    def set_HP(self, HP):
        if(HP < 0):
            HP = 0
            self.HP = HP
        else:
            self.HP = HP

    def get_HP(self):
        return self.HP

    def get_damage(self):
        return self.damage

    def get_weapon(self):
        return self.weapon
