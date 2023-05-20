import random

my_list = []

for i in range(10):
    my_list.append(random.randint(1, 10))

print(sum(my_list))
