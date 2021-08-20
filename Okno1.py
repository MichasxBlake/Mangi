from tkinter import *
from Lista import *
from Okno2 import *
from Okno3 import *
import sqlite3


full = 0

t = sqlite3.connect('database.db')

mycursor = t.cursor()
t.commit()

class Main():

    def Ustawienia(self):
        self.root.title("Mangi")
        self.root.config(bg = "#1B1324")
        self.root.resizable(width=False, height=False)
        self.root.geometry('500x700')

    def Okno(self):
        self.Label_Number_1 = Label(self.root, text='całkowita cena: {}'.format(full), fg="#8E7719", bg="#1B1324")
        self.Label_Number_1.config(font=("Courier", 20, "bold"))
        self.Label_Number_1.place(relx=0.1, rely=0)

        self.button1 = Button(self.root, text="Lista Mang", fg="black", padx=80, pady=5, command=self.Lista)
        self.button1.place(relx=0.219, rely=0.17)
        self.button2 = Button(self.root, text="Dodawanie Tomu", fg="black", padx=80, pady=5, command=self.Okno2)
        self.button2.place(relx=0.219, rely=0.30)
        self.button2 = Button(self.root, text="Dodawanie Mang", fg="black", padx=80, pady=5, command=self.Okno3)
        self.button2.place(relx=0.219, rely=0.60)

    def Start(self):
        self.root.mainloop()

    def Lista(self):
        d = Lista()
        d.zol = Tk()
        d.v()
        d.Enter()
        d.z()

    def Okno2(self):
        b = Dodawanie()
        b.root1 = Tk()
        b.Ustawienia()
        b.Okno()
        b.Start()

    def Okno3(self):
        f = Admin()
        f.root2 = Tk()
        f.Ustawienia()
        f.Widok()