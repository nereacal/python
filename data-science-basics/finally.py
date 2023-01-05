# FInally se usa al final de una estructura para poder cerrar un file, una conexión a bbdd o liberar recursos externos.

try:
    f = open("archivo.txt")
    #hacer cualquier cosa con nuestro archivo
finally:
    f.close()