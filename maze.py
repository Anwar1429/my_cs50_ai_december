# create a search algorithm in python code

import sys

""""
Create a class "Node" which is an object with three attributes:
    - state: Represents the state of the node, which could be the position 
     in a maze, configuration in a puzzle, or any relevant information for
     the specific problem being solved.

    - parent: Points to the parent node, indicating how the algorithm reached 
     the current state. This linkage is crucial for reconstructing the
     solution path once the goal state is reached.

    - action: Represents the action taken to transition from the parent node
      to the current node. This could be a move in a maze, a step in a puzzle,
      or any action relevant to the problem.
"""
class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

# This class implements a stack-based frontier for depth-first search
class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node): #adds a node to the frontier
        self.frontier.append(node)

    def contains_state(self, state):#checks if a state is already in the frontier
        return any (node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
        



""" the Node in this code is a class 
(i.e., a blueprint) of a square in a maze, while the node is a specific
 instance of that class. The Node class objects have a state, parent, and
action. The state of the node instance is described by two elements,
row (i) and column (j), so the node.state means parameters (i, j) for
this particular square in the maze."""
    
print("end")
    




