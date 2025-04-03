from .piramide import Piramide

class Juego:
    def __init__(self, num_piedras):
        self.piramide = Piramide(num_piedras)

    def iniciar(self):
        print("Empieza el puzzle...")
        self.piramide.resolver(self.piramide.piedras, "Columna Inicial", "Columna Final", "Columna Auxiliar")
        print("Puzzle terminado.")
