file_name = str(input("Введите имя файла: "))


try:
    file = open(file_name, 'r')
    text = file.read()
    print(text)

except FileNotFoundError:
    print("Ошибка! Такого файла не существует")

except:
    print("Ошибка!")
