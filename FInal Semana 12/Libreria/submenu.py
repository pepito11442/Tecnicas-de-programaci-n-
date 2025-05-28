import Libreria.procesar as proc

def submenu_estadisticas():
    while True:
        print("\n--- SUBMENÚ ESTADÍSTICAS ---")
        print("1. Ver conteo total de jugadores por género")
        print("2. Ver estadísticas detalladas por jugador")
        print("3. Volver al menú principal")

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                print("\nConteo total de jugadores:")
                print(f"Mujeres: {proc.contFem}")
                print(f"Hombres: {proc.contMasc}")
            elif opcion == 2:
                print("\nEstadísticas por jugador:")
                for i, jugador in enumerate(proc.datos_de_jugador, start=1):
                    nombre = jugador["nombre"]
                    niveles = jugador["niveles"]
                    puntajes = jugador["puntajes"]
                    total = sum(puntajes)
                    print(f"Jugador {i}. {nombre} - Niveles: {niveles},puntaje final: {total:.2f}")
            elif opcion == 3:
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Ingrese un número válido.")