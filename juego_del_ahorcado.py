# Imprime unos _ para cada letra
# El usuario tiene que ir metiendo letras
# Si hacierta la letra, se reemplaza el _ por la letra
# Incorporar comprehensions
# Manejar los errores
# manejo de archivos
# funcion enumerate
# método get para los diccionarios
# os.system("clear") - para limpiar la pantalla

# Leer el archivo y guardar en una lista
# Sacar una palabra random y guardar en variable palabra_a_adivinar

import random
import os

def read():
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        words = [i.replace('\n', '') for i in f]
    return(words)


def juego(word, lines):
    w = list()
    l = list(lines)
    user = ''

    while w != word:
        user = input('Ingresa una letra: ')
        assert len(user) == 1, 'Tienes que ingresar una letra!'

        for i in range(len(word)):
            if user == word[i]:
                w.append(i) = word[i]
        print(l)
    
    print('Has ganado !')

        


def run():
    words = read()
    word = random.choice(words)
    print('Adivina la palabra!\n')
    word = list(word)
    lines = '_' * len(word)
    print(' '.join(lines))
    print(word)
    juego(word, lines)


if __name__ == '__main__':
    run()