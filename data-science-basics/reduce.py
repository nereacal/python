#Reducir los valores de una lista con un único valor.

my_list = [2,2,2,2,2]
all_multiplied = 1
for i in my_list:
    all_multiplied = all_multiplied*i
print(all_multiplied)


#Lo mismo de arriba, lambda lo hace así:
from functools import reduce
my_list = [2,2,2,2,2]
all_multiplied = reduce(lambda a, b: a * b, my_list)
print(all_multiplied)