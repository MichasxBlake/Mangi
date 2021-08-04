import sqlite3
from tkinter import *
from Okno1 import *

t = sqlite3.connect('database.db')
mycursor = t.cursor()
#mycursor.execute('''CREATE TABLE Login (Login VARCHAR(40),HASŁO VARCHAR(40))''')
#mycursor.execute('''INSERT INTO `Login`(`Login`,`HASŁO`) VALUES ('Admin','Admin')''')
t.commit()

class Head():

    def __init__(self,root = Tk()):
        self.root4 = root

    def Ustawienia(self):
        self.root4.title("Mangi")
        self.root4.config(bg = "#1B1324")
        self.root4.resizable(width=False, height=False)
        self.root4.geometry('500x700')

    def Okno(self):
        self.Label_Number_1 = Label(self.root4, text='Zaloguj się',fg="#8E7719", bg="#1B1324")
        self.Label_Number_1.config(font=("Courier", 20, "bold"))
        self.Label_Number_1.place(relx=0.1, rely=0)


        self.text1 = Label(self.root4, text="Podaj Login:", fg="#8E7719", bg="#1B1324")
        self.text1.config(font=("Courier", 14, "bold"))
        self.text1.place(relx=0, rely=0.05)
        self.get_1 = Entry(self.root4, bg="white")
        self.get_1.place(relx=0.5, rely=0.066)
        self.text2 = Label(self.root4, text="Podaj Hasło:", fg="#8E7719", bg="#1B1324")
        self.text2.config(font=("Courier", 14, "bold"))
        self.text2.place(relx=0, rely=0.09)
        self.get_2 = Entry(self.root4, bg="white")
        self.get_2.place(relx=0.5, rely=0.1)
        self.button_accept1 = Button(self.root4, text="Zaloguj", fg="black", padx=80, pady=5, command=self.Logowanie)
        self.button_accept1.place(relx=0.219, rely=0.17)

    def Logowanie(self):
        login = str(self.get_1.get())
        haslo = str(self.get_2.get())
        mycursor.execute('''SELECT `Login` FROM `Login`''')
        result = [item[0] for item in mycursor.fetchall()]
        for i in result:
            if login == i:
                mycursor.execute('''SELECT `HASŁO` FROM `Login`''')
                result1 = [item[0] for item in mycursor.fetchall()]
                for j in result1:
                    if haslo == j:
                        mycursor.execute('''CREATE TABLE IF NOT EXISTS `%s` (Nazwa_Mangi VARCHAR(30), Ilość INT(31), Od INT(32), Do INT(32),Cena INT(33), Cała_Cena INT(34))'''%(login))
                        a = Main()
                        a.root = Tk()
                        a.Ustawienia()
                        a.Okno()
                        a.Start()
                        t.close()
                self.root4.destroy()

    def Start(self):
        self.root4.mainloop()

r = Head()
r.Ustawienia()
r.Okno()
r.Start()