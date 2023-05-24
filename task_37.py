list = []
print("Заполните список десятью значениями")
i = 10
while i > 0:
    n = int(input(f"{i} осталось: "))
    list.append(n)
    i -= 1

list.sort()
print(f"Двы наименьших значения списка - {list[0]} и {list[1]}")
