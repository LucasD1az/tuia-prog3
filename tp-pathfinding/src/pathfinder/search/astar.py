from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """     
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached and the frontier with the initial state
        reached = {root.state: root.cost}
        frontier = PriorityQueueFrontier()
        
        # The priority is the cost plus the heuristic
        frontier.add(root, root.cost + grid.heuristic(root))

        while not frontier.is_empty():
            node = frontier.pop()

            if grid.objective_test(node.state):
                return Solution(node, reached)

            for action in grid.actions(node.state):
                #Get successor
                successor = grid.result(node.state, action)
                #Calculate the total cost
                cost = node.cost + grid.individual_cost(node.state, action)

                if successor not in reached or cost < reached[successor]:
                    # Initialize the son node 
                    son = Node("", successor, cost, parent=node, action=action)
                    reached[successor] = cost
                    # Add the son to the frontier with the cost + the heuristic
                    frontier.add(son, cost + grid.heuristic(son))

        return NoSolution(reached)