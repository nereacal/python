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


def lineas(word):
    cantidad_letras = len(word)
    line = ['_' for i in word]
    lin = ''.join(line)
    return lin


def juego(word, lines):
    w = list(word)
    l = list(lines)

    letra_candidata = ''
    while w != l:
        letra_candidata = input("Ingresa una letra: ")
        assert len(letra_candidata) == 1, 'Tienes que meter solo una letra a la vez'
        clear = lambda: os.system('cls')
        clear()
        for i in range(0, len(w)):
            if w[i] == letra_candidata:
                l[i] = w[i]
        print(' '.join(l).upper())
        print('\n')
    print('De puta madre! Has ganado. Palabra: ' + word.upper())


def run():
    words = read()
    word = random.choice(words)
    print('Adivina la palabra!\n')
    lines = lineas(word)
    print(' '.join(lines))
    print('\n')
    juego(word, lines)


if __name__ == '__main__':
    run()