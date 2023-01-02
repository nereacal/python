import requests
import os 
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r = requests.get(url)

r.status_code # imprime el status de la respuesta para saber si ha ido bien
r.request.headers # ver el header de la request
r.request.body # ver el body de la request
r.headers['date'] # la fecha de la request
r.headers['Content-Type'] # el tipo de data
r.encoding # el encoding
r.text[0:100] # como el content-type es text/html se puede usar text para ver el html del body, ver los primeros 100 caracteres

# para ver otro tipos de dato distintos de text como imagenes. Comillas simples para el string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r=requests.get(url)

# como la imagen es un objeto de respuesta que contiene una imagen en bytes object, lo guardamos en un file, primero se define el nombre y path del file
path = os.path.join(os.getcwd(), 'imagen.png')

# para acceder al body de la respuesta se usa el atributo 'content' y lo guardamos usando open y write
with open(path, 'wb') as f:
    f.write(r.content)

Image.open(path) # para ver la imagen



# POST requests

url_post='http://httpbin.org/post'
payload={"name":"Joseph","ID":"123"}
r_post = requests.post(url_post, data = payload) # en el parametro data se envia la variable payload que tiene un form

print("POST request URL:",r_post.url )
print("GET request URL:",r.url)
print(r_post.json()['form'])