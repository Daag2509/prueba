from Especie import Especie

class Carnivoro(Especie):
    def __init__(self, nombre, reproduccion, busqueda, tasa_efectividad):
        super().__init__(nombre, 'carnivoro', reproduccion)
        self.busqueda = busqueda
        self.tasa_efectividad = tasa_efectividad
        self.tasa_mortalidad_adicional = 0.02
        self.comio_hoy = False

    def comer(self):
        self.comio_hoy = True

    def morir_por_vejez(self):
        if not self.comio_hoy:
            self.morir(0.1)
        else:
            self.comio_hoy = False