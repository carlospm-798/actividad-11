"""
Carlos Paredes Márquez.
Clase particula. xd
28/10/2020.
"""
class Particula:
    def __init__(self, id=0, origen_x=0, origen_y=0, destino_x=0, destino_y=0, velocidad=0, red=0, green=0, blue=0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
    
    def __str__(self):
        return(
            'ID: ' + str(self.__id) + '\n' +
            'Origen x: ' + str(self.__origen_x) + '\n' +
            'Origen y: ' + str(self.__origen_y) + '\n' +
            'Destino x: ' + str(self.__destino_x) + '\n' +
            'Destino y: ' + str(self.__destino_y) + '\n' +
            'Velocidad: ' + str(self.__velocidad) + '\n' +
            'Red: ' + str(self.__red) + '\n' +
            'Green: ' + str(self.__green) + '\n' +
            'Blue: ' + str(self.__blue) + '\n'
        )
    
    def to_dict(self):
        return {
            'id': self.__id,
            'origen_x': self.__origen_x,
            'origen_y': self.__origen_y,
            'destino_x': self.__destino_x,
            'destino_y': self.__destino_y,
            'velocidad': self.__velocidad,
            'red': self.__red,
            'green': self.__green,
            'blue': self.__blue
        }

#P01 = Partiula(id=10, origen_x=12, origen_y=13, destino_x=21, destino_y=22, velocidad=180, red= 15, green=18, blue=36)