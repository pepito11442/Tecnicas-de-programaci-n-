import Libreria.procesar as proc
import Libreria.salir as salir
import Libreria.submenu as sub

def menu():
    while True:
        print("\n=========== MENÚ DE OPCIONES ===========\n")
        print("1. Procesar jugadores")
        print("2. Mostrar estadísticas")
        print("3. Salir")

        while True:
            op = input("Ingrese opción del menú: ")

            if op == "1" or op == "2" or op == "3":
                return int(op)
            else:
                print("ERROR. Opción inválida. Ingrese 1, 2 o 3.")
                print("\n=========== MENÚ DE OPCIONES ===========\n")
                print("1. Procesar jugadores")
                print("2. Mostrar estadísticas")
                print("3. Salir")

def ejecutar():
    while True:
        opcion = menu()
        match opcion:
            case 1:
                proc.procesar()
            case 2:
                sub.submenu_estadisticas()
            case 3:
                salir.salir()
            case _:
                print("Error")

ejecutar()

