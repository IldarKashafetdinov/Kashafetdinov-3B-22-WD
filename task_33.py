def count_symbol(st):
    dictionary = {}

    for symbol in st:
        key = " ".join(symbol)
        dictionary[key] = dictionary.get(key, 0) + 1

    return dictionary

res = count_symbol(input("Введите строку: "))
print(res)
