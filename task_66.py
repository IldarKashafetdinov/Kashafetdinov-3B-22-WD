import sqlite3

# подключение к бд
conn = sqlite3.connect('database.db')


# создание таблицы
cursor = conn.cursor()    # объект который делает запросы и получает их результаты
cursor.execute('''CREATE TABLE IF NOT EXISTS students
(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, avarage_score INTEGER)''')


# вставка данных в таблицу
cursor.execute("INSERT INTO students (name, age, avarage_score) VALUES (?, ?, ?)", ('Alex', 35, 2))
cursor.execute("INSERT INTO students (name, age, avarage_score) VALUES (?, ?, ?)", ('Bob', 21, 4))
cursor.execute("INSERT INTO students (name, age, avarage_score) VALUES (?, ?, ?)", ('Peter', 19, 5))
cursor.execute("INSERT INTO students (name, age, avarage_score) VALUES (?, ?, ?)", ('Ann', 23, 5))


cursor.execute("SELECT * FROM students")  # выборка из таблицы
rows = cursor.fetchall()   # получение записей из выборки


for row in rows:
    print(row)      # вывод на экран каждой строки

conn.close()   # закрытие подключения
