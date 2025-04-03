class Piramide:
    def __init__(self, total_piedras):
        self.piedras = total_piedras

    def resolver(self, n, origen, destino, auxiliar):
        if n == 1:
            print(f"Mover piedra de {origen} a {destino}")
        else:
            self.resolver(n - 1, origen, auxiliar, destino)
            print(f"Mover piedra de {origen} a {destino}")
            self.resolver(n - 1, auxiliar, destino, origen)
