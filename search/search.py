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

class SearchProblem:
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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # get the start state from the problem
    startState = problem.getStartState()
    # dfs uses last in first out so use a stack
    fringe = util.Stack()
    # make a node with the current state (startstate) and an empty list for the direction path
    node = (startState, [])
    # push the node on the fringe
    fringe.push(node)
    # make a list with states we already have expanded
    expanded = []

    #check whether the fringe is empty
    while not fringe.isEmpty():
        # get the next state and the direction path we want to check
        (state, directions) = fringe.pop()

        # check if the state is the goal, if so return the direction path
        if problem.isGoalState(state):
            return directions

        # check if we already expanded the state, go back to the while statement
        if state not in expanded:
            # if not expanded, append to the expanded list
            expanded.append(state)
            # get the successors of the state
            for (successorState, successorDirection, successorCost) in problem.getSuccessors(state):
                # if a successor is not expanded yet
                if successorState not in expanded:
                    # copy the direction path and add the direction of the successor path
                    newDirections = list(directions)
                    newDirections.append(successorDirection)
                    # make a new node with the successor state and newly made direction path and push it to the fringe
                    newNode = (successorState, newDirections)
                    fringe.push(newNode)

    # if the fringe is empty return nothing (no solution found)
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # get the start state from the problem
    startState = problem.getStartState()
    # bfs uses first in first out so use a queue
    fringe = util.Queue()
    # make a node with the current state (startstate) and an empty list for the direction path
    node = (startState, [])
    # push the node on the fringe
    fringe.push(node)
    # make a list with states we already have expanded
    expanded = []

    #check whether the fringe is empty
    while not fringe.isEmpty():
        # get the next state and the direction path we want to check
        (state, directions) = fringe.pop()

        # check if the state is the goal, if so return the direction path
        if problem.isGoalState(state):
            return directions

        # check if we already expanded the state, go back to the while statement
        if state not in expanded:
            # if not expanded, append to the expanded list
            expanded.append(state)
            # get the successors of the state
            for (successorState, successorDirection, successorCost) in problem.getSuccessors(state):
                # if a successor is not expanded yet
                if successorState not in expanded:
                    # copy the direction path and add the direction of the successor path
                    newDirections = list(directions)
                    newDirections.append(successorDirection)
                    # make a new node with the successor state and newly made direction path and push it to the fringe
                    newNode = (successorState, newDirections)
                    fringe.push(newNode)

    # if the fringe is empty return nothing (no solution found)
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # get the start state from the problem
    startState = problem.getStartState()
    # ufs uses first in first out, but with priority, so use a priority queue
    fringe = util.PriorityQueue()
    # make a node with the current state (startstate) and an empty list for the direction path
    node = (startState, [])
    # push the node on the fringe, with the current total cost (0)
    fringe.push(node, 0)
    # make a list with states we already have expanded
    expanded = []

    #check whether the fringe is empty
    while not fringe.isEmpty():
        # get the next state and the direction path we want to check
        (state, directions) = fringe.pop()

        # check if the state is the goal, if so return the direction path
        if problem.isGoalState(state):
            return directions

        # check if we already expanded the state, go back to the while statement
        if state not in expanded:
            # if not expanded, append to the expanded list
            expanded.append(state)
            # get the successors of the state
            for (successorState, successorDirection, successorCost) in problem.getSuccessors(state):
                # if a successor is not expanded yet
                if successorState not in expanded:
                    # copy the direction path and add the direction of the successor path
                    newDirections = list(directions)
                    newDirections.append(successorDirection)
                    # make a new node with the successor state and newly made direction path
                    newNode = (successorState, newDirections)
                    # calculate the cost with the direction path and push the node with the cost to the fringe
                    cost = problem.getCostOfActions(newDirections)
                    fringe.push(newNode, cost)

    # if the fringe is empty return nothing (no solution found)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowestf combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # get the start state from the problem
    startState = problem.getStartState()
    # astar uses first in first out, but with priority, so use a priority queue
    fringe = util.PriorityQueue()
    # make a node with the current state (startstate) and an empty list for the direction path
    node = (startState, [])
    # push the node on the fringe, with the current total cost (0) and the estimated path cost (heuristic)
    fringe.push(node, heuristic(startState, problem))
    # make a list with states we already have expanded
    expanded = []

    #check whether the fringe is empty
    while not fringe.isEmpty():
        # get the next state and the direction path we want to check
        (state, directions) = fringe.pop()

        # check if the state is the goal, if so return the direction path
        if problem.isGoalState(state):
            return directions

        # check if we already expanded the state, go back to the while statement
        if state not in expanded:
            # if not expanded, append to the expanded list
            expanded.append(state)
            # get the successors of the state
            for (successorState, successorDirection, successorCost) in problem.getSuccessors(state):
                # if a successor is not expanded yet
                if successorState not in expanded:
                    # copy the direction path and add the direction of the successor path
                    newDirections = list(directions)
                    newDirections.append(successorDirection)
                    # make a new node with the successor state and newly made direction path
                    newNode = (successorState, newDirections)
                    # calculate the cost with the direction path and heuristic, and push the node with the cost to the fringe
                    cost = problem.getCostOfActions(newDirections) + heuristic(successorState,problem)
                    fringe.push(newNode, cost)

    # if the fringe is empty return nothing (no solution found)
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
