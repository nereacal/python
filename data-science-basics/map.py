#Recorre los elementos de la lista, los eleva al cuadrado y los guarda en una nueva lista (squares)
my_list = [1,2,3,4,5,6,7,8,9,10]
squares = list(map(lambda x:x**2, my_list))
print(squares)