from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

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
        

        # Initialize frontier with the root node
        frontier = PriorityQueueFrontier()
        frontier.add(root, root.cost)

        while not frontier.is_empty():
            
            node = frontier.pop()

            if grid.objective_test(node.state):
                return Solution(node, reached)
            
            for action in grid.actions(node.state):
                #Get successor
                successor = grid.result(node.state, action)
                #Calculate the total cost
                cost = node.cost + grid.individual_cost(node.state, action)
                
                # Check if the successor is reached
                if successor not in reached or cost < reached[successor]:
                    # Initialize the son node 
                    son = Node(
                    "",
                    successor,
                    cost,
                    parent=node,
                    action=action,
                    )
                    
                
                    reached[successor] = cost

                    frontier.add(son, son.cost)
                
        return NoSolution(reached) 
