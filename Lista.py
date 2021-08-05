from tkinter import *
import sqlite3


t = sqlite3.connect('database.db')

c = t.cursor()

class Lista:

    #def __init__(self, zol=Tk()):
        #self.zol = zol

    def v(self):
        file=open('file.txt','r')
        login=file.read()
        file.close()
        self.zol.title("Lista Mang")
        self.zol.config(bg="#1B1324")
        self.zol.resizable(width=False, height=False)
        c.execute('''SELECT * FROM `%s`'''%(login))
        self.lst = []
        templist = c.fetchall()
        my_columns = 0
        for row in templist:
            self.lst.append(row)
            my_columns += 1
        self.total_rows = len(self.lst)
        self.total_columns = len(self.lst[0])

    def Enter(self):
        for i in range(self.total_rows):
            for j in range(self.total_columns):
                self.e = Entry(self.zol, width=20, fg='black', font=('Arial', 16, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, self.lst[i][j])

    def z(self):
        self.zol.mainloop()
