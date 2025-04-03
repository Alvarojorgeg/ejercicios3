from subclases.Piramide import Piramide

def iniciar_puzzle():
    cantidad = 3  # Cambia este número para probar con más piedras
    piramide = Piramide(cantidad)
    resultado = piramide.resolver()
    print("\nPiedras en destino:")
    for piedra in resultado:
        print(piedra)