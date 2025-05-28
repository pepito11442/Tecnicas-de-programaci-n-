contMasc = 0
contFem = 0
contTotalJug = 0
cantMascMayDosMil = 0
acumTotalPuntos = 0
acumPuntosFem = 0

def Salir():
    print("Gracias por jugar, vuelve pronto..!")

def Reportar():
    print("\n=========== REPORTE DE ESTADÍSTICAS ===========\n")
    print("Total de jugadores:\t", contTotalJug)
    print("Jugadores femeninos:\t", contFem)
    print("Jugadores masculinos:\t", contMasc)
    print("Hombres con más de 2000 puntos:\t", cantMascMayDosMil)
    print("Total de puntos acumulados:\t", acumTotalPuntos)
    print("Total de puntos de jugadoras:\t", acumPuntosFem)

def Procesar():
    global contMasc, contFem, contTotalJug, cantMascMayDosMil, acumTotalPuntos, acumPuntosFem
    
    while True:
        genero = input("Ingrese género del jugador (M/F):\t").upper()
        if genero not in ['M', 'F']:
            print("ERROR. Ingrese 'M' para masculino o 'F' para femenino")
        else:
            break

    while True:
        cant_niveles = int(input("Ingrese la cantidad de niveles superados:\t"))
        if cant_niveles <= 0:
            print("ERROR. La cantidad de niveles debe ser mayor a 0")
        else:
            break
    
    puntos_totales = 0
    for i in range(cant_niveles):
        while True:
            puntos_nivel = int(input(f"Ingrese los puntos obtenidos en el nivel {i+1}: "))
            if puntos_nivel < 0:
                print("ERROR. Los puntos no pueden ser negativos")
            else:
                break
        puntos_totales += puntos_nivel

    contTotalJug += 1
    acumTotalPuntos += puntos_totales

    if genero == 'M':
        contMasc += 1
        if puntos_totales > 2000:
            cantMascMayDosMil += 1
    else:
        contFem += 1
        acumPuntosFem += puntos_totales
    
    print("\n=========== REPORTE DEL JUGADOR ============\n")
    print("Total de puntos obtenidos:\t", puntos_totales)

def Menu():
    print("\n=========== MENÚ DE OPCIONES ===========\n")
    print("1. Procesar jugador")
    print("2. Mostrar estadísticas")
    print("3. Salir")

    while True:
        opcion = int(input("Seleccione una opción del menú:\t"))
        if opcion not in [1, 2, 3]:
            print("ERROR. Opción inválida, intente nuevamente")
        else:
            break
    
    match opcion:
        case 1: Procesar()
        case 2: Reportar()
        case 3:
            while True:
                rpta = input("¿Desea salir del programa? (S/N): ").strip().upper()
                if rpta not in ['S', 'N']:
                    print("ERROR. Responda con 'S' para sí o 'N' para no")
                else:
                    break
            if rpta == 'S':
                Salir()
            else:
                Menu()

    return opcion

def Ejecutor():
    while True:
        opcion = Menu()
        if opcion == 3:
            break

Ejecutor()
