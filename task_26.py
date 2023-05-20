def calculate_least_common_multiple(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm

x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))

print(f"Наименьшее общее кратное для чисел {x} и {y} равно {calculate_least_common_multiple(x, y)}")