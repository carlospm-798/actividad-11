"""
Carlos Paredes Márquez.
Libreria de particulas. xd
28/10/2020.
"""
from particula import Particula
import json

class Libreria:
    def __init__(self):
        self.__particulas = []
    
    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)
    
    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)
    
    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__particulas
        )
    
    def __len__(self):
        return len(self.__particulas)
    
    def __iter__(self):
        self.cont = 0
        return self
    
    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration
        #return self.__particulas[self.cont+1]
    
    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                print(lista)
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0

"""
P01 = Particula(id="10", origen_x="12", origen_y="13", destino_x="21", destino_y="22", velocidad="180", red="15", green="18", blue="36")
P02 = Particula(11, 14, 115, 31, 252, 181, 16, 10, 6)
libreria = Libreria()
libreria.agregar_inicio(P01)
libreria.agregar_inicio(P02)
libreria.mostrar()
"""