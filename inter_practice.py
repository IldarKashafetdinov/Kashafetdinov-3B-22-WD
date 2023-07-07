"""
Написать программу, которая находит и удаляет дубликаты
файлов в указанной директории и всех ее поддиректориях
"""



import os  # импортировать модуль, отвечающий за работу с операционной системой


"""
Функция собирает и возвращает пути до каждого файла в указанной директории и всех ее поддиректориях
"""
def get_paths_files(dir):
    files = []
    paths = os.walk(dir)  # получить кортеж с тремя элементами папки(1-путь до папки, 2-список вложенных папок, 3-список файлов)
    for path in paths:
        for path_file in path[2]:
            if '.DS_Store' not in path_file:  # не добавляем сервисные файлы
                files.append(f'{path[0]}/{path_file}')  # добавить путь до каждого файла в список
    return files



"""
Функция удаляет дубликаты файлов 
"""
def remove_duplicates(paths_files):
    for i in range(len(paths_files)):  # проходит циклом по списку
        try:  # обрабатывает ошибку, когда файл уже удален, а к нему все равно обращается по индексу
            first_file = open(paths_files[i], 'r').read()  # открывает файл с которым сравнивает остальные файлы
            for j in range(len(paths_files)):
                if paths_files[i] != paths_files[j]:  # условие, чтобы не сравнивать файл с самим собой
                    second_file = open(paths_files[j], 'r').read()  # открывает остальные файлы
                    if first_file == second_file:
                        os.remove(paths_files[j])  # удаляет дубликат с диска
                        paths_files.remove(paths_files[j])  # удаляет дубликат из передавоемого списка
        except IndexError:
            continue




if __name__ == "__main__": #точка входа
    path_to_dir = str(input("Введите абсолютный путь до директории: "))
    paths_files = get_paths_files(path_to_dir)
    remove_duplicates(paths_files)

