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
    """

    # Definimos las funciones recursivas para calcular los valores minimax de los nodos
    def MINIMAX_MAX(tateti: Tateti, estado: List[List[str]])-> Tuple[int, int]:
        # Calcula recursivamente el valor minimax
        # en un nodo MAX
    
        # Caso base: si el juego terminó, devuelve el valor del tablero
        if tateti.test_terminal(estado):
            return tateti.utilidad(estado, JUGADOR_MAX) 
    
        valor = -10000 # Un valor muy negativo que simula "-infinito"
        
        # En un nodo MAX buscamos maximizar su ganancia eligiendo el valor más alto de sus hijos (MIN)
        for accion in tateti.acciones(estado):
            #Obtener el sucesor
            sucesor = tateti.resultado(estado, accion)
            valor = max(valor, MINIMAX_MIN(tateti, sucesor))
        return valor 

    
    def MINIMAX_MIN(tateti: Tateti, estado: List[List[str]])-> Tuple[int, int]:
        # Calcula recursivamente el valor minimax
        # en un nodo MIN

        # Caso base: si el juego terminó, devuelve el valor del tablero
        if tateti.test_terminal(estado):
            return tateti.utilidad(estado, JUGADOR_MAX) 
        
        valor = 10000 # Un valor muy alto que simula "+infinito"
        
        # En un nodo MIN se busca minimizar la ganancia de MAX eligiendo el valor más bajo de sus hijos (MAX)
        for accion in tateti.acciones(estado):
            #Obtener el sucesor
            sucesor = tateti.resultado(estado, accion)
            valor = min(valor, MINIMAX_MAX(tateti, sucesor))
        return valor
    
    # Si es el turno de MAX, evalúa todas las acciones posibles y elige la que maximiza el resultado
    if tateti.jugador(estado) == JUGADOR_MAX:
        sucesores = {accion: MINIMAX_MIN(tateti, tateti.resultado(estado,accion)) 
                     for accion in tateti.acciones(estado)}
        return max(sucesores, key=sucesores.get) # Obtiene la clave (accion) con el mayor valor
    
    if tateti.jugador(estado) == JUGADOR_MIN:
        sucesores = {accion: MINIMAX_MAX(tateti, tateti.resultado(estado,accion)) 
                     for accion in tateti.acciones(estado)}
        return min(sucesores, key=sucesores.get) # Obtiene la clave (accion) con el menor valor
