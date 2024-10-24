from Especie import Especie

class Herbivoro(Especie):
    def __init__(self, nombre, reproduccion, busqueda):
        super().__init__(nombre, 'herbivoro', reproduccion)
        self.busqueda = busqueda