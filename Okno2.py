from tkinter import *
from Okienka import Error
import sqlite3

t = sqlite3.connect('database.db')
mycursor = t.cursor()

test = 0
var1 = 0
var2 = 0


class Dodawanie():

    #def __init__(self,root1 = Tk()):
        #self.root1 = root1

    def Ustawienia(self):
        self.test = test
        self.root1.title("Mangi")
        self.root1.config(bg = "#1B1324")
        self.root1.resizable(width=False, height=False)
        self.root1.geometry('500x700')

    def Okno(self):
        self.Label_Number_1 = Label(self.root1, text="Mangi", fg="#8E7719", bg="#1B1324")
        self.Label_Number_1.config(font=("Courier", 20, "bold"))
        self.Label_Number_1.place(relx=0.3, rely=0)

        self.text1 = "kjffsfajfja"
        self.Label_Number_2 = Label(self.root1, text=self.text1, fg="#8E7719", bg="#1B1324")
        self.Label_Number_2.config(font=("Courier", 10, "bold"))
        self.Label_Number_2.place(relx=0.06, rely=0.1)

        self.text1 = Label(self.root1, text="Podaj Nazwę Mangi:", fg="#8E7719", bg="#1B1324")
        self.text1.config(font=("Courier", 14, "bold"))
        self.text1.place(relx=0, rely=0.05)
        self.get_1 = Entry(self.root1, bg="white")
        self.get_1.place(relx=0.5, rely=0.066)
        self.text2 = Label(self.root1, text="Podaj Tom:", fg="#8E7719", bg="#1B1324")
        self.text2.config(font=("Courier", 14, "bold"))
        self.text2.place(relx=0, rely=0.09)
        self.get_2 = Entry(self.root1, bg="white")
        self.get_2.place(relx=0.5, rely=0.095)

        self.button_accept1 = Button(self.root1, text="Accept", fg="black", padx=80, pady=5, command=self.Dodawanie)
        self.button_accept1.place(relx=0.219, rely=0.17)

    def Start(self):
        self.root1.mainloop()

    def Dodawanie(self):
        var1 = str(self.get_1.get())
        file=open('file.txt','r')
        login = file.read()
        #Lista otrzymuje 1 tom
        mycursor.execute('''SELECT `Nazwa_Mangi` FROM `%s`'''%(login))
        result = [item[0] for item in mycursor.fetchall()]
        for i in result:
            if var1 == i:
                var2 = int(self.get_2.get())
                mycursor.execute(''' UPDATE `%s` SET `Ilość` = Ilość + 1 WHERE `Nazwa_Mangi` = ? '''% (login), [var1])
                #cena całkowita jest powiększana o dany tom
                mycursor.execute('''SELECT `Cena` FROM `%s` WHERE `Nazwa_Mangi` = ?'''%(login),[var1])
                result1 = [item[0] for item in mycursor.fetchall()]
                if result1[0] > 5:
                    mycursor.execute(''' UPDATE `%s` SET `Cała_Cena` = Cała_Cena + ? WHERE `Nazwa_Mangi` = ? '''%(login), [result1[0],var1])
                #dodano tom do 'Od_do'
                mycursor.execute('''SELECT `Do` FROM `%s` WHERE `Nazwa_Mangi` = ?'''%(login), [var1])
                result2 = [item[0] for item in mycursor.fetchall()]
                if result2[0] > var2:
                    mycursor.execute(''' UPDATE `%s` SET `Od` = ? WHERE `Nazwa_Mangi` = ? '''%(login), [var2,var1])
                else:
                    mycursor.execute(''' UPDATE `%s` SET `Do` = ? WHERE `Nazwa_Mangi` = ? '''%(login), [var2,var1])
                t.commit()
            else:
                self.test=self.test+1
        if self.test == len(result):
            error = Error()
            error.root3 = Tk()
            error.Ustawienia()
            error.Okno()
            file.close()
            error.Start()
            quit()