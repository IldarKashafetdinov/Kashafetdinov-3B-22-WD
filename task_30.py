def get_qty_letters(string):
    vowels = 0
    consonants = 0

    low_string = string.lower()

    for i in low_string:
        if i.isalpha():
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "y":
                vowels += 1
            else:
                consonants += 1

    return f"Колличество гласныx: {vowels} \nКолличество согласных: {consonants}"

st = get_qty_letters(str(input("Введите строку: ")))

print(st)
