class Nave:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros

    def __str__(self):
        return (f"{self.nombre} - Longitud: {self.longitud}, "
                f"Tripulantes: {self.tripulantes}, Pasajeros: {self.pasajeros}")
