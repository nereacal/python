from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
import pandas as pd

# Beautiful soup saca información de archivos html y xml usando métodos para parsear el html y navegar por el dom para buscar los items
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# Parsear
soup = BeautifulSoup(html, "html.parser")

print(soup.prettify()) # para ver el html

# Acceder a las tags
tag_object=soup.title
print("tag object:",tag_object)
print("tag object type:",type(tag_object)) # el tipo de dato

tag_object = soup.h3
tag_child = tag_object.b # saca el hijo del tag seleccionado
parent_tag = tag_child.parent # saca el parent
tag_object.parent # el parent del tag_object es el body
sibling_1 = tag_object.next_sibling # corresponde al parrafo
sibling_2 = sibling_1.next_sibling

tag_child['id'] # saber el id del tag_child
tag_child.attrs # {'id': 'boldest'}
tag_child.string # acceder al string contenido en el tag



# Otro ejemplo
table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, "html.parser")

# El metodo find_all(name, attrs, recursive, string, limit, **kwargs) encuentra todos descendientes del tag seleccionado aplicando los filtros pasados por parámetros
table_rows = table_bs.find_all('tr') # El resultado es una lista a la que se puede acceder
first_row = table_rows[0] # <tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>
first_row.td # obtiene el hijo <td id="flight">Flight No</td>

table_bs.find_all(id="flight")
list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
table_bs.find_all(href=True)





# Web scrapping de tablas html en dataframe 

url = "https://en.wikipedia.org/wiki/World_population"
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")
tables = soup.find_all('table') # in html table is represented by the tag <table>
print(len(tables)) # para ver cuantas tablas contiene
for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index

print(table_index) # hay unas 4
print(tables[table_index].prettify())

population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

print(population_data)

