import random as rd
from tkinter import *



class Boss():

    def __init__(self):
        self.HP = 20
        self.damage = 2
        self.special = 5
        self.name = "Toby"
        self.weapon = "Great sword"

    def set_HP(self, HP):
        if(HP < 0):
            HP = 0
            self.HP = HP
        else:
            self.HP = HP

    def get_HP(self):
        if(self.HP == 0):
            return self.HP
        else:
            return self.HP

    def get_damage(self):
        if(rd.randint(1,50) < 5):
            return self.special
        else:
            return self.damage

    def get_weapon(self):
        return self.weapon

    def get_name(self):
        return self.name