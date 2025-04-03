from superclases.Piedra import Piedra

class Piramide:
    def __init__(self, cantidad):
        self.origen = [Piedra(i) for i in range(cantidad, 0, -1)]
        self.auxiliar = []
        self.destino = []

