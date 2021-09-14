def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"nombre": "Nerea", "apellido": "Nerever"}

    super_list = [
        {"nombre": "Nerea", "apellido": "Nerever"},
        {"nombre": "Bugs", "apellido": "Bunny"},
        {"nombre": "Peter", "apellido": "Salas"},
        {"nombre": "Coño", "apellido": "Sucio"},
        {"nombre": "Fleetwood", "apellido": "Mac"},
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43]
    }

    for key, value in super_dict.items():
        print(key, " - ", value)

    for item in super_list:
        print(item['nombre'] , ' - ', item['apellido'])


if __name__ == '__main__':
    run()