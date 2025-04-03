from .nave import Nave

class Rally:
    def __init__(self, lista_naves):
        self.naves = [Nave(**n) for n in lista_naves]