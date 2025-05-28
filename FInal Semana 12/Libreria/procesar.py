contMasc = 0
contFem = 0
datos_de_jugador = []

def procesar():
    global contMasc, contFem, datos_de_jugador
    datos_de_jugador.clear()
    contMasc = 0
    contFem = 0

    while True:
        try:
            jugadores = int(input("\nIngrese cantidad de jugadores:\t\t"))
            if jugadores <= 0:
                print("\nIngrese aunque sea un jugador.")
            else:
                print(f"La cantidad de jugadores es {jugadores}")
                for i in range(jugadores):
                    while True:
                        genero = input(f"Ingrese género del jugador {i+1} (M/F):\t").upper()
                        if genero not in ['M', 'F']:
                            print("ERROR. Ingrese 'M' para masculino o 'F' para femenino")
                        else:
                            break
                    if genero == "M":
                        contMasc += 1
                    else:
                        contFem += 1

                    while True:
                        nombre = input(f"Ingrese nombre de Jugador {i+1}:\t").strip()
                        if nombre == "":
                            print("El nombre no puede estar vacío.")
                        else:
                            break

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
                                puntaje = float(input(f"Ingrese el puntaje del nivel [0 - 500] {n + 1} de {nombre}: "))
                                if 0 <= puntaje <= 500:
                                    puntajes.append(puntaje)
                                    break
                                else:
                                    print("Introduzca valores entre 0 y 500")
                            except ValueError:
                                print("Ingrese un número válido.")

                    jugador = {
                        "nombre": nombre,
                        "genero": genero,
                        "niveles": niveles,
                        "puntajes": puntajes
                    }
                    datos_de_jugador.append(jugador)
                break
        except ValueError:
            print("ERROR. Ingrese un número válido para la cantidad de jugadores.")