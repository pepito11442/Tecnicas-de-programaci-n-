import Libreria.procesar as proc
import Libreria.salir as salir
import Libreria.submenu as sub
import Libreria.juego as juego

def menu():
    print(r"""
       //\\   \\      // ||==== ||\\   || ====== ||    || ||===||    //\\  
      //  \\   \\    //  ||____ || \\  ||   ||   ||    || ||===||   //  \\ 
     //====\\   \\  //   ||     ||  \\ ||   ||   ||    || ||  \\   //====\\   
    //      \\   \\//    ||==== ||   \\||   ||   ||====|| ||   \\ //      \\
                        
                        ||==== ||==|| ==== //===   //\\
                        ||--   ||__||  ||  ||     //__\\
                        ||==== ||     ==== \\=== //    \\
    """)
    print("""\t\t\t\n=========== MENÚ DE OPCIONES ===========\n
        1. Procesar jugadores
        2. Mostrar estadísticas
        3. Iniciar juego
        4. Salir""")

    while True:
        op = input("Ingrese opción del menú: ")
        if op in ["1", "2", "3", "4"]:
            return int(op)
        else:
            print("ERROR. Opción inválida.")
            print("""\t\t\t\n=========== MENÚ DE OPCIONES ===========\n
                1. Procesar jugadores
                2. Mostrar estadísticas
                3. Iniciar juego
                4. Salir""")

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
