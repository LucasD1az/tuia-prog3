from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search"""
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Aplicar test objetivo inicial
        if grid.objective_test(root.state):
            return Solution(root, reached)

        # Inicializar frontera como cola de prioridad usando h(n)
        frontier = PriorityQueueFrontier()
        # En GBFS la prioridad es solo la heurística: f(n) = h(n)
        frontier.add(root, grid.heuristic(root.state))

        while not frontier.is_empty():
            node = frontier.pop()

            if grid.objective_test(node.state):
                return Solution(node, reached)

            for action in grid.actions(node.state):
                successor = grid.result(node.state, action)
                cost = node.cost + grid.individual_cost(node.state, action)

                if successor not in reached:
                    son = Node("", successor, cost, parent=node, action=action)
                    reached[successor] = cost
                    # Se agrega a la frontera priorizando por la distancia estimada al objetivo
                    frontier.add(son, grid.heuristic(successor))

        return NoSolution(reached)