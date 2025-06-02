import Libreria.procesar as proc

puntajes_por_nivel = {
    1: {"A": 400, "E": 0},
    2: {"A": 450, "E": 0},
    3: {"A": 500, "E": 0},
    4: {"A": 550, "E": 0},
    5: {"A": 600, "E": 0}
}

def jugar():
    if not proc.datos_de_jugador:
        print("\nPrimero debes procesar jugadores.")
        return

    print("\n===== COMIENZA LA AVENTURA =====")

    for jugador in proc.datos_de_jugador:
        print(f"\nTurno de {jugador['nombre']}")
        puntos = 0
        niveles_superados = 0

        for nivel in range(1, 6):
            print(f"\nNivel {nivel}: Un monstruo aparece")

            accion = input("¿Qué haces? (A)taque o (E)vitar: ").upper()
            if accion in ["A", "E"]:
                puntos_nivel = puntajes_por_nivel[nivel][accion]
                puntos += puntos_nivel

                if accion == "A" and puntos_nivel > 0:
                    print(f"¡Ganaste el combate! +{puntos_nivel} puntos")
                    niveles_superados += 1
                elif accion == "A" and puntos_nivel == 0:
                    print("Fallaste el ataque. No ganaste puntos.")
                else:
                    print("Escapaste del peligro. No ganaste puntos")
            else:
                print("Acción inválida. Perdiste el turno.")

        jugador["puntajes"] = [puntos]
        jugador["niveles"] = niveles_superados
        jugador["destacado"] = puntos >= 2000

        print(f"\n{jugador['nombre']} terminó con {puntos} puntos y {niveles_superados} niveles superados.")
        if jugador["destacado"]:
            print("Felicidades eres un Heroe muy gozu")
