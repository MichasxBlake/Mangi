from tkinter import *

class Error():

    def Ustawienia(self):
        self.root3.title("Error")
        self.root3.config(bg = "#1B1324")
        self.root3.resizable(width=False, height=False)
        self.root3.geometry('200x100')

    def Okno(self):
        self.Label_Number_1 = Label(self.root3, text="Nie istnieje taka manga", fg="#8E7719", bg="#1B1324")
        self.Label_Number_1.config(font=("Courier", 10, "bold"))
        self.Label_Number_1.place(relx=0.03, rely=0.2)
        self.Przycisk = Button(self.root3,text='Ok', fg="#8E7719", bg="#1B1324",command=self.Exit)
        self.Przycisk.config(font=("Courier", 11, "bold"))
        self.Przycisk.place(relx=0.4, rely=0.5)

    def Exit(self):
        self.root3.destroy()

    def Start(self):
        self.root3.mainloop()

class Login_Error():

    def Ustawienia(self):
        self.root3.title("Niepoprawny Login")
        self.root3.config(bg = "#1B1324")
        self.root3.resizable(width=False, height=False)
        self.root3.geometry('200x100')

    def Okno(self):
        self.Label_Number_1 = Label(self.root3, text="Podany Login nie istnieje", fg="#8E7719", bg="#1B1324")
        self.Label_Number_1.config(font=("Courier", 10, "bold"))
        self.Label_Number_1.place(relx=0.03, rely=0.2)
        self.Przycisk = Button(self.root3,text='Ok', fg="#8E7719", bg="#1B1324",command=self.Exit)
        self.Przycisk.config(font=("Courier", 11, "bold"))
        self.Przycisk.place(relx=0.4, rely=0.5)

    def Exit(self):
        self.root3.destroy()

    def Start(self):
        self.root3.mainloop()


class Haslo_Error():

    def Ustawienia(self):
        self.root3.title("Niepoprawne Hasło")
        self.root3.config(bg="#1B1324")
        self.root3.resizable(width=False, height=False)
        self.root3.geometry('200x100')

    def Okno(self):
        self.Label_Number_1 = Label(self.root3, text="Niepoprawne Hasło", fg="#8E7719", bg="#1B1324")
        self.Label_Number_1.config(font=("Courier", 10, "bold"))
        self.Label_Number_1.place(relx=0.03, rely=0.2)
        self.Przycisk = Button(self.root3, text='Ok', fg="#8E7719", bg="#1B1324", command=self.Exit)
        self.Przycisk.config(font=("Courier", 11, "bold"))
        self.Przycisk.place(relx=0.4, rely=0.5)

    def Exit(self):
        self.root3.destroy()

    def Start(self):
        self.root3.mainloop()

class Zmienna_Error():

    def Ustawienia(self):
        self.root3.title("Błąd w cenie bądź Ilości")
        self.root3.config(bg="#1B1324")
        self.root3.resizable(width=False, height=False)
        self.root3.geometry('200x100')

    def Okno(self):
        self.Label_Number_1 = Label(self.root3, text="Proszę wprowadzić dane liczbowe w Ilość oraz cena", fg="#8E7719", bg="#1B1324")
        self.Label_Number_1.config(font=("Courier", 10, "bold"))
        self.Label_Number_1.place(relx=0.03, rely=0.2)
        self.Przycisk = Button(self.root3, text='Ok', fg="#8E7719", bg="#1B1324", command=self.Exit)
        self.Przycisk.config(font=("Courier", 11, "bold"))
        self.Przycisk.place(relx=0.4, rely=0.5)

    def Exit(self):
        self.root3.destroy()

    def Start(self):
        self.root3.mainloop()