from math import gcd

list1 = [24, 36, 48, 60]
list2 = [12, 18, 24, 36, 72]

list1.extend(list2)
print(gcd(list1))
