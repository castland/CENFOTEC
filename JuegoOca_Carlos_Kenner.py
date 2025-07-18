#Juego de la Oca | Estudiantes: Carlos Carballo, Kenner Gamboa

#SIMBOLOS PARA HACER CUADROS ═, ║, ╔, ╗, ╚, ╝, ╠, ╦, ╩, ╬ 

#IMPORTAR LIBRERIAS
import os
import random
import time

#LIMPIAR CONSOLA
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

#MOSTRAR MENU DEL JUEGO
def mostrar_menu():
    print("╔════════════════════════════╗")
    print("║       MENÚ PRINCIPAL       ║")
    print("╠════════════════════════════╣")
    print("║  1. Iniciar juego          ║")
    print("║  2. Ver Reglas del Juego   ║")
    print("║  3. Salir                  ║")
    print("╚════════════════════════════╝")

#MOSTRAR INSTRUCCIONES DEL JUEGO
def mostrar_instrucciones():
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

#LISTAS DE CASILLAS ESPECIALES
ocas = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59]
puentes = [6, 12]
pozo = [31]
laberinto = [42]
carcel = [56]
calavera = [58]
jardin_de_la_oca = [63]

#JUGADORES
j1 = ""
j2 = ""

#DADOS
dado_1 = random.randint(1, 6)
dado_2 = random.randint(1, 6)
avanzar = dado_1 + dado_2

#JUGADORES
def nombre_jugadores():
    global j1, j2

    limpiar_consola()
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
        limpiar_consola()

        if j1 and j2 and j1 != j2:
            print("╔══════════════════════════════════════╗")
            print("║    BIENVENIDOS AL JUEGO DE LA OCA    ║")
            print("╠══════════════════════════════════════╣")
            # Calcular espacios necesarios para alinear la caja
            ancho_caja = 40  # Espacios en la caja
            texto_j1 = "║  Jugador 1: " + j1
            texto_j2 = "║  Jugador 2: " + j2
            espacios_j1 = ancho_caja - len(texto_j1) - 1  # -1 por el ║ final
            espacios_j2 = ancho_caja - len(texto_j2) - 1  # -1 por el ║ final
            print(texto_j1 + " " * espacios_j1 + "║")
            print(texto_j2 + " " * espacios_j2 + "║")
            print("╚══════════════════════════════════════╝")
            input("Presiona ENTER para continuar...")
            limpiar_consola()
            break
        else:
            print("╔══════════════════════════════════╗")
            print("║  Nombres inválidos o duplicados. ║")
            print("║  Por favor, inténtalo de nuevo.  ║")
            print("╚══════════════════════════════════╝")
            input("Presiona ENTER para continuar...")
            limpiar_consola()

# TIRAR DADOS
def tirar_dados():
    global dado_1, dado_2, avanzar
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
    ancho_caja = 39  # Ancho total de la caja
    espacios_totales = ancho_caja - len(mensaje) - 2  # -2 por los ║ a cada lado
    espacios_izq = espacios_totales // 2
    espacios_der = espacios_totales - espacios_izq
    
    print("║ " + " " * espacios_izq + mensaje + " " * espacios_der + " ║")
    print("╚═══════════════════════════════════════╝") 
    input("Presiona ENTER para continuar...")
    time.sleep(1)
    limpiar_consola()

# MOSTRAR ESTADO DEL JUEGO
def mostrar_estado(jugador_1_posicion, jugador_2_posicion):
    print("╔═════════════════════════════════════════════════╗")
    print("║                ESTADO DEL JUEGO                 ║")
    print("╠═════════════════════════════════════════════════╣")
    
    # Calcular espacios para el jugador 1
    mensaje_j1 = j1 + " está en la casilla " + str(jugador_1_posicion)
    ancho_caja = 51
    espacios_j1 = ancho_caja - len(mensaje_j1) - 4  # -4 por los ║ y espacios
    print("║  " + mensaje_j1 + " " * espacios_j1 + "║")
    
    # Calcular espacios para el jugador 2
    mensaje_j2 = j2 + " está en la casilla " + str(jugador_2_posicion)
    espacios_j2 = ancho_caja - len(mensaje_j2) - 4
    print("║  " + mensaje_j2 + " " * espacios_j2 + "║")
    
    print("╚═════════════════════════════════════════════════╝")
    input("Presiona ENTER para continuar...")
    limpiar_consola()

# MOSTRAR MENSAJE DE CASILLA ESPECIAL
def mostrar_mensaje_especial(mensaje):
    print("╔═════════════════════════════════════════════════╗")
    print("║               CASILLA ESPECIAL                  ║")
    print("╠═════════════════════════════════════════════════╣")
    
    # Calcular espacios para centrar el mensaje
    ancho_caja = 51
    espacios_totales = ancho_caja - len(mensaje) - 4  # -4 por los ║ y espacios
    espacios_izq = espacios_totales // 2
    espacios_der = espacios_totales - espacios_izq
    
    print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
    print("╚═════════════════════════════════════════════════╝")
    input("Presiona ENTER para continuar...")
    time.sleep(1)
    limpiar_consola()

# MOSTRAR TURNO DEL JUGADOR
def mostrar_turno(jugador):
    nombre = j1 if jugador == 1 else j2
    print("╔═════════════════════════════════════════════════╗")
    print("║                  TURNO ACTUAL                   ║")
    print("╠═════════════════════════════════════════════════╣")
    
    # Calcular espacios para centrar el mensaje
    mensaje = "Turno de " + nombre
    ancho_caja = 51
    espacios_totales = ancho_caja - len(mensaje) - 4
    espacios_izq = espacios_totales // 2
    espacios_der = espacios_totales - espacios_izq
    
    print("║" + " " * (espacios_izq + 2) + mensaje + " " * espacios_der + "║")
    print("╚═════════════════════════════════════════════════╝")
    input("Presiona ENTER para lanzar los dados...")
    limpiar_consola()

# LOGICA DEL JUEGO
def logica_juego():
    global j1, j2, dado_1, dado_2, avanzar
    
    # Variables para el juego
    jugador_1_posicion = 0
    jugador_2_posicion = 0
    turno = 1  # 1 = Jugador 1, 2 = Jugador 2
    turnos_perdidos_j1 = 0
    turnos_perdidos_j2 = 0
    
    # Bucle principal del juego
    while jugador_1_posicion < 63 and jugador_2_posicion < 63:
        repetir_turno = False
        limpiar_consola()
        
        # Mostrar estado actual del juego
        mostrar_estado(jugador_1_posicion, jugador_2_posicion)
        
        # Determinar jugador actual
        if turno == 1:
            if turnos_perdidos_j1 > 0:
                mostrar_mensaje_especial(f"{j1} pierde este turno. Turnos restantes: {turnos_perdidos_j1}")
                turnos_perdidos_j1 -= 1
                turno = 2
                continue
            jugador_actual = 1
            posicion = jugador_1_posicion
        else:
            if turnos_perdidos_j2 > 0:
                mostrar_mensaje_especial(f"{j2} pierde este turno. Turnos restantes: {turnos_perdidos_j2}")
                turnos_perdidos_j2 -= 1
                turno = 1
                continue
            jugador_actual = 2
            posicion = jugador_2_posicion
        
        # Mostrar de quién es el turno
        mostrar_turno(jugador_actual)
        
        # Tirar dados
        tirar_dados()
        posicion += avanzar
        
        # Si pasa de 63, retrocede lo que se pasó
        if posicion > 63:
            exceso = posicion - 63
            mostrar_mensaje_especial(f"¡Ups! Te pasaste. Retrocedes {exceso} casilla(s).")
            posicion = 63 - exceso
        
        # Verificación de casillas especiales
        if posicion in ocas:
            while posicion in ocas:
                index_oca = ocas.index(posicion)
                if index_oca + 1 < len(ocas):
                    nueva_posicion = ocas[index_oca + 1]
                    mostrar_mensaje_especial(f"¡Oca! Avanzas a la siguiente Oca: {nueva_posicion}")
                    posicion = nueva_posicion
                    
                    # Volver a tirar dados
                    mostrar_turno(jugador_actual)
                    tirar_dados()
                    posicion += avanzar
                else:
                    break
            repetir_turno = True
        
        elif posicion in puentes:
            # Encontrar el otro puente
            otro_puente = puentes[0] if posicion == puentes[1] else puentes[1]
            mostrar_mensaje_especial(f"¡Puente! Saltas al otro puente: {otro_puente}")
            posicion = otro_puente
        
        elif posicion in laberinto:
            mostrar_mensaje_especial("¡Laberinto! Retrocedes a la casilla 30.")
            posicion = 30
        
        elif posicion in pozo:
            mostrar_mensaje_especial("¡Pozo! Pierdes 1 turno.")
            if jugador_actual == 1:
                turnos_perdidos_j1 = 1
            else:
                turnos_perdidos_j2 = 1
        
        elif posicion in carcel or posicion in calavera:
            nombre = "Cárcel" if posicion in carcel else "Calavera"
            mostrar_mensaje_especial(f"¡{nombre}! Pierdes 2 turnos.")
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
            limpiar_consola()
            break
        
        # Solo cambiar de turno si no hay repetición
        if not repetir_turno:
            turno = 2 if turno == 1 else 1
        
        # Pausa entre turnos
        time.sleep(1)

#LOOP PRINCIPAL PARA MOSTRAR EL MENU Y EJECUTAR El JUEGO
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        limpiar_consola()
        print("╔═══════════════════════╗")
        print("║ Iniciando el juego... ║")
        print("╚═══════════════════════╝")
        time.sleep(2)
        limpiar_consola()
        nombre_jugadores()
        logica_juego()       
    elif opcion == '2':
        limpiar_consola() 
        mostrar_instrucciones()
        input("Presiona ENTER para volver al menú...")
        limpiar_consola()
    elif opcion == '3':
        limpiar_consola()
        print("╔═══════════════════════════════════╗")
        print("║ Saliendo del juego. ¡Hasta luego! ║")
        print("╚═══════════════════════════════════╝")
        time.sleep(2)
        limpiar_consola()
        break
    else:
        limpiar_consola()
        print("╔═══════════════════════════════════╗")
        print("║          Opción inválida          ║")
        print("║ selecciona una opción del 1 al 3. ║")
        print("╚═══════════════════════════════════╝")
        time.sleep(3)
        limpiar_consola()
# FIN