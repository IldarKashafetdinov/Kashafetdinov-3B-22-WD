class TodoList:

    def __init__(self):
        with open('todo.txt', 'r', encoding='utf-8') as file:
            self.lines = file.read()
            file.close()

    # Добавление строки
    def add(self, string):
        with open('todo.txt', 'a', encoding='utf-8') as file:
            file.writelines(string + '\n')
            file.close()
        return

    # Удаление строки
    def delete(self, index):
        with open('todo.txt', 'r') as file:
            lines = file.readlines()
            del lines[index]
            file.close()
        with open('todo.txt', 'w') as file:
            file.writelines(lines)
            file.close()
        return

    # Вывод на экран
    def print(self):
        return print(self.lines)

my_list = TodoList()

my_list.add("kekjejd")
my_list.delete(1)

my_list.print()