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
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):  
    self.head = None
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode

def depthFirstSearch(problem: SearchProblem):
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
    """if problem.isGoalState():
        return problem.getStartState()
    else if !problem.getSuccessors(problem.getStartState()):
        return null
    LL = LinkedList()
    LL.head = Node(problem.getStartState())
    LL.
    """
    
    s = util.Stack()
    s.push(problem.getStartState())
    visited = []
    path = {}
    start = problem.getStartState()
    path[start] = ""
    potential_path = []
    count = 0
    goal = ""
    while (not s.isEmpty()):
        i = s.pop()
        if (problem.isGoalState(i)):
          
            return path[i]
        if (not i in visited):
            visited.append(i)
            successors = problem.getSuccessors(i)
            for triple in successors:
                s.push(triple[0])
                if (not triple[0] in visited):
                    if (i != start):
                        path[triple[0]] = path[i].copy()
                        path[triple[0]].append(triple[1])
                    else:
                        path[triple[0]] = []
                        path[triple[0]].append(triple[1])
                
    """else:
            successors = problem.getSuccessors(i)
            if (len(successors) > 0):
            
                for triple in successors:
            
          
                    if (not triple[0] in vijuhsited):
                        s.push(triple[0])
                        if (i != start):
                            path[triple[0]] = path[i]
                        else:
                            path[triple[0]] = []
                        path[triple[0]].append(triple[1])
                    elif (problem.isGoalState(triple[0])):
                        goal = triple[0]
                        count += 1
                        if (i != start):
                            path[triple[0] + str(count)] = path[i]
                        else:
                            path[triple[0] + str(count)] = []
                        path[triple[0] + str(count)].append(triple[1])
                        potential_path.append(path[triple[0] + str(count)])

        
    if len(potential_path) > 0:
        result = potential_path[0]
        lowest_cost = problem.getCostOfActions(potential_path[0])
        for p in potential_path:
            if problem.getCostOfActions(p) < lowest_cost:
                result = p
        return result
    elif goal != "":
        return path[goal]
    else:
        return []
     """
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    """fringe = util.Queue()
    current = (problem.getStartState(), [])
    fringe.push(current)
    closed = []
    
    while not fringe.isEmpty():
        node, path = fringe.pop()
        if problem.isGoalState(node):
            return path
        if not node in closed:
            closed.append(node)
            for coord, move, cost in problem.getSuccessors(node):
                fringe.push((coord, path + [move])) """
 
    s = util.Queue()
    s.push((problem.getStartState(),[]))
    visited = []
    path = {}
    start = problem.getStartState()
    path[str(start)[:7]] = []
    potential_path = []
    count = 0
    goal = ""
    
    while (not s.isEmpty()):
        node, path = s.pop()
        if problem.isGoalState(node):
            return path
        if not node in visited:
            visited.append(node)
            for coord, move, cost in problem.getSuccessors(node):
                s.push((coord, path + [move]))
        """i = s.pop()
        print(i)
       

        if len(i) > 1 and len(start) > 1 and type(i) == list:
            i[1] = start[1]
           
        if (problem.isGoalState(i)):
            print(path[str(i)[:7]])
            return path[str(i)[:7]]
            
        if (not str(i)[:7] in visited):
            visited.append(str(i)[:7])
            successors = problem.getSuccessors(i)
           
            for triple in successors:
                s.push(triple[0])
                if (not str(triple[0])[:7] in visited):
                    if (str(triple[0])[:7] in path):
                        continue
                    elif (i != start):
                        path[str(triple[0])[:7]] = path[str(i)[:7]].copy()
                        path[str(triple[0])[:7]].append(triple[1])
                        
                    else:
                        path[str(triple[0])[:7]] = []
                        path[str(triple[0])[:7]].append(triple[1])"""
               
    
    return []
    util.raiseNotDefined()
    


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    s = util.PriorityQueue()
    s.push(problem.getStartState(),0)
    visited = []
    path = {}
    cost = {}
    start = problem.getStartState()
    path[start] = ""
    cost[start] = 0
    potential_path = []
    count = 0
    goal = ""
    while (not s.isEmpty()):
        i = s.pop()
        if (problem.isGoalState(i)):
            return path[i]
        if (not i in visited):
            visited.append(i)
            successors = problem.getSuccessors(i)
            for triple in successors:
               if (not triple[0] in visited):
                    if (triple[0] in path) and (cost[i] + triple[2]) < cost[triple[0]]:
                        s.update(triple[0],(cost[i] + triple[2]))
                        path[triple[0]] = path[i].copy()
                        path[triple[0]].append(triple[1])
                    elif (triple[0] in path):
                        continue
                    elif (i != start):
                        path[triple[0]] = path[i].copy()
                        path[triple[0]].append(triple[1])
                        cost[triple[0]] = cost[i]
                        cost[triple[0]] += triple[2]
                        s.push(triple[0],cost[triple[0]])
                    else:
                        path[triple[0]] = []
                        path[triple[0]].append(triple[1])
                        cost[triple[0]] = triple[2]
                        s.push(triple[0],cost[triple[0]])
                
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    """
    s = util.PriorityQueue()
    s.push(problem.getStartState(),heuristic(problem.getStartState(),problem))
    visited = []
    path = {}
    cost = {}
    start = problem.getStartState()
    path[str(start)] = []
    cost[str(start)] = 0
    potential_path = []
    count = 0
    goal = ""
    while (not s.isEmpty()):
        i = s.pop()
        if (problem.isGoalState(i)):
            return path[str(i)]
        if (not i in visited):
            visited.append(i)
            successors = problem.getSuccessors(i)
            for triple in successors:
               if (not triple[0] in visited):
                    if (str(triple[0]) in path) and (cost[str(i)] + triple[2]) < cost[str(triple[0])]:
                        s.update(triple[0],(cost[str(i)] + triple[2]))
                        path[str(triple[0])] = path[str(i)].copy()
                        path[str(triple[0])].append(triple[1])
                    elif (str(triple[0]) in path):
                        continue
                    elif (i != start):
                        path[str(triple[0])] = path[str(i)].copy()
                        path[str(triple[0])].append(triple[1])
                        cost[str(triple[0])] = cost[str(i)]
                        cost[str(triple[0])] += triple[2]
                        s.push(triple[0],heuristic(triple[0],problem) + cost[str(triple[0])])
                    else:
                        path[str(triple[0])] = []
                        path[str(triple[0])].append(triple[1])
                        cost[str(triple[0])] = triple[2]
                        s.push(triple[0],heuristic(triple[0],problem) + cost[str(triple[0])])
    return []
    util.raiseNotDefined()
    """
    fringePQ = util.PriorityQueue()
    closed = []
    startState = problem.getStartState()
    fringePQ.push((startState, []), 0)
    while not fringePQ.isEmpty():
        currentNode, currentActions = fringePQ.pop()
        if problem.isGoalState(currentNode):
            return currentActions
        if currentNode not in closed:
            closed.append(currentNode)
            successors = problem.getSuccessors(currentNode)
            for child in successors:
                
                s, a, sc = child
                fringePQ.push((s, currentActions + [a]), 
                    problem.getCostOfActions(currentActions) + sc + heuristic(s, problem))
    return []
        

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
