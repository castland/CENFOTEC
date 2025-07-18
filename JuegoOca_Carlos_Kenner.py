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

# falta implementar:
# Sistema de jugadores
# Lógica de dados
# Movimiento de fichas
# Efectos de casillas especiales
# Condición de victoria
 

#LOOP PRINCIPAL PARA MOSTRAR EL MENU Y EJECUTAR ACCIONES
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
    
        #AQUI VA EL RESTO DEL JUEGO DE LA OCA
        break
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
        time.sleep(2)
        limpiar_consola()


# Simulación completa de turnos con efectos de casillas especiales
jugador_1_posicion = 0
jugador_2_posicion = 0
turno = 1  # 1 = Jugador 1, 2 = Jugador 2
turnos_perdidos_j1 = 0
turnos_perdidos_j2 = 0

while jugador_1_posicion < 63 and jugador_2_posicion < 63:
    repetir_turno = False

    if turno == 1:
        if turnos_perdidos_j1 > 0:
            print(f"Jugador 1 pierde este turno. Turnos restantes: {turnos_perdidos_j1}")
            turnos_perdidos_j1 -= 1
            turno = 2
            continue
        jugador_actual = 1
        posicion = jugador_1_posicion
    else:
        if turnos_perdidos_j2 > 0:
            print(f"Jugador 2 pierde este turno. Turnos restantes: {turnos_perdidos_j2}")
            turnos_perdidos_j2 -= 1
            turno = 1
            continue
        jugador_actual = 2
        posicion = jugador_2_posicion

    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    avanzar = dado_1 + dado_2
    print(f"Turno del Jugador {jugador_actual}: Lanzó {dado_1} + {dado_2} = {avanzar}")

    posicion += avanzar

    # Si pasa de 63, retrocede lo que se pasó
    if posicion > 63:
        exceso = posicion - 63
        print(f"¡Ups! Te pasaste. Retrocedes {exceso} casilla(s).")
        posicion = 63 - exceso

    # Verificación de casillas especiales
    if posicion in ocas:
        while posicion in ocas:
            index_oca = ocas.index(posicion)
            if index_oca + 1 < len(ocas):
                nueva_posicion = ocas[index_oca + 1]
                print(f"¡Oca! Avanzas a la siguiente Oca: {nueva_posicion}")
                posicion = nueva_posicion
                dado_1 = random.randint(1, 6)
                dado_2 = random.randint(1, 6)
                avanzar = dado_1 + dado_2
                print(f"Vuelves a lanzar: {dado_1} + {dado_2} = {avanzar}")
                posicion += avanzar
            else:
                break
        repetir_turno = True

    elif posicion in laberinto:
        print("¡Laberinto! Retrocedes a la casilla 30.")
        posicion = 30

    elif posicion in pozo:
        print("¡Pozo! Pierdes 1 turno.")
        if jugador_actual == 1:
            turnos_perdidos_j1 = 1
        else:
            turnos_perdidos_j2 = 1

    elif posicion in carcel or posicion in calavera:
        nombre = "Cárcel" if posicion in carcel else "Calavera"
        print(f"¡{nombre}! Pierdes 2 turnos.")
        if jugador_actual == 1:
            turnos_perdidos_j1 = 2
        else:
            turnos_perdidos_j2 = 2

    # Actualizar posición
    if jugador_actual == 1:
        jugador_1_posicion = posicion
        print("Jugador 1 avanza a casilla", jugador_1_posicion)
    else:
        jugador_2_posicion = posicion
        print("Jugador 2 avanza a casilla", jugador_2_posicion)

    # Verificar victoria
    if posicion == 63:
        print(f"¡Jugador {jugador_actual} ha llegado exactamente a la casilla 63 y gana el juego!")
        break

    # Solo cambiar de turno si no hay repetición
    if not repetir_turno:
        turno = 2 if turno == 1 else 1