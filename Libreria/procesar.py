contMasc = 0
contFem = 0
datos_de_jugador = []

def procesar():
    global contMasc, contFem, datos_de_jugador
    while True:
        try:
            jugadores = int(input("\nIngrese cantidad de jugadores:\t\t"))
            if jugadores <= 0:
                print("Ingrese al menos un jugador.")
            else:
                break
        except ValueError:
            print("ERROR. Ingrese un número válido.")

    print(f"\nCantidad de jugadores: {jugadores}")
    for i in range(jugadores):
        while True:
            genero = input(f"Ingrese género del jugador {i+1} (H/M):\t").upper()
            if genero not in ['H', 'M']:
                print("ERROR. Ingrese 'H' para Hombre o 'M' para Mujer")
            else:
                break

        if genero == "H":
            contMasc += 1
        else:
            contFem += 1

        nombre = input(f"Ingrese nombre del jugador {i+1}:\t")

        while True:
            try:
                niveles = int(input(f"Ingrese la cantidad de niveles superados por {nombre} (1-5): "))
                if 1 <= niveles <= 5:
                    break
                else:
                    print("Debe ser un número entre 1 y 5.")
            except ValueError:
                print("Ingrese un número válido.")

        puntajes = []
        for n in range(niveles):
            while True:
                try:
                    puntaje = float(input(f"Ingrese el puntaje del nivel {n+1} [0 - 500] de {nombre}: "))
                    if 0 <= puntaje <= 500:
                        puntajes.append(puntaje)
                        break
                    else:
                        print("Introduzca valores entre 0 y 500.")
                except ValueError:
                    print("Ingrese un número válido.")

        total_puntos = sum(puntajes)
        destacado = total_puntos >= 2000

        jugador = {
            "nombre": nombre,
            "genero": genero,
            "niveles": niveles,
            "puntajes": puntajes,
            "destacado": destacado
        }
        datos_de_jugador.append(jugador)