from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        # 1. Definimos la meta para calcular la heurística
        goal = grid.end
        
        # 2. Nodo raíz
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # 3. Función interna para la Heurística (Distancia de Manhattan)
        def h(pos):
            return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

        reached = {root.state: root.cost}
        frontier = PriorityQueueFrontier()
        
        # Prioridad f(n) = g(n) + h(n)
        frontier.add(root, root.cost + h(root.state))

        while not frontier.is_empty():
            node = frontier.pop()

            if grid.objective_test(node.state):
                return Solution(node, reached)

            for action in grid.actions(node.state):
                successor = grid.result(node.state, action)
                cost = node.cost + grid.individual_cost(node.state, action)

                if successor not in reached or cost < reached[successor]:
                    son = Node("", successor, cost, parent=node, action=action)
                    reached[successor] = cost
                    # f(n) = g(n) + h(n)
                    frontier.add(son, cost + h(successor))

        return NoSolution(reached)