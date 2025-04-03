class Polinomio:
    def __init__(self, terminos):
        self.terminos = terminos  # {exponente: coeficiente}

    def restar(self, otro):
        resultado = self.terminos.copy()
        for exp, coef in otro.terminos.items():
            resultado[exp] = resultado.get(exp, 0) - coef
        return Polinomio({e: c for e, c in resultado.items() if c != 0})

    def dividir(self, otro):
        dividendo = self.terminos.copy()
        divisor = otro.terminos
        cociente = {}

        grado_divisor = max(divisor)
        coef_divisor = divisor[grado_divisor]

        while dividendo and max(dividendo) >= grado_divisor:
            grado = max(dividendo) - grado_divisor
            coef = dividendo[max(dividendo)] / coef_divisor
            cociente[grado] = coef

            for exp, val in divisor.items():
                dividendo[exp + grado] = dividendo.get(exp + grado, 0) - val * coef
                if abs(dividendo[exp + grado]) < 1e-10:
                    del dividendo[exp + grado]

        return Polinomio(cociente), Polinomio(dividendo)

    def eliminar_termino(self, exponente):
        if exponente in self.terminos:
            del self.terminos[exponente]

    def existe_termino(self, exponente):
        return exponente in self.terminos

    def __str__(self):
        terminos_ordenados = sorted(self.terminos.items(), reverse=True)
        return ' + '.join(f"{coef}x^{exp}" if exp != 0 else f"{coef}"
                          for exp, coef in terminos_ordenados).replace('+ -', '- ')
