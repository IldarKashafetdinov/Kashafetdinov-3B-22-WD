# Существует ли файл в текущей директории

import os

list = os.listdir(".")

res = "Файлa не существует"
for file in list:
    if file == "test.txt":
        res = "Файл существует"

print(res)
