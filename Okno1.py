from tkinter import *
from Lista import *
from Okno2 import *
from Okno3 import *
import sqlite3

t = sqlite3.connect('database.db')

mycursor = t.cursor()
t.commit()

class Main():

    def __init__(self,root = Tk()):
        self.root = root

    def Ustawienia(self):
        self.root.title("Mangi")
        self.root.config(bg = "#1B1324")
        self.root.resizable(width=False, height=False)
        self.root.geometry('500x700')

    def Okno(self):
        self.Label_Number_1 = Label(self.root, text="Mangi", fg="#8E7719", bg="#1B1324")
        self.Label_Number_1.config(font=("Courier", 20, "bold"))
        self.Label_Number_1.place(relx=0.3, rely=0)

        self.text1 = "kjffsfajfja"
        self.Label_Number_2 = Label(self.root, text=self.text1, fg="#8E7719", bg="#1B1324")
        self.Label_Number_2.config(font=("Courier", 10, "bold"))
        self.Label_Number_2.place(relx=0.06, rely=0.1)

        self.button1 = Button(self.root, text="Lista Mang", fg="black", padx=80, pady=5, command=self.Lista)
        self.button1.place(relx=0.219, rely=0.17)
        self.button2 = Button(self.root, text="Dodawanie Mang", fg="black", padx=80, pady=5, command=self.Okno2)
        self.button2.place(relx=0.219, rely=0.30)
        self.button2 = Button(self.root, text="Admin", fg="black", padx=80, pady=5, command=self.Okno3)
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


a=Main()
a.Ustawienia()
a.Okno()
a.Start()
t.close()