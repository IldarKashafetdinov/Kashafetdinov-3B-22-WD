n = input("")


try:
    i = 1
    s = 0

    while i <= int(n):
        s = i + s
        i = i + 1
    print(s)

except ValueError:
    print("Ошибка")
