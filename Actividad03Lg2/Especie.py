import random

class Especie:
    def __init__(self, nombre, tipo, reproduccion, poblacion=10):
        self.nombre = nombre
        self.tipo = tipo
        self.poblacion = poblacion
        self.reproduccion = reproduccion

    def reproducirse(self):
        if random.random() < self.reproduccion:
            incremento = int(self.poblacion * self.reproduccion)
            self.poblacion += incremento

    def morir(self, muerte):
        disminucion = int(self.poblacion * muerte)
        self.poblacion -= disminucion
        if self.poblacion < 0:
            self.poblacion = 0
                   