import sqlite3

# подключение к бд
conn = sqlite3.connect('database.db')


# создание таблицы
cursor = conn.cursor()    # объект который делает запросы и получает их результаты
cursor.execute('''DROP TABLE employes''')   # дроп таблицы
cursor.execute('''CREATE TABLE employes
(id INTEGER PRIMARY KEY, name TEXT, post TEXT, salary INTEGER)''')


# вставка данных в таблицу
cursor.execute("INSERT INTO employes (name, post, salary) VALUES (?, ?, ?)", ('Alex', 'стажер', 1000))
cursor.execute("INSERT INTO employes (name, post, salary) VALUES (?, ?, ?)", ('Bob', 'менеджер', 2000))
cursor.execute("INSERT INTO employes (name, post, salary) VALUES (?, ?, ?)", ('Peter', 'стажер', 3000))
cursor.execute("INSERT INTO employes (name, post, salary) VALUES (?, ?, ?)", ('Ann', 'менеджер', 4000))


cursor.execute("SELECT * FROM employes WHERE post is 'менеджер'")  # выборка из таблицы
rows = cursor.fetchall()   # получение записей из выборки


for row in rows:
    print(row)      # вывод на экран каждой строки

conn.close()   # закрытие подключения
