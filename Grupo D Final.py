import Libreria.procesar as proc
import Libreria.salir as salir
import Libreria.submenu as sub
import Libreria.juego as juego

def menu():
    print("\n=========== MENÚ DE OPCIONES ===========\n")
    print("1. Procesar jugadores")
    print("2. Mostrar estadísticas")
    print("3. Iniciar juego")
    print("4. Salir")

    while True:
        op = input("Ingrese opción del menú: ")
        if op in ["1", "2", "3", "4"]:
            return int(op)
        else:
            print("ERROR. Opción inválida.")
            print("\n=========== MENÚ DE OPCIONES ===========\n")
            print("1. Procesar jugadores")
            print("2. Mostrar estadísticas")
            print("3. Iniciar juego")
            print("4. Salir")

def ejecutar():
    while True:
        opcion = menu()
        if opcion == 1:
            proc.procesar()
        elif opcion == 2:
            sub.submenu_estadisticas()
        elif opcion == 3:
            juego.jugar()
        elif opcion == 4:
            salir.salir()
ejecutar()
