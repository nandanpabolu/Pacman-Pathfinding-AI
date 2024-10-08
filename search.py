# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem(object):
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    start_node = problem.getStartState()
    if problem.isGoalState(start_node):
        return []

    frontier = util.Stack()
    explored_nodes = []
    
    frontier.push((start_node, []))

    while not frontier.isEmpty():
        choosen_node, actions = frontier.pop()
        if choosen_node not in explored_nodes:
            explored_nodes.append(choosen_node)
            if problem.isGoalState(choosen_node):
                return actions
            for next_node, action, cost in problem.getSuccessors(choosen_node):
                new_actions = actions + [action]
                frontier.push((next_node, new_actions))
   
    util.raiseNotDefined() 
    


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    """queue_BFS = util.Queue()
    explored_nodes = set()  
    start_node = (problem.getStartState(), 0, [])  
    queue_BFS.push(start_node)

    while not queue_BFS.isEmpty():
        (new_node, cost, path) = queue_BFS.pop()
        if problem.isGoalState(new_node):
            return path
        if new_node not in explored_nodes:
            explored_nodes.add(new_node)
            for next_node, next_action, next_cost in problem.getSuccessors(new_node):
                total_cost = cost + next_cost
                total_path = path + [next_action]
                final_state = (next_node, total_cost, total_path)
                queue_BFS.push(final_state)"""
     
    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    myQueue = util.Queue()
    visitedNodes = []
    # (node,actions)
    myQueue.push((startingNode, []))

    while not myQueue.isEmpty():
        currentNode, actions = myQueue.pop()
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            for nextNode, action, cost in problem.getSuccessors(currentNode):
                newAction = actions + [action]
                myQueue.push((nextNode, newAction))

    util.raiseNotDefined()            


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    PQ_UCS = util.PriorityQueue() #PQ_UCS = Priority Queue used for algorithm
    explored_nodes = set()  
    start_node = (problem.getStartState(), 0, []) 
    PQ_UCS.push(start_node,0)

    while not PQ_UCS .isEmpty():
        (new_node, cost, path) = PQ_UCS.pop()
        if problem.isGoalState(new_node):
            return path
        if new_node not in explored_nodes:
            explored_nodes.add(new_node)
            for next_node, next_action, next_cost in problem.getSuccessors(new_node):
                total_cost = cost + next_cost
                total_path = path + [next_action]
                final_state = (next_node, total_cost, total_path)
                PQ_UCS.push(final_state,total_cost)
    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    """PQ_AStar = util.PriorityQueue() #PQ_AStar is priority queue.
    explored_nodes = set()  
    start_node= (problem.getStartState(), 0, []) 
    Initial_Cost = 0 + heuristic(start_node[0], problem)
    PQ_AStar.push(start_node, Initial_Cost)

    while not PQ_AStar.isEmpty():
        (new_node, cost, path) = PQ_AStar.pop()
        if problem.isGoalState(new_node):
            return path
        if new_node not in explored_nodes:
            explored_nodes.add(new_node)
            for next_node, next_action, next_cost in problem.getSuccessors(new_node):
                total_cost = cost + next_cost
                total_path = path + [next_action]
                Final_state = (next_node, total_cost, total_path)
                total_cost = total_cost + heuristic(Final_state[0], problem)
                PQ_AStar.push(Final_state, total_cost)"""
    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    visitedNodes = []

    pQueue = util.PriorityQueue()
    #((coordinate/node , action to current node , cost to current node),priority)
    pQueue.push((startingNode, [], 0), 0)

    while not pQueue.isEmpty():

        currentNode, actions, prevCost = pQueue.pop()

        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            for nextNode, action, cost in problem.getSuccessors(currentNode):
                newAction = actions + [action]
                newCostToNode = prevCost + cost
                heuristicCost = newCostToNode + heuristic(nextNode,problem)
                pQueue.push((nextNode, newAction, newCostToNode),heuristicCost)

    util.raiseNotDefined()
    


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
