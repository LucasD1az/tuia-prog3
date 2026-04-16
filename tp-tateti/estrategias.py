"""
Módulo de estrategias para el juego del Tateti

Este módulo contiene las estrategias para elegir la acción a realizar.
Los alumnos deben implementar la estrategia minimax.

Por defecto, se incluye una estrategia aleatoria como ejemplo base.
"""

import random
from typing import List, Tuple
from tateti import Tateti, JUGADOR_MAX, JUGADOR_MIN

def estrategia_aleatoria(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia aleatoria: elige una acción al azar entre las disponibles.
  
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)

    Raises:
        ValueError: Si no hay acciones disponibles
    """
    acciones_disponibles = tateti.acciones(estado)
    if not acciones_disponibles:
        raise ValueError("No hay acciones disponibles")
    
    return random.choice(acciones_disponibles)

def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
    
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)
        
    Raises:
        NotImplementedError: Hasta que el alumno implemente el algoritmo
    """
    def MINIMAX_MAX(tateti: Tateti, estado: List[List[str]])-> Tuple[int, int]:
    
    if tateti.test_terminal(estado):
        return tateti.utilidad(estado, JUGADOR_MAX) 
    
    valor = -10000

    for accion in tateti.acciones(estado):
        #Obtener el sucesor
        sucesor = tateti.resultado(estado, accion)
        valor = max(valor, MINIMAX_MIN(tateti, sucesor))
        return valor 

    
    def MINIMAX_MIN(tateti: Tateti, estado: List[List[str]])-> Tuple[int, int]:
    
    if tateti.test_terminal(estado):
        return tateti.utilidad(estado, JUGADOR_MAX) 
    
    valor = 10000

    for accion in tateti.acciones(estado):
        #Obtener el sucesor
        sucesor = tateti.resultado(estado, accion)
        valor = min(valor, MINIMAX_MAX(tateti, sucesor))
        return valor
    
