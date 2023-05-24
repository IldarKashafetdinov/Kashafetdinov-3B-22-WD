from calculator import get_summ
from calculator import get_substraction
from calculator import get_multiplication
from calculator import get_division

a = int(input("Введите число: "))
b = int(input("Введите число: "))

result1 = get_summ(a, b)
result2 = get_substraction(a, b)
result3 = get_multiplication(a, b)
result4 = get_division(a, b)

print(result1)
print(result2)
print(result3)
print(result4)
