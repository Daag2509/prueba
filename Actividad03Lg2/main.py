# main.py

from Ecosistema import Ecosistema
from Planta import Planta
from Herviboro import Herbivoro
from Carnivoro import Carnivoro

def main():
    ecosistema = Ecosistema()

    while True:
        print("\nMenú:")
        print("1. Agregar Especie")
        print("2. Simular Día")
        print("3. Mostrar Estadísticas")
        print("4. Guardar Ecosistema")
        print("5. Cargar Ecosistema")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la especie: ")
            tipo = input("Tipo (planta/herbivoro/carnivoro): ")
            capacidad_reproduccion = float(input("Capacidad de reproducción (0-1): "))

            if tipo == "planta":
                especie = Planta(nombre, capacidad_reproduccion)
                ecosistema.agregar_especie(especie)

            elif tipo == "herbivoro":
                capacidad_busqueda = float(input("Capacidad de búsqueda (0-1): "))
                especie = Herbivoro(nombre, capacidad_reproduccion, capacidad_busqueda)
                ecosistema.agregar_especie(especie)

            elif tipo == "carnivoro":
                capacidad_busqueda = float(input("Capacidad de búsqueda (0-1): "))
                tasa_efectividad = float(input("Tasa de efectividad (0-1): "))
                especie = Carnivoro(nombre, capacidad_reproduccion, capacidad_busqueda, tasa_efectividad)
                ecosistema.agregar_especie(especie)

            else:
                print("Tipo no válido.")

        elif opcion == "2":
            dias_simulacion = int(input("¿Cuántos días desea simular? "))
            for _ in range(dias_simulacion):
                ecosistema.simular_dia()

        elif opcion == "3":
            ecosistema.mostrar_estadisticas()

        elif opcion == "4":
            ecosistema.guardar_ecosistema()

        elif opcion == "5":
            ecosistema.cargar_ecosistema()

        elif opcion == "6":
            break

if __name__ == "__main__":
    main()