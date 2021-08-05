# dungeon crawler game for me and my friends

from tkinter import *

from weapon import *
from player import *
from goblin import *
from Boss import *
import time as time



class Game():
    pass


root = Tk()
p = Player(10, "None")
root.geometry('1690x1120')

frame = Frame(root)
frame.pack(side=BOTTOM)
labelfont = ('times', 10, 'bold')
labelfont2 = ('times', 12)
wep = Text(root, height=2, width=18, font=labelfont)
health = Text(root, height=2, width=15, font=labelfont)
dialog = Text(frame, height=2, width=82, font=labelfont2)

wep.pack(side=TOP, anchor=W)
health.pack(side=TOP, anchor=W)
dialog.pack(side=TOP)

canvas = Canvas(root, width=1152, height=648)
canvas.pack()
img = PhotoImage(file="swords.png")
img2 = PhotoImage(file="cave.png")
img3= PhotoImage(file="goblin.png")
img4 = PhotoImage(file="goblin_dead.png")
img5 = PhotoImage(file="fight.png")
img6 = PhotoImage(file="dead.png")
img7 = PhotoImage(file="complete.png")
img8 = PhotoImage(file="died.png")
picture = canvas.create_image(20, 20, anchor=NW, image=img)

class Start(Game):


    def begin(self):

        start = Button(frame, text="Start", font=labelfont, bg="grey", fg="black", height=10, width=30,
                       command= lambda: self.choose_weapon(start))
        dialog.insert(INSERT, "Welcome to my game. Get started by pressing the start button then choose your weapon.")
        start.pack()
        wep.insert(INSERT, 'Weapon: ' + p.get_weapon())
        health.insert(INSERT, p.get_HP())
        root.mainloop()

    def choose_weapon(self, start):

        labelfont = ('times', 10, 'bold')
        dagger = Button(frame, text="Dagger", font=labelfont, bg="grey", fg="red", height=10, width=30,
                      command=lambda: [p.set_weapon("Dagger"), p.set_damage("Dagger"),
                                          self.entrance(), dagger.pack_forget(), longsword.pack_forget(), scimitar.pack_forget()])
        longsword = Button(frame, text="Longsword", font=labelfont, bg="grey", fg="green", height=10, width=30, command=lambda:[p.set_weapon("Longsword"), p.set_damage("Longsword"),
                                          self.entrance(), dagger.pack_forget(), longsword.pack_forget(), scimitar.pack_forget()])
        scimitar = Button(frame, text="Scimitar", font=labelfont, bg="grey", fg="blue", height=10, width=30,
                         command=lambda: [p.set_weapon("Scimitar"), p.set_damage("Scimitar"),
                                          self.entrance(), dagger.pack_forget(), longsword.pack_forget(), scimitar.pack_forget()])
        dialog.delete(1.0, END)
        dialog.insert(INSERT, "Choose your weapon. Choose between a dagger, longsword, or scimitar.")

        start.pack_forget()
        dagger.pack(side=LEFT)
        longsword.pack(side=LEFT)
        scimitar.pack(side=LEFT)

    def entrance(self):
        picture = canvas.create_image(20, 20, anchor=NW, image=img2)


        labelfont = ('times', 10, 'bold')
        wep.delete(1.0, END)
        wep.insert(INSERT, "Weapon: " + p.get_weapon())
        enter = Button(frame, text="ENTER", font=labelfont, bg="grey", fg="yellow", height=10, width=30,
                        command=lambda: self.goblin_fight(enter))
        dialog.delete(1.0, END)
        dialog.insert(INSERT, "Dangerous beings dwell in this cave. DO you dare to find out who they are?")

        enter.pack()

    def goblin_fight(self, enter):
        picture = canvas.create_image(20, 20, anchor=NW, image=img3)
        g1 = Goblin()
        g2 = Goblin()

        attack = Button(frame, text="ATTACK", font=labelfont, bg="grey", fg="red", height=10, width=30,
                        command=lambda: [p.set_HP(p.get_HP() - 1), health.delete(1.0, END),
                                         health.insert(INSERT, p.get_HP()),
                                         g1.set_HP(g1.get_HP() - p.get_damage()), goblin_health.delete(1.0, END),
                                         goblin_health.insert(INSERT, "Goblin HP: " + str(g1.get_HP())),
                                         root.after(1000, self.goblin_dead(g1, attack, run, goblin_health))])

        run = Button(frame, text="RUN", font=labelfont, bg="grey", fg="blue", height=10, width=30,
                     command=lambda: [self.entrance(), attack.pack_forget(), run.pack_forget(), goblin_health.pack_forget()])

        goblin_health = Text(root, height=2, width=20, font=labelfont)
        goblin_health.pack(side=TOP, anchor=N)
        goblin_health.insert(INSERT, "Goblin HP: " + str(g1.get_HP()))

        enter.pack_forget()
        attack.pack(side=LEFT)
        run.pack(side=LEFT)

        dialog.delete(1.0, END)
        dialog.insert(INSERT, "You enter the cave and encounter a Goblin! ")

    def goblin_dead(self, goblin, button, button2, entry):
        picture = canvas.create_image(20, 20, anchor=NW, image=img4)
        gob_HP = goblin.get_HP()
        if(gob_HP < 1):
            dialog.delete(1.0, END)
            dialog.insert(INSERT, "You managed to kill the goblin! Continue down the cave... or turn back.")
        time.sleep(1)
        button.pack_forget()
        button2.pack_forget()

        walk = Button(frame, text="WALK", font=labelfont, bg="grey", fg="blue", height=10, width=30,
                      command=lambda: [self.boss(), walk.pack_forget(), runs.pack_forget(), entry.pack_forget()])
        runs = Button(frame, text="RUN", font=labelfont, bg="grey", fg="blue", height=10, width=30,
                     command=lambda: [self.entrance(), walk.pack_forget(), runs.pack_forget(), entry.pack_forget()])
        walk.pack(side=LEFT)
        runs.pack(side=LEFT)

    def boss(self):
        picture = canvas.create_image(20, 20, anchor=NW, image=img5)
        boss = Boss()
        attack = Button(frame, text="ATTACK", font=labelfont, bg="grey", fg="red", height=10, width=30,
                        command=lambda: [p.set_HP(p.get_HP()-boss.get_damage()), health.delete(1.0, END), health.insert(INSERT, p.get_HP()),
                                         boss_health.delete(1.0, END), boss.set_HP(boss.get_HP()-p.get_damage()),
                                         boss_health.insert(INSERT, "Toby's HP: " + str(boss.get_HP())), self.end(boss, attack, run, potion, boss_health)])
        run = Button(frame, text="RUN", font=labelfont, bg="grey", fg="blue", height=10, width=30,
                        command=lambda: [self.walking(), attack.pack_forget(), potion.pack_forget()])
        potion = Button(frame, text="DRINK POTION", font=labelfont, bg="grey", fg="yellow", height=10, width=30,
                        command=lambda: [self.potion(potion), health.delete(1.0, END), health.insert(INSERT, p.get_HP())])

        boss_health = Text(root, height=2, width=20, font=labelfont)
        boss_health.pack(side=TOP, anchor=N)
        boss_health.insert(INSERT, "Toby's HP: " + str(boss.get_HP()))

        dialog.delete(1.0, END)
        dialog.insert(INSERT, "You encounter the boss Toby! FIGHT!")
        attack.pack(side=LEFT)
        run.pack(side=LEFT)
        potion.pack(side=LEFT)

    def potion(self, potion):
        p.set_HP(p.get_HP()+5)
        dialog.delete(1.0, END)
        dialog.insert(INSERT, "You've healed yourself 5 hitpoints!")
        potion.pack_forget()

    def end(self, boss, button, button2, button3, entry):
        if(boss.get_HP() < 1 and p.get_HP() > 0):
            time.sleep(1)

            dialog.delete(1.0, END)
            picture = canvas.create_image(20, 20, anchor=NW, image=img6)
            dialog.insert(INSERT, "The boss has been defeated! Please exit the cave.")
            complete = Button(frame, text="PASS", bg="grey", fg="blue", height=10, width=30,
                              command=lambda: [self.leaving(), complete.pack_forget()])
            complete.pack()
            entry.pack_forget()
            button.pack_forget()
            button2.pack_forget()
            button3.pack_forget()
        elif(p.get_HP() < 1):
            time.sleep(1)
            picture = canvas.create_image(20, 20, anchor=NW, image=img8)
            dialog.delete(1.0, END)
            dialog.insert(INSERT, "You have died!")
            died = Button(frame, text="END", bg="grey", fg="blue", height=10, width=30,
                              command=lambda: root.destroy())
            died.pack()
            entry.pack_forget()
            button.pack_forget()
            button2.pack_forget()
            button3.pack_forget()

    def leaving(self):
        time.sleep(1)
        picture = canvas.create_image(20, 20, anchor=NW, image=img7)
        leave = Button(frame, text="LEAVE", bg="grey", fg="green", height=10, width=30, command=lambda: root.destroy())
        leave.pack()

if __name__ == '__main__':
    game = Start()
    game.begin()