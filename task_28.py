a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
multiplication = str(input("Введите операцию, котрую хотите воспроизвести (сложение, вычитание, умножение, деление): "))

if multiplication == "сложение":
    print(f"{a} + {b} = {a + b}")
elif multiplication == "вычитание":
    print(f"{a} - {b} = {a - b}")
elif multiplication == "умножение":
    print(f"{a} * {b} = {a * b}")
elif multiplication == "деление":
    print(f"{a} / {b} = {a / b}")
else:
    print("Введи конкретно операцию")
