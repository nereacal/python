#Imprime solo los núms impares de una lista

my_list = [1,2,3,4,5,6,7,8,9,10]
res = [i for i in my_list if i%2 !=0]
print(res)


#Lo mismo de arriba, lo hace lambda así:
my_lista = [1,2,3,4,5,6,7,8,9,10]
resul = list(filter(lambda x: x%2 !=0, my_lista))
print(resul)