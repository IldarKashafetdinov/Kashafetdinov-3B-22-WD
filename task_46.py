try:
    file = open("test.txt", "w")
    file.write("Hello, world!")

except FileNotFoundError:
    print("Ошибка! Такого файла не существует")

except:
    print("Ошибка!")
