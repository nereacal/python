# Librería para data analisis

# Leer un archivo en csv
import pandas as pd

csv_path="file1.csv"

df = pd.read_csv(csv_path)
df.head() # expone las primeras 5 lineas

# El resultado es un dictionary
# Las claves corresponden a los valores de las coulumnas
# Los valores corresponden a los valores de las filas
# Casteamos el dictinoary a un dataframe
songs_frame = pd.DataFrame(df)
# Nos devolverá una tabla

# Para obtener los valores de una columna:
val = df[['nombre_columna']] # El resultado es un nuevo dataframe con los valores de la columna

# Para sacar más de una columna
val = df[['columna_1', 'columna_5', 'columna_7']] 

# Para encontrar los distinct valores de un dataframe -> función unique()
# Inidcamos el nombre de la columna
df['nombre_columna'].unique()

# Encontrar todos los valores de una columna que pertenezcan a cierto criterio dado en una columna (ej, valores mayores o iguales a 10 en nombre_columna)
df1 = df[df['nombre_columna'] >= 10]

# Save as csv
df1.to_csv('nombre_del_nuevo_archivo.csv')