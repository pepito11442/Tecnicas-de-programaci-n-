import Libreria.procesar as proc
import Libreria.salir as salir
import Libreria.submenu as sub

def menu():
    print("\n=========== MENÚ DE OPCIONES ===========\n")
    print("1. Procesar jugadores")
    print("2. Mostrar estadísticas")
    print("3. Salir")

    while True:
        try:
            op = int(input("Ingrese opción del menú: "))
            if op in [1, 2, 3]:
                return op
            else:
                print("ERROR. Opción inválida.")
        except ValueError:
            print("ERROR. Ingrese un número.")

def ejecutar():
    while True:
        opcion = menu()
        if opcion == 1:
            proc.procesar()
        elif opcion == 2:
            sub.submenu_estadisticas()
        elif opcion == 3:
            salir.salir()
            break

ejecutar()
