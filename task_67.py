import sqlite3

# подключение к бд
conn = sqlite3.connect('database.db')


# создание таблицы
cursor = conn.cursor()    # объект который делает запросы и получает их результаты
cursor.execute('''DROP TABLE books''')   # дроп таблицы
cursor.execute('''CREATE TABLE books
(id INTEGER PRIMARY KEY, name TEXT, author TEXT, realise DATE)''')


# вставка данных в таблицу
cursor.execute("INSERT INTO books (name, author, realise) VALUES (?, ?, ?)", ('1984', 'Джордж Оруэлл', '1949-05-06'))
cursor.execute("INSERT INTO books (name, author, realise) VALUES (?, ?, ?)", ('Маленький принц', 'Антуан де Сент-Экзюпери', '1943-11-07'))
cursor.execute("INSERT INTO books (name, author, realise) VALUES (?, ?, ?)", ('Убийство Роджера Экройда', 'Агата Кристи', '1926-02-01'))
cursor.execute("INSERT INTO books (name, author, realise) VALUES (?, ?, ?)", ('Гарри Поттер', 'Дж.Роулинг', '2003-04-06'))


cursor.execute("SELECT * FROM books WHERE realise >= '2000-01-01'")  # выборка из таблицы
rows = cursor.fetchall()   # получение записей из выборки


for row in rows:
    print(row)      # вывод на экран каждой строки

conn.close()   # закрытие подключения
