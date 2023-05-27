try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    res = num1 / num2
    print(f'Результат: {res}')

except ValueError:
    print("Ошибка")

except ZeroDivisionError:
    print("Деление на ноль невозможно")

finally:
    print("Завершение программы")
