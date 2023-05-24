def get_reverse_string(string):
    result = ""
    for i in range(len(string) - 1, -1, -1):
        result += string[i]
    return result


st = get_reverse_string(str(input("Введите строку: ")))

print(st)
