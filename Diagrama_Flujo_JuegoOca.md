# DIAGRAMA DE FLUJO - JUEGO DE LA OCA

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
