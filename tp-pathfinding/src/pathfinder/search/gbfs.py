from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        
        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Apply objective test
        if grid.objective_test(root.state):
            return Solution(root, reached)

        # Initialize frontier as a priority queue with the heuristic
        frontier = PriorityQueueFrontier()

        # In GBFS the priority is the heuristic
        frontier.add(root, grid.heuristic(root))

        while not frontier.is_empty():
            node = frontier.pop()

            # Apply objective test
            if grid.objective_test(node.state):
                return Solution(node, reached)

            for action in grid.actions(node.state):
                # Get the successor
                successor = grid.result(node.state, action)
                cost = node.cost + grid.individual_cost(node.state, action)

                if successor not in reached or cost < reached[successor]:
                    son = Node("", successor, cost, parent=node, action=action)
                    reached[successor] = cost

                    # The son is added to the frontier with its heuristic
                    frontier.add(son, grid.heuristic(son))

        return NoSolution(reached)