from superclases.Piedra import Piedra

class Piramide:
    def __init__(self, cantidad):
        self.origen = [Piedra(i) for i in range(cantidad, 0, -1)]
        self.auxiliar = []
        self.destino = []

    def mover_piedras(self, n, origen, destino, auxiliar):
        if n == 1:
            piedra = origen.pop()
            destino.append(piedra)
            print(f"Mover {piedra} de {origen} a {destino}")
        else:
            self.mover_piedras(n-1, origen, auxiliar, destino)
            self.mover_piedras(1, origen, destino, auxiliar)
            self.mover_piedras(n-1, auxiliar, destino, origen)

    def resolver(self):
        self.mover_piedras(len(self.origen), self.origen, self.destino, self.auxiliar)
        return self.destino