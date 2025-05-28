import Libreria.procesar as proc
import Libreria.submenu as rep
import Libreria.salir as Salir

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
            rep.submenu_estadisticas()
        elif opcion == 3:
            Salir.salir()

if __name__ == "__main__":
    ejecutar()
