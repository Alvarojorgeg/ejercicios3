from clases.rally import Rally

if __name__ == "__main__":
    datos_naves = [
        {"nombre": "Cometa Veloz", "longitud": 150, "tripulantes": 5, "pasajeros": 8},
        {"nombre": "Titán del Cosmos", "longitud": 300, "tripulantes": 20, "pasajeros": 50},
        {"nombre": "GX Ultra", "longitud": 220, "tripulantes": 10, "pasajeros": 25},
        {"nombre": "GX Turbo", "longitud": 180, "tripulantes": 8, "pasajeros": 15},
        {"nombre": "Estrella Fugaz", "longitud": 120, "tripulantes": 4, "pasajeros": 6},
        {"nombre": "Nebulosa", "longitud": 400, "tripulantes": 25, "pasajeros": 100},
        {"nombre": "GX Viper", "longitud": 175, "tripulantes": 6, "pasajeros": 9},
        {"nombre": "Centella", "longitud": 110, "tripulantes": 3, "pasajeros": 4},
    ]

    rally = Rally(datos_naves)

    rally.ordenar_naves()
    rally.info_naves(["Cometa Veloz", "Titán del Cosmos"])
    rally.cinco_mas_pasajeros()
    rally.nave_mas_tripulantes()
    rally.naves_con_prefijo("GX")
    rally.naves_mas_de_seis_pasajeros()
    rally.nave_mas_pequena_y_grande()
