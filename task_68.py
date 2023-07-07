import sqlite3

# подключение к бд
conn = sqlite3.connect('database.db')


# создание таблицы
cursor = conn.cursor()    # объект который делает запросы и получает их результаты
cursor.execute('''DROP TABLE films''')   # дроп таблицы
cursor.execute('''CREATE TABLE films
(id INTEGER PRIMARY KEY, name TEXT, genre TEXT, rating INTEGER)''')


# вставка данных в таблицу
cursor.execute("INSERT INTO films (name, genre, rating) VALUES (?, ?, ?)", ('Зеленая миля', 'драма', 9.1))
cursor.execute("INSERT INTO films (name, genre, rating) VALUES (?, ?, ?)", ('Интерстеллар', 'фантастика', 8.6))
cursor.execute("INSERT INTO films (name, genre, rating) VALUES (?, ?, ?)", ('Темный рыцарь', 'фантастика', 8.5))
cursor.execute("INSERT INTO films (name, genre, rating) VALUES (?, ?, ?)", ('Джентльмены', 'криминал', 8.6))


cursor.execute("SELECT * FROM films WHERE genre is 'фантастика'")  # выборка из таблицы
rows = cursor.fetchall()   # получение записей из выборки


for row in rows:
    print(row)      # вывод на экран каждой строки

conn.close()   # закрытие подключения
