# Proyecto Tateti - Algoritmo Minimax

## 📋 Descripción

Este proyecto tiene como objetivo enseñar el algoritmo **Minimax** aplicado al juego del Tateti (Tic-Tac-Toe). El proyecto está estructurado en módulos para facilitar la comprensión e implementación gradual.

## 🎯 Objetivos

- Comprender la teoría de juegos y los algoritmos de búsqueda entre adversarios
- Implementar el algoritmo Minimax  
- Repasar conceptos de recursión

## 📁 Estructura del Proyecto

```
tp-tateti/
├── tateti.py           # Formulación del juego (COMPLETO)
├── estrategias.py      # Estrategias de juego (PARA IMPLEMENTAR)
├── gui_pygame.py       # Interfaz gráfica moderna (COMPLETO)
├── main.py             # Punto de entrada de la aplicación (COMPLETO)
├── test.py             # Pruebas unitarias (COMPLETO)
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Este archivo
```

## 🔧 Componentes

### 1. `tateti.py` - Formulación del juego ✅

Este módulo contiene la **formulación** del tateti según la teoría de juegos.

### 2. `estrategias.py` - Para implementar 🔨

**TODO**: Implementar el algoritmo Minimax en este módulo.

#### Funciones a completar:

```python
def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
    ....
    """
    # TODO: Implementar algoritmo minimax
```

### 3. `main.py` - Interfaz gráfica ✅

Aplicación completa con tres modos de juego:
- **Humano vs Humano**: Dos jugadores hacen click en las casillas
- **Humano vs Máquina**: El humano juega contra la IA
- **Máquina vs Máquina**: Observa dos IAs jugando

### 4. `test.py` - Pruebas ✅

Suite de pruebas para verificar tu implementación.

## 🚀 Instalación y Ejecución

### Requisitos del Sistema

- **Python 3.10+** (recomendado)
- **Sistema operativo**: Windows, macOS, o Linux

### 1. Instalar Dependencias

#### Opción A: Usando requirements.txt (Recomendado)
```bash
python3 -m pip install -r requirements.txt
```

#### Opción B: Instalación manual
```bash
python3 -m pip install pygame>=2.6.0
```

#### Verificar la instalación
```bash
python3 -c "import pygame; print('Pygame instalado correctamente:', pygame.version.ver)"
```

### 2. Ejecutar el Juego

```bash
python3 main.py
```

### 3. Ejecutar las Pruebas

```bash
python3 test.py
```

## 📝 Guía de Implementación

### Paso 1: Primer acercamiento
1. Ejecuta `python3 main.py` y juega algunos juegos, 
   inicialmente la única estrategia implementada es la aleatoria.
2. Examina el código en `tateti.py`

### Paso 2: Implementar `estrategia_minimax` en `estrategias.py`

### Paso 3: Probar y Validar
1. Ejecuta las pruebas: `python3 test.py`

```
----------------------------------------------------------------------
Ran 18 tests in 5.515s

OK

=== RESUMEN ===
Pruebas ejecutadas: 18
Errores: 0
Fallos: 0

✅ ¡TODAS LAS PRUEBAS PASARON!
```

2. Juega contra tu IA: `python3 main.py`
3. ¿Es posible ganarle a la IA?

A partir de varias ejecuciones del algoritmo (jugando varias partidas contra la IA), observamos consistentemente que la IA nunca pierde. Si el humano llega a cometer un error, la IA puede capitalizarlo y ganar. Si ambos jugadores juegan de manera óptima, la partida termina en empate.

El Ta-Te-Ti es un juego resuelto, y se sabe que el mejor resultado posible para ambos jugadores es el empate. Como minimax garantiza juego óptimo, la IA siempre alcanza ese resultado como mínimo.

## 🔗 Bibliografía

- [Russell & Norvig - AI: A Modern Approach, Chapter 5](http://aima.cs.berkeley.edu/)
