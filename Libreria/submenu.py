import Libreria.procesar as proc

def submenu_estadisticas():
    while True:
        print("\n--- SUBMENÚ ESTADÍSTICAS ---")
        print("1. Ver conteo total de jugadores por género")
        print("2. Ver estadísticas detalladas por jugador")
        print("3. Ver solo jugadores destacados")
        print("4. Volver al menú principal")

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
                    promedio = total / niveles if niveles > 0 else 0
                    destacado = "DESTACADO" if jugador["destacado"] else ""
                    print(f"Jugador {i}. {nombre} - Niveles: {niveles}, Total: {total}, Promedio: {promedio:.2f} {destacado}")
            elif opcion == 3:
                print("\nJugadores DESTACADOS (más de 2000 puntos):")
                destacados = [j for j in proc.datos_de_jugador if j["destacado"]]
                if destacados:
                    for i, jugador in enumerate(destacados, start=1):
                        nombre = jugador["nombre"]
                        niveles = jugador["niveles"]
                        puntajes = jugador["puntajes"]
                        total = sum(puntajes)
                        promedio = total / niveles if niveles > 0 else 0
                        print(f"Jugador {i}. {nombre} - Niveles: {niveles}, Total: {total}, Promedio: {promedio:.2f} DESTACADO")
                else:
                    print("Ningún jugador ha destacado")
            elif opcion == 4:
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Ingrese un número válido")