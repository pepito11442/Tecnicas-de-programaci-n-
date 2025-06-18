import time
import Libreria.procesar as proc

puntajes_por_nivel = {
    1: {"A": 400, "E": -60},
    2: {"A": 450, "E": -70},
    3: {"A": 500, "E": -80},
    4: {"A": 550, "E": -90},
    5: {"A": 600, "E": -100}
}

def animacion(nivel_actual):
    siguiente_nivel = nivel_actual + 1
    print(f"\n Nivel {nivel_actual} => Nivel {siguiente_nivel}")
    time.sleep(1)

    for i in range(30):
        camino = "─" * i + ">"
        print("\r" + camino, end="", flush=True)
        time.sleep(0.03)

    print("\n Pasando al siguiente nivel, espere un segundo porfi :D\n")
    time.sleep(1)

# 🎮 Juego principal
def jugar():
    if not proc.datos_de_jugador:
        print("\nPrimero debes procesar jugadores.")
        return

    print("\n===== COMIENZA LA AVENTURA =====")

    for jugador in proc.datos_de_jugador:
        print(f"\nJuega {jugador['nombre']}")
        puntos = 0
        niveles_superados = 0
        acciones_usadas = set()

        for nivel in range(1, 6):
            print(f"\n NIVEL {nivel} — Un enemigo aparece ")

            try:
                accion = input("¿Qué haces? (A)taque o (E)vitar: ").strip().upper()
                if accion in ["A", "E"]:
                    acciones_usadas.add(accion)
                    puntos_nivel = puntajes_por_nivel[nivel][accion]
                    puntos += puntos_nivel

                    if accion == "A" and puntos_nivel > 0:
                        print(f"Buena, Ganaste +{puntos_nivel} puntos")
                        niveles_superados += 1
                    elif accion == "A":
                        print("Fallaste el ataque. No ganaste puntos.")
                    else:
                        print("Evitaste y fuiste al siguiente nivel")
                else:
                    print("Acción no valida. Perdiste el turno.")
            except:
                print("Error inesperado")

            if nivel < 5:
                animacion(nivel)

        jugador["puntajes"] = (puntos,)
        jugador["niveles"] = niveles_superados
        jugador["acciones_usadas"] = acciones_usadas
        jugador["destacado"] = puntos >= 2000

        print(f"\n{jugador['nombre']} consiguio {puntos} puntos y supero {niveles_superados} niveles.")
        if jugador["destacado"]:
            print("Eres especial\n")

def mostrar_destacados():
    if not proc.datos_de_jugador:
        print("\nNo hay jugadores registrados.")
        return

    print("\n===== JUGADORES DESTACADOS =====")
    encontrados = False
    for jugador in proc.datos_de_jugador:
        if jugador.get("destacado"):
            print(f"\n{jugador['nombre']}")
            print(f"Puntaje: {jugador['puntajes'][0]}")
            print(f"Niveles superados: {jugador['niveles']}")
            encontrados = True

    if not encontrados:
        print("No hay jugadores destacados")
