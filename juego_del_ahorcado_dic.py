import random
import os

def read():
    with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
        words = [i.replace('\n', '') for i in f]
    return words


def run():
    words = read()
    word = random.choice(words)
    print(word)
    diccionario = dict(word)
    print(diccionario)




if __name__ == '__main__':
    run()