import Libreria.procesar as proc

def submenu_estadisticas():
    while True:
        print("\n====== SUBMENÚ DE ESTADÍSTICAS ======")
        print("1. Total de jugadores procesados")
        print("2. Cantidad de jugadores por género")
        print("3. Jugadores DESTACADOS (más de 2000 puntos)")
        print("4. Ver todos los jugadores registrados")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            total = 0
            for jugador in proc.datos_de_jugador:
                total = total + 1
            print(f"\nTotal de jugadores procesados: {total}")

        elif opcion == "2":
            print(f"\nCantidad de hombres: {proc.contMasc}")
            print(f"Cantidad de mujeres: {proc.contFem}")

        elif opcion == "3":
            print("\nJugadores DESTACADOS (más de 2000 puntos):")
            i = 1
            hay_destacados = False
            for jugador in proc.datos_de_jugador:
                if jugador["destacado"]:
                    hay_destacados = True
                    nombre = jugador["nombre"]
                    niveles = jugador["niveles"]
                    puntajes = jugador["puntajes"]
                    total = 0
                    for p in puntajes:
                        total = total + p
                    if niveles > 0:
                        promedio = total / niveles
                    else:
                        promedio = 0
                    print(f"{i}. {nombre} - Niveles: {niveles}, Total: {total}, Promedio: {promedio:.2f} DESTACADO")
                    i = i + 1
            if not hay_destacados:
                print("No hay jugadores destacados.")

        elif opcion == "4":
            print("\n=== Lista de todos los jugadores registrados ===")
            if proc.datos_de_jugador == []:
                print("No hay jugadores registrados.")
            else:
                contador = 1
                for jugador in proc.datos_de_jugador:
                    nombre = jugador["nombre"]
                    genero = jugador["genero"]
                    niveles = jugador["niveles"]
                    puntajes = jugador["puntajes"]
                    total = 0
                    for p in puntajes:
                        total = total + p
                    destacado = "Sí" if jugador["destacado"] else "No"
                    print(f"{contador}. {nombre} | Género: {genero} | Niveles: {niveles} | Puntaje total: {total} | Destacado: {destacado}")
                    contador = contador + 1
        elif opcion == "5":
            print("Volviendo al menú principal\n")
            break
        else:
            print("Opción inválida. Intente nuevamente.")