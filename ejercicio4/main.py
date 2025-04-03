from clases.polinomio import Polinomio

if __name__ == "__main__":
    p1 = Polinomio({2: 5, 1: -3, 0: 4})  # 5x² - 3x + 4
    p2 = Polinomio({1: 2, 0: 1})         # 2x + 1

    print("Polinomio 1:", p1)
    print("Polinomio 2:", p2)

    resta = p1.restar(p2)
    print("\nResta (P1 - P2):", resta)

    cociente, resto = p1.dividir(p2)
    print("\nDivisión (P1 / P2):")
    print("Cociente:", cociente)
    print("Resto:", resto)

    p1.eliminar_termino(1)
    print("\nP1 tras eliminar término x^1:", p1)

    existe = p1.existe_termino(2)
    print("\n¿Existe término x^2 en P1?:", existe)
