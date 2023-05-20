import random

my_list = []

for i in range(10):
    my_list.append(random.randint(1, 100))

print(my_list)

x = int(input("Введите число: "))

if x in my_list:
    print("Число найдено в массиве")
else:
    print("Число не найдено в массиве")