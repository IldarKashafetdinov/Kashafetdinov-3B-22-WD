my_list = []


i = 20
while i != "":
    i = input("Введите число: ")
    try:
        if type(int(i)) == int:
            my_list.append(int(i))
    except ValueError:
        break

print(my_list)
print(min(my_list))
