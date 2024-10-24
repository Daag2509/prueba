import json
import random
from Planta import Planta
from Herviboro import Herbivoro
from Carnivoro import Carnivoro

class Ecosistema:
    def __init__(self):
        self.especies = []

    def agregar_especie(self, especie):
        """ Agrega una nueva especie al ecosistema """
        self.especies.append(especie)

    def simular_dia(self):
        """ Simula un día en el ecosistema """

        print("Iniciando un nuevo día...")

        # Reproducción de plantas
        for especie in filter(lambda x: isinstance(x, planta), self.especies):
            especie.reproducirse()

        # Alimentación de herbívoros
        for herbivoro in sorted(filter(lambda x: isinstance(x, Herbivoro), self.especies), 
                                key=lambda x: x.capacidad_busqueda, reverse=True):
            planta_alimentada = False
            for planta in filter(lambda x: isinstance(x, Planta) and x.poblacion > 0, self.especies):
                if random.random() < herbivoro.capacidad_busqueda:
                    comida_consumida = min(planta.poblacion // 2, herbivoro.poblacion)  
                    planta.poblacion -= comida_consumido
                    herbivoro.poblacion += comida_consumido // 2  
                    planta_alimentada = True
                    break

            if not planta_alimentada:
                herbivoro.morir(0.1)  

        # Alimentación de carnívoros
        for carnivoro in sorted(filter(lambda x: isinstance(x, Carnivoro), self.especies), 
                                key=lambda x: (x.capacidad_busqueda * x.tasa_efectividad), reverse=True):
            herbivoro_alimentado = False
            for herbivoro in filter(lambda x: isinstance(x, Herbivoro) and x.poblacion > 0, self.especies):
                if random.random() < carnivoro.capacidad_busqueda * carnivoro.tasa_efectividad:
                    comida_consumida = min(herbivoro.poblacion // 2, carnivoro.poblacion)  
                    herbivoro.morir(comida_consumido / (herbivoro.poblacion + comida_consumido))  
                    carnivoro.poblacion += comida_consumido // 2  
                    herbivoro_alimentado = True
                    break

            if not herbivoro_alimentado:
                carnivoro.morir(0.1)  

            carnivoro.morir_por_vejez()

        # Reproducción de herbívoros y carnívoros después de alimentarse
        for especie in filter(lambda x: isinstance(x, Herbivoro) or isinstance(x, Carnivoro), self.especies):
            especie.reproducirse()

    def mostrar_estadisticas(self):
        """ Muestra estadísticas del ecosistema """

        print("\nEstadísticas del ecosistema:")

        for especie in self.especies:
            print(f"{especie.nombre} ({especie.tipo}): {especie.poblacion} individuos")

    def guardar_ecosistema(self, filename='ecosistema.json'):
        """ Guarda el estado actual del ecosistema en un archivo JSON """

        with open(filename, 'w') as f:
            json.dump([es.__dict__ for es in self.especies], f)

    def cargar_ecosistema(self, filename='ecosistema.json'):
        """ Carga el estado del ecosistema desde un archivo JSON """

        try:
            with open(filename) as f:
                data = json.load(f)
                for item in data:
                    if item['tipo'] == 'planta':
                        especie = Planta(item['nombre'], item['capacidad_reproduccion'])
                    elif item['tipo'] == 'herbivoro':
                        especie = Herbivoro(item['nombre'], item['capacidad_reproduccion'], item.get('capacidad_busqueda', 0))
                    elif item['tipo'] == 'carnivoro':
                        especie = Carnivoro(item['nombre'], item['capacidad_reproduccion'], item.get('capacidad_busqueda', 0), item.get('tasa_efectividad', 0))

                    especie.poblacion = item['poblacion']
                    self.agregar_especie(especie)

                print("Ecosistema cargado exitosamente.")

        except FileNotFoundError:
            print("El archivo no fue encontrado.")