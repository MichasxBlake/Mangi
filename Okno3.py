from tkinter import *
import sqlite3
global login

t = sqlite3.connect('database.db')
mycursor = t.cursor()
#w momencie usunięcia bazy dancyh odznaczyć te polecenia i wykonać
#mycursor.execute('''CREATE TABLE Mangi (Nazwa_Mangi VARCHAR(30), Ilość INT(31), Od INT(32), Do INT(32),Cena INT(33), Cała_Cena INT(34))''')
#mycursor.execute('''INSERT INTO `Mangi`(`Nazwa_Mangi`, `Ilość`,`Od`,`Do`, `Cena`, `Cała_Cena`) VALUES ('No.6', 5, 1, 5, 19.47, 97.35)''')
t.commit()

class Admin():

    def Ustawienia(self):
        self.root2.title("Admin")
        self.root2.config(bg = "#1B1324")
        self.root2.resizable(width=False, height=False)
        self.root2.geometry('500x700')

    def Widok(self):

        self.text1 = Label(self.root2, text="Podaj Nazwę Mangi:", fg="#8E7719", bg="#1B1324")
        self.text1.config(font=("Courier", 14, "bold"))
        self.text1.place(relx=0, rely=0.05)
        self.get_1 = Entry(self.root2, bg="white")
        self.get_1.place(relx=0.5, rely=0.066)
        self.text2 = Label(self.root2, text="Podaj Ilość:", fg="#8E7719", bg="#1B1324")
        self.text2.config(font=("Courier", 14, "bold"))
        self.text2.place(relx=0, rely=0.09)
        self.get_2 = Entry(self.root2, bg="white")
        self.get_2.place(relx=0.5, rely=0.095)
        self.text3 = Label(self.root2, text="Od", fg="#8E7719", bg="#1B1324")
        self.text3.config(font=("Courier", 14, "bold"))
        self.text3.place(relx=0, rely=0.13)
        self.get_3 = Entry(self.root2, bg="white")
        self.get_3.place(relx=0.5, rely=0.124)
        self.text4 = Label(self.root2, text="Do", fg="#8E7719", bg="#1B1324")
        self.text4.config(font=("Courier", 14, "bold"))
        self.text4.place(relx=0, rely=0.17)
        self.get_4 = Entry(self.root2, bg="white")
        self.get_4.place(relx=0.5, rely=0.153)
        self.text5 = Label(self.root2, text="Cena", fg="#8E7719", bg="#1B1324")
        self.text5.config(font=("Courier", 14, "bold"))
        self.text5.place(relx=0, rely=0.21)
        self.get_5 = Entry(self.root2, bg="white")
        self.get_5.place(relx=0.5, rely=0.182)
        self.text6 = Label(self.root2, text="Cała Cena", fg="#8E7719", bg="#1B1324")
        self.text6.config(font=("Courier", 14, "bold"))
        self.text6.place(relx=0, rely=0.25)
        self.get_6 = Entry(self.root2, bg="white")
        self.get_6.place(relx=0.5, rely=0.211)

        self.button_accept1 = Button(self.root2, text="Accept", fg="black", padx=80, pady=5, command=self.Akceptuj)
        self.button_accept1.place(relx=0.219, rely=0.30)

    def Start(self):
        self.root2.mainloop()

    def Akceptuj(self):
        var1 = str(self.get_1.get())
        var2 = str(self.get_2.get())
        var3 = str(self.get_3.get())
        var4 = str(self.get_4.get())
        var5 = str(self.get_5.get())
        var6 = str(self.get_6.get())
        mycursor.execute('''INSERT INTO `%s`(`Nazwa_Mangi`,`Ilość`,`Od`,`Do`,`Cena`,`Cała_Cena`) VALUES (?,?,?,?,?,?)'''%(login),[var1,var2,var3,var4,var5,var6])
        t.commit()

