# Controla que el user ingrese strings y no números

def palindromo(string):
    return string == string[::-1]

try:
    print(palindromo(1))
except TypeError:
    print("Solo se pueden ingresar strings")