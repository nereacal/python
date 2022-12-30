class Circle (object):

#Constructor de clase con __init__. self es como "this"
    def __init__(self, radius, color):  
        self.radius = radius
        self.color = color


#Inicializando un objecto de la clase Circle
RedCircle = Circle(10, "red")   

#Accediendo a las propiedades de la instancia
RedCircle.radius                
RedCircle.color

#Modificando las propiedades
RedCircle.color = "Blue"        
RedCircle.radius = 15


#Funcion para añadir radio
def add_radius(self, rad):
    self.radius = self.radius + rad
    return (self.radius)

#Dir sirve para obtener la lista de atributos y metodos asociados a una clase
dir(RedCircle)
