# Data es una lista de diccionarios
DATA = [
{
    'name': 'Facundo',
    'age': 72,
    'organization': 'Platzi',
    'position': 'Technical Coach',
    'language': 'python',
},
{
    'name': 'Luisana',
    'age': 33,
    'organization': 'Globant',
    'position': 'UX Designer',
    'language': 'javascript',
},
{
    'name': 'Solomillo',
    'age': 19,
    'organization': 'Platzi',
    'position': 'Associate',
    'language': 'ruby',
},
{
    'name': 'Gabriel',
    'age': 20,
    'organization': 'Platzi',
    'position': 'Associate',
    'language': 'javascript',
},
{
    'name': 'Ramera',
    'age': 30,
    'organization': 'Platzi',
    'position': 'QA Manager',
    'language': 'java',
},
{
    'name': 'Karo',
    'age': 23,
    'organization': 'Everis',
    'position': 'Backend Developer',
    'language': 'python',
},
{
    'name': 'Ariel',
    'age': 32,
    'organization': 'Rappi',
    'position': 'Support',
    'language': '',
},
{
    'name': 'Coño Sucio',
    'age': 17,
    'organization': '',
    'position': 'Student',
    'language': 'go',
},
{
    'name': 'Bugs',
    'age': 32,
    'organization': 'Master',
    'position': 'Human Resources Manager',
    'language': 'python',
},
{
    'name': 'Nerea',
    'age': 56,
    'organization': 'Python Organization',
    'position': 'Language Maker',
    'language': 'python',
},
]


def run():

    # Filtrar los nombres de todos los trabajadores de python
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    for worker in all_python_devs:
        print("Desarrollador de Python: " + worker)


    # Filtrar los nombres de todos los que trabajan en Platzi
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    for worker in all_platzi_workers:
        print("Trabaja en Platzi: " + worker)
        

    # FIltra solo los mayores de edad
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    #Hasta aquí me trae todos los datos de cada diccionario en la lista, pero solo queremos el nombre, usamos map
    adults = list(map(lambda worker: worker["name"], adults))
    for worker in adults:
        print("Es adulto: " + worker)



if __name__ == "__main__":
    run()