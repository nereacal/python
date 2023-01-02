# arrays 1D
import numpy as np

# Crear un array sin numpy
a = ["0", 0, "1", 1, "2", 2, "3", 3]

# Crear un array con numpy
a = np.array([0, 1, 2, 3])

# un array numpy contiene valores del mismo tipo de dato.

a.dtype # tipo de datos que contiene el array
a.size # tamaño
a.ndim # el número de dimensiones del array (1D)
a.shape # el tamaño del array de cada dimension

# crear un array solo con los valores del 1 al 4 del array a
a = np.array([100, 1, 2, 3, 0])
b=a[1:4] # b= [1,2,3]

# asignar nuevos valores a los indices 3 al 5
a[3:5] = 300, 400 # a = [100, 1, 2, 300, 400]



# Operaciones
# añadir y sustraer

# Crear una nueva lista con la suma de las listas a y b
a = [1, 0]
b = [0, 1]
z = []
for n, m in zip(a, b):
    z.append(n + m)
#otra manera
z = a + b


# array multiplicación con scalar
z = 2 * b

# Producto de 2 numpy arrays
a = np.array([0, 1, 2, 3])
b = np.array([0, 1, 2, 3])
z = a * b

a = np.array([1, -2, 3, 4, 5])
mean_a = a.mean() # calcula el valor de media de los valores = 2.2
max_a = a.max() # el valor más alto = 5

# mapear numpy arrays con nuevos numpy arrays
np.pi # accede al valor de pi
x = np.array([0, np.pi/2, np.pi]) 
y = np.sin(x)

# crear un array con trazado
# linspace(indice_inicial, indice_final, num_de_samples_a_generar)

a = np.linspace(-2, 2, num=5) # = [-2. -1.  0.  1.  2.]
a = np.linspace(-2, 2, num=9) # = [-2.  -1.5 -1.  -0.5  0.   0.5  1.   1.5  2. ]
print(a)