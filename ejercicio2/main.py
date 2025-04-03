from clases.matriz import Matriz

from clases.matriz import Matriz

if __name__ == "__main__":
    numeros = [
        [4, 3, 2],
        [1, 5, 7],
        [6, 8, 9]
    ]

    matriz = Matriz(numeros)

    print("Determinante (recursivo):", matriz.det_recursivo())
    print("Determinante (iterativo):", matriz.det_iterativo())
