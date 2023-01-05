def run():
    
    # 2 maneras de imprimir los nums del 1 al 50 puestos al cubo y que NO son dividibles entre 3

    #my_dict = {}
    #for i in range(1,50):
    #    if i%3 !=0:         
    #        my_dict[i] = i**3
    #print(my_dict)

    #Para cada elemento en un iterable, coloca una llave y un valor SOLAMENTE si se produce la condición (if i%3...)
    my_dict = {i: i**3 for i in range(1,50) if i%3 != 0}
    print(my_dict)

    #Este coloca una llave y un valor para cada número del 1 al 50 haciendo su raíz cuadrada
    my_dicto = {i: i**0.5 for i in range(1,50)}
    print(my_dicto)

    


if __name__ == '__main__':
    run()