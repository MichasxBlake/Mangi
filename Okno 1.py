from tkinter import *
import sqlite3

t = sqlite3.connect('database.db')

mycursor = t.cursor()
#mycursor.execute('''INSERT INTO `Mangi`(`Nazwa_Mangi`, `Ilość`,'Od_do', `Cena`, `Cała_Cena`) VALUES ('No.6',5,'1-5', 19.47, 97.35)''')
#mycursor.execute('''CREATE TABLE Mangi (Nazwa_Mangi VARCHAR(30), Ilość INT(31), Od_do VARCHAR(32), Cena INT(33), Cała_Cena INT(34))''')
mycursor.execute('''SELECT * FROM `mangi` WHERE 1''')
t.commit()
result = mycursor.fetchall()
for r in result:
    print(r)

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

    def Start(self):
        self.root.mainloop()

a =Main()
a.Ustawienia()
a.Okno()
a.Start()