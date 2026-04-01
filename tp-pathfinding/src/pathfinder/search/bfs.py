from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True
        
        # Apply objective test
        if grid.objective_test(root.state):
            return Solution(root, reached)

        # Initialize frontier with the root node
        frontier = QueueFrontier()
        frontier.add(root)

        while not frontier.is_empty():
            node = frontier.remove()

            for action in grid.actions(node.state):
                # Get the successor
                successor = grid.result(node.state, action)
                
                # Check if the successor is reached
                if successor in reached:
                    continue

                # Initialize the son node
                son = Node(
                    "",
                    successor,
                    cost=node.cost + grid.individual_cost(node.state, action),
                    parent=node,
                    action=action,
                )
                
                # Apply objective test
                if grid.objective_test(successor):
                    return Solution(son, reached)
                
                # Mark the successor as reached
                reached[successor] = True
                

                frontier.add(son)

        return NoSolution(reached)
