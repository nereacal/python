# Expresiones combinando variables con operadores
# Teniendo un código, si la afirmación (assert) se cumple, sigue, si no, Error
# assert condition, mensaje de error

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num%i == 0:
            divisors.append(i)
    
    return divisors


def run():
    num = input("Escribe un número: ")
    assert num.isnumeric(), "Tiene que ser un número"
    print(divisors(int(num)))
    print('Fin del programa')

        

if __name__ == "__main__":
    run()