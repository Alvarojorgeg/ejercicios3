class Matriz:
    def __init__(self, numeros):
        self.numeros = numeros

    def det_recursivo(self, m=None):
        if m is None:
            m = self.numeros

        if len(m) == 1:
            return m[0][0]

        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]

        det = 0
        for c in range(len(m)):
            det += ((-1) ** c) * m[0][c] * self.det_recursivo(
                [fila[:c] + fila[c+1:] for fila in m[1:]])
        return det

    def det_iterativo(self):
        m = self.numeros
        return (
            m[0][0] * m[1][1] * m[2][2] +
            m[0][1] * m[1][2] * m[2][0] +
            m[0][2] * m[1][0] * m[2][1] -
            m[0][2] * m[1][1] * m[2][0] -
            m[0][0] * m[1][2] * m[2][1] -
            m[0][1] * m[1][0] * m[2][2]
        )