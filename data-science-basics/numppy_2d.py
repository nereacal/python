# arrays 2D
import numpy as np
a = [[11, 12, 13], [21, 22, 23], [30, 31, 32]]

a = np.array([[11, 12, 13], [21, 22, 23], [30, 31, 32]])

a.ndim # indica el num de dimensiones
a.shape # retorna una tupla con el tamaño = [3, 3]
a.size # tamaño de valores = 9

a[1, 2] # Access the element on the second row and third column
a[1][2] # Access the element on the second row and third column
a[0][0] # Access the element on the first row and first column
a[0:2, 2] # Access the element on the first and second rows and third column