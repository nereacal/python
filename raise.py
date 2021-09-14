#Controla que el usuario ingrese algo y no deje en blanco el input("")

def palindromo(string):
    try:
        if len(string) == 0:
            raise ValueError("NO se puede dejar la cadena vacía")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

try:
    print(palindromo(""))
except TypeError:
    print("SOlo se pueden ingresar strings")
