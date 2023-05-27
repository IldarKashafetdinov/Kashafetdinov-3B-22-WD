try:
    file = open('test.txt', 'r')
    text = file.read()
    print(text)

except FileNotFoundError:
    print("Файл не найден")
