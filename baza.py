import sqlite3

t = sqlite3.connect('database.db')
mycursor = t.cursor()
#w momencie usunięcia bazy dancyh odznaczyć te polecenia i wykonać
mycursor.execute('''CREATE TABLE Mangi (Nazwa_Mangi VARCHAR(30), Ilość INT(31), Od INT(32), Do INT(32),Cena INT(33), Cała_Cena INT(34))''')
mycursor.execute('''INSERT INTO `Mangi`(`Nazwa_Mangi`, `Ilość`,`Od`,`Do`, `Cena`, `Cała_Cena`) VALUES ('Przykład', 0, 0, 0, 0, 0)''')
t.commit()