import time
import Libreria.procesar as proc  # Importa el módulo 'procesar' desde la carpeta 'Libreria'

# Diccionario que almacena los puntajes por nivel.
# Cada nivel tiene un puntaje asociado según si el jugador elige Atacar (A) o Evitar (E)
puntajes_por_nivel = {
    1: {"A": 400, "E": -60},
    2: {"A": 450, "E": -70},
    3: {"A": 500, "E": -80},
    4: {"A": 550, "E": -90},
    5: {"A": 600, "E": -100}
}

# Función que muestra una animación de transición entre niveles
def animacion(nivel_actual):
    siguiente_nivel = nivel_actual + 1
    print(f"\n Nivel {nivel_actual} => Nivel {siguiente_nivel}")
    time.sleep(0.3)  # Espera 0.3 segundos

    # Muestra una animación de flecha moviéndose
    for i in range(55):
        camino = "-" * i + ">"
        print("\r" + camino, end="")  # Imprime en la misma línea
        time.sleep(0.025)

    print("\n Pasando al siguiente nivel, espere un segundo porfi :D\n")
    time.sleep(0.3)

# Función principal del juego que recorre a cada jugador y los hace jugar 5 niveles
def jugar():
    # Verifica si hay jugadores procesados
    if not proc.datos_de_jugador:
        print("\nPrimero debes procesar jugadores.")
        return

    print("\n===== COMIENZA LA AVENTURA =====")

    # Itera por cada jugador registrado
    for jugador in proc.datos_de_jugador:
        print(f"\nTurno de {jugador['nombre']}")
        puntos = 0  # Puntos acumulados por el jugador
        niveles_superados = 0  # Contador de niveles superados
        acciones_usadas = set()  # Conjunto para guardar acciones únicas realizadas

        # Itera por los niveles del 1 al 5
        for nivel in range(1, 6):
            print(f"\n NIVEL {nivel} Un enemigo aparece ")

            try:
                # Pide al jugador una acción: Atacar o Evitar
                accion = input("¿Qué haces? (A)taque o (E)vitar: ").strip().upper()
                if accion in ["A", "E"]:
                    acciones_usadas.add(accion)  # Guarda la acción usada
                    puntos_nivel = puntajes_por_nivel[nivel][accion]  # Obtiene el puntaje correspondiente
                    puntos += puntos_nivel  # Suma el puntaje al total

                    # Si eligió atacar y ganó puntos, venció al monstruo
                    if accion == "A" and puntos_nivel > 0:
                        print(f"""
                        Buena le ganaste al mounstruo
                        Ganaste +{puntos_nivel} puntos""")
                        niveles_superados += 1  # Suma nivel superado

                    # Si atacó pero no obtuvo puntos (falló)
                    elif accion == "A":
                        print("Fallaste el ataque. No ganaste puntos.")

                    # Si evitó el combate, pierde puntos
                    else:
                        print(f"""
                        Evitaste y fuiste al siguiente nivel
                        Pero pierdes {puntos_nivel} puntos """)
                else:
                    print("Acción no valida. Perdiste el turno.")
            except:
                print("Error inesperado")

            # Si no es el último nivel, muestra la animación de transición
            if nivel < 5:
                animacion(nivel)

        # Almacena los datos del jugador
        jugador["puntajes"] = (puntos,)  # Tupla con el puntaje total
        jugador["niveles"] = niveles_superados
        jugador["acciones_usadas"] = acciones_usadas  # Conjunto con las acciones usadas
        jugador["destacado"] = puntos >= 2000  # Marca si el jugador es "destacado"

        # Muestra resumen del jugador
        print(f"\n{jugador['nombre']} consiguio {puntos} puntos y supero {niveles_superados} niveles.")
        if jugador["destacado"]:
            print("Eres especial\n")

# Función para mostrar los jugadores destacados (puntaje >= 2000)
def mostrar_destacados():
    # Verifica si hay jugadores registrados
    if not proc.datos_de_jugador:
        print("\nNo hay jugadores registrados.")
        return

    print("\n===== JUGADORES DESTACADOS =====")
    encontrados = False  # Bandera para saber si se encontró algún destacado

    # Recorre la lista de jugadores
    for jugador in proc.datos_de_jugador:
        if jugador.get("destacado"):
            print(f"\n{jugador['nombre']}")
            print(f"Puntaje: {jugador['puntajes'][0]}")
            print(f"Niveles superados: {jugador['niveles']}")
            encontrados = True

    if not encontrados:
        print("No hay jugadores destacados")
