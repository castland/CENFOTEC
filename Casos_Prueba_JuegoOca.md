# CASOS DE PRUEBA - JUEGO DE LA OCA

## CASO DE PRUEBA 1: Victoria con tirada exacta
**Objetivo:** Validar que el jugador gana al llegar exactamente a la casilla 63

**Condiciones iniciales:**
- Jugador 1 en casilla 58
- Es el turno del Jugador 1
- Dados disponibles

**Pasos de ejecución:**
1. Jugador 1 lanza los dados
2. Obtiene suma de 5 (ejemplo: dado1=2, dado2=3)
3. Avanza de casilla 58 a casilla 63

**Resultado esperado:**
- El jugador llega exactamente a la casilla 63
- Se muestra mensaje de victoria
- El juego termina
- Se regresa al menú principal

**Estado final:** Juego terminado con Jugador 1 como ganador

---

## CASO DE PRUEBA 2: Retroceso por exceso en casilla 63
**Objetivo:** Validar que el jugador retrocede cuando se pasa de la casilla 63

**Condiciones iniciales:**
- Jugador 2 en casilla 60
- Es el turno del Jugador 2
- Dados disponibles

**Pasos de ejecución:**
1. Jugador 2 lanza los dados
2. Obtiene suma de 6 (ejemplo: dado1=4, dado2=2)
3. Avanzaría a casilla 66 (60+6)
4. Se calcula exceso: 66-63 = 3
5. Retrocede: 63-3 = 60

**Resultado esperado:**
- Se muestra mensaje "¡Ups! Te pasaste. Retrocedes 3 casilla(s)."
- Jugador 2 queda en casilla 60
- El turno pasa al siguiente jugador
- El juego continúa

**Estado final:** Jugador 2 en casilla 60, turno del Jugador 1

---

## CASO DE PRUEBA 3: Casilla especial Oca con turno adicional
**Objetivo:** Validar el comportamiento de las casillas Oca (turno adicional)

**Condiciones iniciales:**
- Jugador 1 en casilla 1
- Es el turno del Jugador 1
- Dados disponibles

**Pasos de ejecución:**
1. Jugador 1 lanza los dados
2. Obtiene suma de 4 (ejemplo: dado1=1, dado2=3)
3. Avanza a casilla 5 (Oca)
4. Se activa efecto Oca: avanza a siguiente Oca (casilla 9)
5. Se muestra mensaje "¡De oca a oca y tiro porque me toca!: 9"
6. Jugador 1 obtiene turno adicional
7. Lanza dados nuevamente
8. Obtiene suma de 3 y avanza a casilla 12

**Resultado esperado:**
- Jugador 1 avanza automáticamente de casilla 5 a casilla 9
- Se muestra mensaje de Oca
- Jugador 1 mantiene el turno y lanza dados de nuevo
- Avanza 3 casillas más (9+3=12)
- El turno pasa al Jugador 2

**Estado final:** Jugador 1 en casilla 12, turno del Jugador 2
