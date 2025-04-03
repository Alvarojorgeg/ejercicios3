from .nave import Nave

class Rally:
    def __init__(self, lista_naves):
        self.naves = [Nave(**n) for n in lista_naves]

    def ordenar_naves(self):
        self.naves.sort(key=lambda x: (x.nombre, -x.longitud))
        print("Naves ordenadas (nombre ascendente y longitud descendente):")
        for nave in self.naves:
            print(nave)

    def info_naves(self, nombres):
        print("\nInformación específica de naves pedidas:")
        for nave in self.naves:
            if nave.nombre in nombres:
                print(nave)

    def cinco_mas_pasajeros(self):
        top5 = sorted(self.naves, key=lambda x: -x.pasajeros)[:5]
        print("\nCinco naves con más pasajeros:")
        for nave in top5:
            print(nave)

    def nave_mas_tripulantes(self):
        nave_max = max(self.naves, key=lambda x: x.tripulantes)
        print("\nNave con más tripulantes:")
        print(nave_max)

    def naves_con_prefijo(self, prefijo):
        print(f"\nNaves que empiezan por '{prefijo}':")
        for nave in self.naves:
            if nave.nombre.startswith(prefijo):
                print(nave)

    def naves_mas_de_seis_pasajeros(self):
        print("\nNaves con seis o más pasajeros:")
        for nave in self.naves:
            if nave.pasajeros >= 6:
                print(nave)

    def nave_mas_pequena_y_grande(self):
        mas_pequena = min(self.naves, key=lambda x: x.longitud)
        mas_grande = max(self.naves, key=lambda x: x.longitud)
        print("\nNave más pequeña:")
        print(mas_pequena)
        print("Nave más grande:")
        print(mas_grande)
