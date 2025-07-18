#Juego de la Oca | Estudiantes: Carlos Carballo, Kenner Gamboa

#SIMBOLOS PARA HACER CUADROS ═, ║, ╔, ╗, ╚, ╝, ╠, ╦, ╩, ╬ 

#LISTAS DE CASILLAS ESPECIALES
oca_1 = 5
oca_2 = 9
oca_3 = 14
oca_4 = 18
oca_5 = 23
oca_6 = 27
oca_7 = 32
oca_8 = 36
oca_9 = 41
oca_10 = 45
oca_11 = 50
oca_12 = 54
oca_13 = 59

puente_1 = 6
puente_2 = 12

pozo_1 = 31
laberinto_1 = 42
carcel_1 = 56
calavera_1 = 58
jardin_de_la_oca_1 = 63

#JUGADORES
j1 = ""
j2 = ""

#IMPORTS
import os
import random
import time

os.system('cls' if os.name == 'nt' else 'clear')
while True:
    print("╔════════════════════════════╗")
    print("║       MENÚ PRINCIPAL       ║")
    print("╠════════════════════════════╣")
    print("║  1. Iniciar juego          ║")
    print("║  2. Ver Reglas del Juego   ║")
    print("║  3. Salir                  ║")
    print("╚════════════════════════════╝")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("╔═══════════════════════╗")
        print("║ Iniciando el juego... ║")
        print("╚═══════════════════════╝")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

        # Nombres de jugadores
        while True:
            print("╔═════════════════════════════╗")
            print("║ Jugador 1 Ingrese el nombre ║")
            print("╚═════════════════════════════╝")        
            j1 = input("Nombre del Jugador 1: ")
            print("╔═════════════════════════════╗")
            print("║ Jugador 2 Ingrese el nombre ║")    
            print("╚═════════════════════════════╝")
            j2 = input("Nombre del Jugador 2: ")

            j1 = j1.strip()
            j2 = j2.strip()
            os.system('cls' if os.name == 'nt' else 'clear')

            if j1 and j2 and j1 != j2:
                print("╔══════════════════════════════════════╗")
                print("║    BIENVENIDOS AL JUEGO DE LA OCA    ║")
                print("╠══════════════════════════════════════╣")
                ancho_caja = 40
                texto_j1 = "║  Jugador 1: " + j1
                texto_j2 = "║  Jugador 2: " + j2
                espacios_j1 = ancho_caja - len(texto_j1) - 1
                espacios_j2 = ancho_caja - len(texto_j2) - 1
                print(texto_j1 + " " * espacios_j1 + "║")
                print(texto_j2 + " " * espacios_j2 + "║")
                print("╚══════════════════════════════════════╝")
                input("Presiona ENTER para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                print("╔══════════════════════════════════╗")
                print("║  Nombres inválidos o duplicados. ║")
                print("║  Por favor, inténtalo de nuevo.  ║")
                print("╚══════════════════════════════════╝")
                input("Presiona ENTER para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')

        # Variables para el juego
        jugador_1_posicion = 0
        jugador_2_posicion = 0
        turno = 1
        turnos_perdidos_j1 = 0
        turnos_perdidos_j2 = 0

        # Bucle principal del juego
        while jugador_1_posicion < 63 and jugador_2_posicion < 63:
            repetir_turno = False
            os.system('cls' if os.name == 'nt' else 'clear')
            print("╔═════════════════════════════════════════════════╗")
            print("║                ESTADO DEL JUEGO                 ║")
            print("╠═════════════════════════════════════════════════╣")
            mensaje_j1 = j1 + " está en la casilla " + str(jugador_1_posicion)
            ancho_caja = 51
            espacios_j1 = ancho_caja - len(mensaje_j1) - 4
            print("║  " + mensaje_j1 + " " * espacios_j1 + "║")
            mensaje_j2 = j2 + " está en la casilla " + str(jugador_2_posicion)
            espacios_j2 = ancho_caja - len(mensaje_j2) - 4
            print("║  " + mensaje_j2 + " " * espacios_j2 + "║")
            print("╚═════════════════════════════════════════════════╝")
            input("Presiona ENTER para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

            # Determinar jugador actual
            if turno == 1:
                if turnos_perdidos_j1 > 0:
                    print("╔═════════════════════════════════════════════════╗")
                    print("║               CASILLA ESPECIAL                  ║")
                    print("╠═════════════════════════════════════════════════╣")
                    mensaje = f"{j1} pierde este turno. Turnos restantes: {turnos_perdidos_j1}"
                    ancho_caja = 51
                    espacios_totales = ancho_caja - len(mensaje) - 4
                    espacios_izq = espacios_totales // 2
                    espacios_der = espacios_totales - espacios_izq
                    print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
                    print("╚═════════════════════════════════════════════════╝")
                    input("Presiona ENTER para continuar...")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    turnos_perdidos_j1 -= 1
                    turno = 2
                    continue
                jugador_actual = 1
                posicion = jugador_1_posicion
            else:
                if turnos_perdidos_j2 > 0:
                    print("╔═════════════════════════════════════════════════╗")
                    print("║               CASILLA ESPECIAL                  ║")
                    print("╠═════════════════════════════════════════════════╣")
                    mensaje = f"{j2} pierde este turno. Turnos restantes: {turnos_perdidos_j2}"
                    ancho_caja = 51
                    espacios_totales = ancho_caja - len(mensaje) - 4
                    espacios_izq = espacios_totales // 2
                    espacios_der = espacios_totales - espacios_izq
                    print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
                    print("╚═════════════════════════════════════════════════╝")
                    input("Presiona ENTER para continuar...")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    turnos_perdidos_j2 -= 1
                    turno = 1
                    continue
                jugador_actual = 2
                posicion = jugador_2_posicion

            # Mostrar turno
            nombre = j1 if jugador_actual == 1 else j2
            print("╔═════════════════════════════════════════════════╗")
            print("║                   TURNO ACTUAL                  ║")
            print("╠═════════════════════════════════════════════════╣")
            mensaje = "Turno de " + nombre
            ancho_caja = 51
            espacios_totales = ancho_caja - len(mensaje) - 4
            espacios_izq = espacios_totales // 2
            espacios_der = espacios_totales - espacios_izq
            print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
            print("╚═════════════════════════════════════════════════╝")
            input("Presiona ENTER para lanzar los dados...")
            os.system('cls' if os.name == 'nt' else 'clear')

            # Tirar dados
            dado_1 = random.randint(1, 6)
            dado_2 = random.randint(1, 6)
            avanzar = dado_1 + dado_2
            print("╔═══════════════════════════════════════╗")
            print("║                                       ║")    
            print("║           ╔═══╗      ╔═══╗            ║")
            print("║           ║ " + str(dado_1) + " ║      ║ " + str(dado_2) + " ║            ║")
            print("║           ╚═══╝      ╚═══╝            ║")
            print("║                                       ║")
            mensaje = "Avanzas " + str(avanzar) + " espacios."
            ancho_caja = 39
            espacios_totales = ancho_caja - len(mensaje) - 2
            espacios_izq = espacios_totales // 2
            espacios_der = espacios_totales - espacios_izq
            print("║ " + " " * espacios_izq + mensaje + " " * espacios_der + " ║")
            print("╚═══════════════════════════════════════╝") 
            input("Presiona ENTER para continuar...")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            posicion += avanzar

            # Si pasa de 63, retrocede lo que se pasó
            if posicion > 63:
                exceso = posicion - 63
                print("╔═════════════════════════════════════════════════╗")
                print("║               CASILLA ESPECIAL                  ║")
                print("╠═════════════════════════════════════════════════╣")
                mensaje = f"¡Ups! Te pasaste. Retrocedes {exceso} casilla(s)."
                ancho_caja = 51
                espacios_totales = ancho_caja - len(mensaje) - 4
                espacios_izq = espacios_totales // 2
                espacios_der = espacios_totales - espacios_izq
                print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
                print("╚═════════════════════════════════════════════════╝")
                input("Presiona ENTER para continuar...")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                posicion = 63 - exceso

            # Verificación de casillas especiales
            if posicion == oca_1 or posicion == oca_2 or posicion == oca_3 or posicion == oca_4 or posicion == oca_5 or posicion == oca_6 or posicion == oca_7 or posicion == oca_8 or posicion == oca_9 or posicion == oca_10 or posicion == oca_11 or posicion == oca_12 or posicion == oca_13:
                if posicion == oca_1:
                    nueva_posicion = oca_2
                elif posicion == oca_2:
                    nueva_posicion = oca_3
                elif posicion == oca_3:
                    nueva_posicion = oca_4
                elif posicion == oca_4:
                    nueva_posicion = oca_5
                elif posicion == oca_5:
                    nueva_posicion = oca_6
                elif posicion == oca_6:
                    nueva_posicion = oca_7
                elif posicion == oca_7:
                    nueva_posicion = oca_8
                elif posicion == oca_8:
                    nueva_posicion = oca_9
                elif posicion == oca_9:
                    nueva_posicion = oca_10
                elif posicion == oca_10:
                    nueva_posicion = oca_11
                elif posicion == oca_11:
                    nueva_posicion = oca_12
                elif posicion == oca_12:
                    nueva_posicion = oca_13
                else:
                    nueva_posicion = posicion
                print("╔═════════════════════════════════════════════════╗")
                print("║               CASILLA ESPECIAL                  ║")
                print("╠═════════════════════════════════════════════════╣")
                mensaje = f"¡De oca a oca y tiro porque me toca!: {nueva_posicion}"
                ancho_caja = 51
                espacios_totales = ancho_caja - len(mensaje) - 4
                espacios_izq = espacios_totales // 2
                espacios_der = espacios_totales - espacios_izq
                print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
                print("╚═════════════════════════════════════════════════╝")
                input("Presiona ENTER para continuar...")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                posicion = nueva_posicion

                # Mostrar turno especial
                nombre_jugador = j1 if jugador_actual == 1 else j2
                mensaje = f"Turno de {nombre_jugador}"
                ancho_caja = 51
                espacios_totales = ancho_caja - len(mensaje) - 4
                espacios_izq = espacios_totales // 2
                espacios_der = espacios_totales - espacios_izq
                print("╔═════════════════════════════════════════════════╗")
                print("║                   TURNO ACTUAL                  ║")
                print("╠═════════════════════════════════════════════════╣")
                print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
                print("╚═════════════════════════════════════════════════╝")
                input("Presiona ENTER para lanzar los dados...")
                os.system('cls' if os.name == 'nt' else 'clear')

                # Volver a tirar dados
                dado_1 = random.randint(1, 6)
                dado_2 = random.randint(1, 6)
                avanzar = dado_1 + dado_2
                print("╔═══════════════════════════════════════╗")
                print("║                                       ║")    
                print("║           ╔═══╗      ╔═══╗            ║")
                print("║           ║ " + str(dado_1) + " ║      ║ " + str(dado_2) + " ║            ║")
                print("║           ╚═══╝      ╚═══╝            ║")
                print("║                                       ║")
                mensaje = "Avanzas " + str(avanzar) + " espacios."
                ancho_caja = 39
                espacios_totales = ancho_caja - len(mensaje) - 2
                espacios_izq = espacios_totales // 2
                espacios_der = espacios_totales - espacios_izq
                print("║ " + " " * espacios_izq + mensaje + " " * espacios_der + " ║")
                print("╚═══════════════════════════════════════╝") 
                input("Presiona ENTER para continuar...")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                posicion += avanzar

                if posicion > 63:
                    exceso = posicion - 63
                    print("╔═════════════════════════════════════════════════╗")
                    print("║               CASILLA ESPECIAL                  ║")
                    print("╠═════════════════════════════════════════════════╣")
                    mensaje = f"¡Ups! Te pasaste. Retrocedes {exceso} casilla(s)."
                    ancho_caja = 51
                    espacios_totales = ancho_caja - len(mensaje) - 4
                    espacios_izq = espacios_totales // 2
                    espacios_der = espacios_totales - espacios_izq
                    print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
                    print("╚═════════════════════════════════════════════════╝")
                    input("Presiona ENTER para continuar...")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    posicion = 63 - exceso

                # Verificar si cayó en otra casilla especial en el segundo tiro
                if posicion == oca_1 or posicion == oca_2 or posicion == oca_3 or posicion == oca_4 or posicion == oca_5 or posicion == oca_6 or posicion == oca_7 or posicion == oca_8 or posicion == oca_9 or posicion == oca_10 or posicion == oca_11 or posicion == oca_12 or posicion == oca_13:
                    if posicion == oca_1:
                        nueva_posicion = oca_2
                    elif posicion == oca_2:
                        nueva_posicion = oca_3
                    elif posicion == oca_3:
                        nueva_posicion = oca_4
                    elif posicion == oca_4:
                        nueva_posicion = oca_5
                    elif posicion == oca_5:
                        nueva_posicion = oca_6
                    elif posicion == oca_6:
                        nueva_posicion = oca_7
                    elif posicion == oca_7:
                        nueva_posicion = oca_8
                    elif posicion == oca_8:
                        nueva_posicion = oca_9
                    elif posicion == oca_9:
                        nueva_posicion = oca_10
                    elif posicion == oca_10:
                        nueva_posicion = oca_11
                    elif posicion == oca_11:
                        nueva_posicion = oca_12
                    elif posicion == oca_12:
                        nueva_posicion = oca_13
                    else:
                        nueva_posicion = posicion
                    print("╔═════════════════════════════════════════════════╗")
                    print("║               CASILLA ESPECIAL                  ║")
                    print("╠═════════════════════════════════════════════════╣")
                    mensaje = f"¡Oca! Avanzas a la siguiente Oca: {nueva_posicion}"
                    ancho_caja = 51
                    espacios_totales = ancho_caja - len(mensaje) - 4
                    espacios_izq = espacios_totales // 2
                    espacios_der = espacios_totales - espacios_izq
                    print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
                    print("╚═════════════════════════════════════════════════╝")
                    input("Presiona ENTER para continuar...")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    posicion = nueva_posicion
                elif posicion == puente_1 or posicion == puente_2:
                    otro_puente = puente_1 if posicion == puente_2 else puente_2
                    print("╔═════════════════════════════════════════════════╗")
                    print("║               CASILLA ESPECIAL                  ║")
                    print("╠═════════════════════════════════════════════════╣")
                    mensaje = f"¡Puente! Saltas al otro puente: {otro_puente}"
                    ancho_caja = 51
                    espacios_totales = ancho_caja - len(mensaje) - 4
                    espacios_izq = espacios_totales // 2
                    espacios_der = espacios_totales - espacios_izq
                    print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
                    print("╚═════════════════════════════════════════════════╝")
                    input("Presiona ENTER para continuar...")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    posicion = otro_puente
                elif posicion == laberinto_1:
                    print("╔═════════════════════════════════════════════════╗")
                    print("║               CASILLA ESPECIAL                  ║")
                    print("╠═════════════════════════════════════════════════╣")
                    mensaje = "¡Laberinto! Retrocedes a la casilla 30."
                    ancho_caja = 51
                    espacios_totales = ancho_caja - len(mensaje) - 4
                    espacios_izq = espacios_totales // 2
                    espacios_der = espacios_totales - espacios_izq
                    print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
                    print("╚═════════════════════════════════════════════════╝")
                    input("Presiona ENTER para continuar...")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    posicion = 30
                elif posicion == pozo_1:
                    print("╔═════════════════════════════════════════════════╗")
                    print("║               CASILLA ESPECIAL                  ║")
                    print("╠═════════════════════════════════════════════════╣")
                    mensaje = "¡Pozo! Pierdes 1 turno."
                    ancho_caja = 51
                    espacios_totales = ancho_caja - len(mensaje) - 4
                    espacios_izq = espacios_totales // 2
                    espacios_der = espacios_totales - espacios_izq
                    print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
                    print("╚═════════════════════════════════════════════════╝")
                    input("Presiona ENTER para continuar...")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if jugador_actual == 1:
                        turnos_perdidos_j1 = 1
                    else:
                        turnos_perdidos_j2 = 1
                elif posicion == carcel_1 or posicion == calavera_1:
                    nombre = "Cárcel" if posicion == carcel_1 else "Calavera"
                    print("╔═════════════════════════════════════════════════╗")
                    print("║               CASILLA ESPECIAL                  ║")
                    print("╠═════════════════════════════════════════════════╣")
                    mensaje = f"¡{nombre}! Pierdes 2 turnos."
                    ancho_caja = 51
                    espacios_totales = ancho_caja - len(mensaje) - 4
                    espacios_izq = espacios_totales // 2
                    espacios_der = espacios_totales - espacios_izq
                    print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
                    print("╚═════════════════════════════════════════════════╝")
                    input("Presiona ENTER para continuar...")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if jugador_actual == 1:
                        turnos_perdidos_j1 = 2
                    else:
                        turnos_perdidos_j2 = 2

            elif posicion == puente_1 or posicion == puente_2:
                otro_puente = puente_1 if posicion == puente_2 else puente_2
                print("╔═════════════════════════════════════════════════╗")
                print("║               CASILLA ESPECIAL                  ║")
                print("╠═════════════════════════════════════════════════╣")
                mensaje = f"¡Puente! Saltas al otro puente: {otro_puente}"
                ancho_caja = 51
                espacios_totales = ancho_caja - len(mensaje) - 4
                espacios_izq = espacios_totales // 2
                espacios_der = espacios_totales - espacios_izq
                print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
                print("╚═════════════════════════════════════════════════╝")
                input("Presiona ENTER para continuar...")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                posicion = otro_puente

            elif posicion == laberinto_1:
                print("╔═════════════════════════════════════════════════╗")
                print("║               CASILLA ESPECIAL                  ║")
                print("╠═════════════════════════════════════════════════╣")
                mensaje = "¡Laberinto! Retrocedes a la casilla 30."
                ancho_caja = 51
                espacios_totales = ancho_caja - len(mensaje) - 4
                espacios_izq = espacios_totales // 2
                espacios_der = espacios_totales - espacios_izq
                print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
                print("╚═════════════════════════════════════════════════╝")
                input("Presiona ENTER para continuar...")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                posicion = 30

            elif posicion == pozo_1:
                print("╔═════════════════════════════════════════════════╗")
                print("║               CASILLA ESPECIAL                  ║")
                print("╠═════════════════════════════════════════════════╣")
                mensaje = "¡Pozo! Pierdes 1 turno."
                ancho_caja = 51
                espacios_totales = ancho_caja - len(mensaje) - 4
                espacios_izq = espacios_totales // 2
                espacios_der = espacios_totales - espacios_izq
                print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
                print("╚═════════════════════════════════════════════════╝")
                input("Presiona ENTER para continuar...")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                if jugador_actual == 1:
                    turnos_perdidos_j1 = 1
                else:
                    turnos_perdidos_j2 = 1

            elif posicion == carcel_1 or posicion == calavera_1:
                nombre = "Cárcel" if posicion == carcel_1 else "Calavera"
                print("╔═════════════════════════════════════════════════╗")
                print("║               CASILLA ESPECIAL                  ║")
                print("╠═════════════════════════════════════════════════╣")
                mensaje = f"¡{nombre}! Pierdes 2 turnos."
                ancho_caja = 51
                espacios_totales = ancho_caja - len(mensaje) - 4
                espacios_izq = espacios_totales // 2
                espacios_der = espacios_totales - espacios_izq
                print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
                print("╚═════════════════════════════════════════════════╝")
                input("Presiona ENTER para continuar...")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                if jugador_actual == 1:
                    turnos_perdidos_j1 = 2
                else:
                    turnos_perdidos_j2 = 2

            # Actualizar posición
            if jugador_actual == 1:
                jugador_1_posicion = posicion
            else:
                jugador_2_posicion = posicion

            # Verificar victoria
            if posicion == 63:
                nombre_ganador = j1 if jugador_actual == 1 else j2
                print("╔═════════════════════════════════════════════════╗")
                print("║                 ¡FIN DEL JUEGO!                 ║")
                print("╠═════════════════════════════════════════════════╣")
                mensaje = f"¡{nombre_ganador}!"
                ancho_caja = 51
                espacios_totales = ancho_caja - len(mensaje) - 4
                espacios_izq = espacios_totales // 2
                espacios_der = espacios_totales - espacios_izq
                print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
                print("║            Llegaste a la casilla 63             ║")
                print("║                  ¡Has ganado!                   ║")
                print("╚═════════════════════════════════════════════════╝")
                input("Presiona ENTER para volver al menú principal...")
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            turno = 2 if turno == 1 else 1
            time.sleep(1)

    elif opcion == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("╔═════════════════════════════════════════════════════════╗")
        print("║             INSTRUCCIONES DEL JUEGO DE LA OCA           ║")
        print("╠═════════════════════════════════════════════════════════╣")
        print("║  1. El tablero tiene casillas numeradas del 1 al 63.    ║")
        print("║  2. Los jugadores lanzan dados y avanzan según el tiro. ║")
        print("║  3. Se gana al llegar a la casilla 63 con tirada exacta.║")
        print("║  4. Si te pasas, retrocedes los espacios sobrantes.     ║")
        print("║                                                         ║")
        print("║  Casillas especiales:                                   ║")
        print("║   'Oca': Avanza hasta la próxima Oca y tira de nuevo.   ║")
        print("║   'Puente': Salta al otro puente.                       ║")
        print("║   'Pozo': Pierdes un turno.                             ║")
        print("║   'Laberinto': Retrocedes a la casilla 30.              ║")
        print("║   'Cárcel': Pierdes dos turnos.                         ║")
        print("║   'Calavera': Pierdes dos turnos.                       ║")
        print("╚═════════════════════════════════════════════════════════╝")
        input("Presiona ENTER para volver al menú...")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif opcion == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("╔═══════════════════════════════════╗")
        print("║ Saliendo del juego. ¡Hasta luego! ║")
        print("╚═══════════════════════════════════╝")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("╔═══════════════════════════════════╗")
        print("║          Opción inválida          ║")
        print("║ selecciona una opción del 1 al 3. ║")
        print("╚═══════════════════════════════════╝")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
# FIN
