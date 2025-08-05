# DIAGRAMA DE FLUJO - JUEGO DE LA OCA

```
                    [INICIO]
                        |
                   [Mostrar Menú]
                        |
                   [Leer Opción]
                        |
            ┌───────────┼───────────┐
            │           │           │
         [1]│        [2]│        [3]│
    [Iniciar Juego] [Reglas]   [Salir]
            │           │           │
            │    [Mostrar Reglas]   │
            │           │           │
            │    [Volver Menú] ─────┘
            │                       │
    [Ingresar Nombres]              │
            │                       │
    [Inicializar Variables]         │
            │                       │
    ┌─── [Mostrar Estado] ──────────┘
    │       │
    │   [¿Turno Perdido?] ──── SÍ ──┐
    │       │                       │
    │      NO                   [Decrementar]
    │       │                   [Cambiar Turno]
    │   [Mostrar Turno]              │
    │       │                       │
    │   [¿Presiona Q?] ──── SÍ ──── [SALIR]
    │       │
    │      NO
    │       │
    │   [Tirar Dados]
    │       │
    │   [Calcular Nueva Posición]
    │       │
    │   [¿Posición > 63?] ──── SÍ ──┐
    │       │                       │
    │      NO                   [Retroceder]
    │       │                   [Pos = 63-Exceso]
    │   [Verificar Casilla]          │
    │       │ ──────────────────────┘
    │       │
    │   ┌───┼───┐
    │   │   │   │
    │ [Oca] │ [Otras Especiales]
    │   │   │   │
    │ [Avanzar] [Aplicar Efecto]
    │ [Turno Extra] [Perder Turnos]
    │   │   │   │
    │   └───┼───┘
    │       │
    │   [¿Posición = 63?] ──── SÍ ──── [VICTORIA]
    │       │                           │
    │      NO                      [Mostrar Ganador]
    │       │                           │
    │   [Cambiar Turno]                 │
    │       │                           │
    └───────┘                      [Volver Menú]
                                        │
                                   [FIN PARTIDA]
```

## DECISIONES CLAVE DEL FLUJO:

### 1. **Validación de Entrada de Menú**
- Opciones válidas: 1, 2, 3
- Manejo de opciones inválidas con mensaje de error

### 2. **Control de Turnos Perdidos**
- Verificación al inicio de cada turno
- Decrementar contador y saltar turno si > 0

### 3. **Validación de Posición Final**
- Si posición > 63: retroceder (63 - exceso)
- Si posición = 63: victoria
- Si posición < 63: continuar juego

### 4. **Procesamiento de Casillas Especiales**
```
Oca (5,9,14,18,23,27,32,36,41,45,50,54,59):
├── Avanzar a siguiente Oca
└── Otorgar turno adicional

Puente (6,12):
└── Saltar al otro puente

Pozo (31):
└── Perder 1 turno

Laberinto (42):
└── Retroceder a casilla 30

Cárcel/Calavera (56,58):
└── Perder 2 turnos
```

### 5. **Condición de Victoria**
- Llegar exactamente a casilla 63
- Mostrar mensaje de ganador
- Terminar partida y volver al menú