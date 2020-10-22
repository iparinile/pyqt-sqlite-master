import sqlite3

db = sqlite3.connect('data.db')
cursor = db.cursor()

cursor.execute('PRAGMA foreign_keys=on')

cursor.execute("CREATE TABLE if not exists Товары("
               "Номер_товара INTEGER PRIMARY KEY AUTOINCREMENT, "
               "Название VARCHAR(30), "
               "Цена INTEGER)")

cursor.execute("CREATE TABLE if not exists Оборотная_ведомость("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "Номер_товара INTEGER,"
               "Поступило INTEGER,"
               "Реализовано INTEGER,"
               "FOREIGN KEY (Номер_товара) REFERENCES Товары(Номер_товара))")

cursor.execute("CREATE TABLE if not exists Товарный_план("
               "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
               "Номер_товара INTEGER,"
               "План INTEGER,"
               "FOREIGN KEY (Номер_товара) REFERENCES Товары(Номер_товара))")


cursor.execute("INSERT INTO Товары (Название) VALUES ('карандаш')")
cursor.execute("INSERT INTO Товарный_план (Номер_товара, План) VALUES (1, 25)")
db.commit()
