contMasc = 0
contFem = 0
datos_de_jugador = []
def procesar():
    global contMasc, contFem, datos_de_jugador
    while True:
        try:
            jugadores = int(input("\nIngrese cantidad de jugadores:\t\t"))
            if jugadores <= 0:
                print("Ingrese al menos un jugador. La cantidad debe ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero para la cantidad de jugadores.")
    for i in range(jugadores):
        print(f"\n=== Datos del Jugador {i + 1} ===")

        while True:
            genero = input(f"Ingrese género del jugador {i + 1} (H/M): ").upper()
            if genero in ['H', 'M']:
                break
            else:
                print("ERROR. Ingrese 'H' o 'M'.")

        if genero == "H":
            contMasc += 1
        else:
            contFem += 1

        nombre = input(f"Ingrese nombre del jugador {i + 1}:\t")
        niveles = 0
        puntajes = []
        jugador = {
            "nombre": nombre,
            "genero": genero,
            "niveles": niveles,
            "puntajes": puntajes,
            "destacado": False
        }
        datos_de_jugador.append(jugador)
