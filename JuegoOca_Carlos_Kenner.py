#Juego de la Oca | Estudiantes: Carlos Carballo, Kenner Gamboa

#SIMBOLOS PARA HACER CUADROS ═, ║, ╔, ╗, ╚, ╝, ╠, ╦, ╩, ╬ 

#IMPORTAR LIBRERIAS
import os
import random
import time

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
    print("║   'Cárcel': Piedes dos turnos.                          ║")
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
        os.system('cls' if os.name == 'nt' else 'clear')
        print("╔═══════════════════════╗")
        print("║ Iniciando el juego... ║")
        print("╚═══════════════════════╝")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    
        #AQUI VA EL RESTO DEL JUEGO DE LA OCA
        break
    elif opcion == '2':
        os.system('cls' if os.name == 'nt' else 'clear') 
        mostrar_instrucciones()
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
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')