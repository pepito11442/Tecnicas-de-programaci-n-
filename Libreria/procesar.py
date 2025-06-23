# Contadores globales para llevar el control de jugadores masculinos y femeninos
contMasc = 0
contFem = 0

# Lista vacía que almacenará los datos de cada jugador como diccionarios
datos_de_jugador = []

# Función principal para ingresar y procesar los datos de los jugadores
def procesar():
    global contMasc, contFem, datos_de_jugador  # Se indica que se usarán las variables globales

    # Bucle para asegurar que se ingrese un número válido de jugadores
    while True:
        try:
            jugadores = int(input("\nIngrese cantidad de jugadores:\t\t"))
            if jugadores <= 0:
                print("Ingrese al menos un jugador. La cantidad debe ser mayor a 0.")
            else:
                break  # Salir del bucle si la entrada es válida
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero para la cantidad de jugadores.")

    # Bucle que se repite según la cantidad de jugadores ingresada
    for i in range(jugadores):
        print(f"\n=== Datos del Jugador {i + 1} ===")

        # Validación para asegurarse de que se ingrese el género correctamente
        while True:
            genero = input(f"Ingrese género del jugador {i + 1} (H/M): ").upper()
            if genero in ['H', 'M']:
                break
            else:
                print("ERROR. Ingrese 'H' o 'M'.")

        # Se actualizan los contadores según el género
        if genero == "H":
            contMasc += 1
        else:
            contFem += 1

        # Se solicita el nombre del jugador
        nombre = input(f"Ingrese nombre del jugador {i + 1}:\t")

        # Se inicializan niveles superados y puntajes como vacíos
        niveles = 0
        puntajes = []

        # Se construye un diccionario con los datos del jugador
        jugador = {
            "nombre": nombre,
            "genero": genero,
            "niveles": niveles,
            "puntajes": puntajes,
            "destacado": False  # Aún no se evalúa si es destacado
        }

        # Se agrega el jugador a la lista principal
        datos_de_jugador.append(jugador)
