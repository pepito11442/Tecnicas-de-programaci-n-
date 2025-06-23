# Librería utilizada: Procesar, es aquella que guarda todos los datos que se introdujeron en la opción 1 y 3 del menú.
import Libreria.procesar as proc

# Se muestra al elegir la opción 2 del menú mostrando estadísticas más específicas según la opción que se elija.
def submenu_estadisticas():  # Define una función llamada submenu_estadisticas.
    while True:  # Crea un bucle que hace que el submenú se repita de forma indefinida hasta elegir el caso 5 para volver al menú principal.
        print("\n====== SUBMENÚ DE ESTADÍSTICAS ======")  # Imprime las opciones que tenemos disponibles.
        print("1. Total de jugadores procesados")
        print("2. Cantidad de jugadores por género")
        print("3. Jugadores DESTACADOS (más de 2000 puntos)")
        print("4. Ver todos los jugadores registrados")
        print("5. Volver al menú principal")

        # Se tiene que introducir una opción válida del 1 al 5 como nos muestra el print.
        opcion = input("Seleccione una opción: ")

        if opcion == "1":  # Si se elige la opción 1, se cuenta el total de jugadores procesados.
            total = 0
            for jugador in proc.datos_de_jugador:
                total += 1  # Se incrementa el contador por cada jugador encontrado.
            print(f"\nTotal de jugadores procesados: {total}")  # Muestra el total de jugadores encontrados.

        elif opcion == "2":  # Opción 2: muestra cuántos hombres y mujeres han sido procesados.
            print(f"\nCantidad de hombres: {proc.contMasc}")
            print(f"Cantidad de mujeres: {proc.contFem}")

        elif opcion == "3":  # Opción 3: muestra jugadores destacados.
            print("\nJugadores DESTACADOS (más de 2000 puntos):")
            i = 1  # Contador para numerar jugadores
            hay_destacados = False  # Bandera para saber si hay destacados

            for jugador in proc.datos_de_jugador: #Recorre la lista de todos los jugadores registrados.
                if jugador["destacado"]: # Verifica si el jugador es destacado.
                    hay_destacados = True # Marca que al menos un jugador destacado ha sido encontrado.
                    nombre = jugador["nombre"] # Nombre del jugador.
                    niveles = jugador["niveles"] # Niveles superados por jugador.
                    puntajes = jugador["puntajes"] # Lista de puntajes por jugador.
                    total = 0 # Inicia la variable para acumular el puntaje total.
                    for p in puntajes:  # Suma los puntajes obtenidos por jugador.
                        total += p
                    if niveles > 0:
                        promedio = total / niveles  # Calcula el promedio de puntos por nivel.
                    else:
                        promedio = 0
                    print(f"{i}. {nombre} - Niveles: {niveles}, Total: {total}, Promedio: {promedio:.2f} DESTACADO")
                    i += 1

            if not hay_destacados:  # Si no se encontró ningun destacado imprime lo que vemos abajo.
                print("No hay jugadores destacados.")

        elif opcion == "4":  # Opción 4: muestra todos los jugadores registrados con sus datos.
            print("\n=== Lista de todos los jugadores registrados ===") # Título/Encabezado que se imprime
            if proc.datos_de_jugador == []: # Revisa la lista de jugadores procesados.
                print("No hay jugadores registrados.") # Si ningun jugador está procesado imprime esto.
            else: # Si hay al menos un jugador procesado
                contador = 1 # El contador aumenta en 1 por cada jugador
                for jugador in proc.datos_de_jugador: # Recorre la lista de jugadores procesados.
                    nombre = jugador["nombre"] #Linea 58-62 muestra los datos de los jugadores procesados y cuantos son.
                    genero = jugador["genero"]
                    niveles = jugador["niveles"]
                    puntajes = jugador["puntajes"]
                    total = 0
                    for p in puntajes:
                        total += p  # Suma del puntaje total por jugador.
                    destacado = "Sí" if jugador["destacado"] else "No" #trabaja con Destacado: {destacado} mostrando si un jugador es destacado cumpiendo con el requisito de 2000 puntos o más, si no lo es simplemente dirá que No.
                    print(f"{contador}. {nombre} | Género: {genero} | Niveles: {niveles} | Puntaje total: {total} | Destacado: {destacado}")
                    contador += 1

        elif opcion == "5":  # Opción 5: sale del submenú.
            print("Volviendo al menú principal\n")
            break # Se rompen todos los bucles y nos devuelve al menú principal.

        else:  # Opción no válida
            print("Opción inválida. Intente nuevamente.") # Imprime eso y se repite el bucle mostrandonos el submenú de opciones otra vez hasta que elijamos la condición 5.
