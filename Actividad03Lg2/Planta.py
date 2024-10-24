from Especie import Especie

class Planta(Especie):
    def __init__(self, nombre, reproduccion):
        super().__init__(nombre, 'planta', reproduccion)