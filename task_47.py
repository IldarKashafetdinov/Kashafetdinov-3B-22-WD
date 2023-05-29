number = input("Введите число: ")

try:
    res = int(number) * int(number)
    print(f"{number} в квадрате = {res}")

except ValueError:
    print("Ошибка! Введите число")
