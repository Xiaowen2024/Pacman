# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util
import statistics

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        """successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        distance = []
        for food in newFood.asList():
            distance.append(manhattanDistance(newPos,food))
        if (len(distance) > 0):
            min_d = min(distance)
        else: 
            min_d = 0
        if  manhattanDistance(newGhostStates[0].getPosition(),newPos) > 15:
            evaluation = - min_d - len(successorGameState.getFood().asList()) * 100  + newScaredTimes[0] * 100
        elif manhattanDistance(newGhostStates[0].getPosition(),newPos) < 1:
            evaluation = manhattanDistance(newGhostStates[0].getPosition(),newPos) * 2
        evaluation = manhattanDistance(newGhostStates[0].getPosition(),newPos) - min_d - len(successorGameState.getFood().asList()) * 50  + newScaredTimes[0]*100 
        return successorGameState.getScore() + evaluation
        """
        successorGameState = currentGameState.generatePacmanSuccessor(action)

        numFood = successorGameState.getNumFood()
        ghostNumber = successorGameState.getNumAgents() - 1
        pacmanPosition = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        capsulesDistance = []
        newGhostStates = currentGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        if (successorGameState.isWin()):
            return 10000000000
        elif (successorGameState.isLose()):
            return -10000000000
        elif (numFood < 1):
            return 100000
        distanceToGhost = 0
        distances = []
        food_distances = []
        min_d = 0 
        for i in range(ghostNumber):
            distanceToGhost += manhattanDistance(pacmanPosition,successorGameState.getGhostPosition(i+1))
            distances.append(manhattanDistance(pacmanPosition,successorGameState.getGhostPosition(i+1)))
        closest = min(distances)
        for food in newFood.asList():
            food_distances.append(manhattanDistance(pacmanPosition,food))
        if (len(food_distances) > 0):
            min_d = min(food_distances)
        for caps in successorGameState.getCapsules():
            capsulesDistance.append(manhattanDistance(caps,pacmanPosition))
        if (len(capsulesDistance) > 0):
            capCloset = min(capsulesDistance)
        if (len(successorGameState.getCapsules()) == 0):
            haveCaps = 0 
        else:
            haveCaps = 1
        return successorGameState.getScore() + closest - numFood - min_d - 10 * haveCaps + min(newScaredTimes)

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        def minMax(agentIndex,depth,gameState: GameState):

            index = 0
            """if (depth == self.depth):
                return gameState.getLegalActions(agentType)"""
            print(gameState.getNumAgents())
            print(depth)
            if (gameState.isWin() or gameState.isLose() or depth >= self.depth or len(gameState.getLegalActions()) == 0):
                return (self.evaluationFunction(gameState),None)
             
            if (agentIndex == 0):
                maximum = float("-inf")
                chosenAction = (0,gameState.getLegalActions(agentIndex)[0])
                print(gameState.getLegalActions(agentIndex))
                for action in gameState.getLegalActions(agentIndex):
                    print(action)
                    print("agentindex" + str(agentIndex))
            
                    actionValue = minMax((agentIndex + 1)%gameState.getNumAgents(),depth,gameState.generateSuccessor(agentIndex,action))
                   
                    if (actionValue):
                        if actionValue[0] > maximum:
                            maximum = actionValue[0]
                            chosenAction = (actionValue[0],action)
                   
                    
                if (chosenAction != None):
                    print(chosenAction)
                    return chosenAction
                
            elif (agentIndex >= 1):
                minimal = float("inf")
                chosenAction = (0,gameState.getLegalActions(agentIndex)[0])
                print(gameState.getLegalActions(agentIndex))
                for action in gameState.getLegalActions(agentIndex):
                    if ((agentIndex + 1)%gameState.getNumAgents() == 0):
                        print("go to next depth")
                        print(action)
                        print("agentindex" + str(agentIndex))
                        newDepth = depth + 1
                        print("new depth" + str(newDepth))
                        actionValue = minMax((agentIndex + 1)%gameState.getNumAgents(),newDepth,gameState.generateSuccessor(agentIndex,action))
                    else:
                        print(action)
                        print("agentindex" + str(agentIndex))
                       
                        actionValue = minMax((agentIndex + 1),depth,gameState.generateSuccessor(agentIndex,action))
                    if (actionValue):
                        if actionValue[0] < minimal:
                            minimal = actionValue[0]
                            chosenAction = (actionValue[0],action)
                    
                if (chosenAction != None):
                    print(chosenAction)
                    return chosenAction
                
        return minMax(0,0,gameState)[1]
        
        util.raiseNotDefined()

   

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        def minMax(agentIndex,depth,gameState: GameState, maxBest, minBest):

            index = 0
            """if (depth == self.depth):
                return gameState.getLegalActions(agentType)"""
            print(gameState.getNumAgents())
            print(depth)
            if (gameState.isWin() or gameState.isLose() or depth >= self.depth or len(gameState.getLegalActions()) == 0):
                return (self.evaluationFunction(gameState),None)
             
            if (agentIndex == 0):
                maximum = float("-inf")
                chosenAction = (0,gameState.getLegalActions(agentIndex)[0])
                print(gameState.getLegalActions(agentIndex))
                for action in gameState.getLegalActions(agentIndex):
                    print(action)
                    print("agentindex" + str(agentIndex))
            
                    actionValue = minMax((agentIndex + 1)%gameState.getNumAgents(),depth,gameState.generateSuccessor(agentIndex,action),maxBest,minBest)
                   
                    if (actionValue):
                        if actionValue[0] > maximum:
                            maximum = actionValue[0]
                            if maximum > minBest:
                                return (maximum,action)
                            maxBest = max(maximum,maxBest)
                            chosenAction = (actionValue[0],action)
                   
                    
                if (chosenAction != None):
                    print(chosenAction)
                    return chosenAction
                
            elif (agentIndex >= 1):
                minimal = float("inf")
                chosenAction = (0,gameState.getLegalActions(agentIndex)[0])
                print(gameState.getLegalActions(agentIndex))
                for action in gameState.getLegalActions(agentIndex):
                    if ((agentIndex + 1)%gameState.getNumAgents() == 0):
                        print("go to next depth")
                        print(action)
                        print("agentindex" + str(agentIndex))
                        newDepth = depth + 1
                        print("new depth" + str(newDepth))
                        actionValue = minMax((agentIndex + 1)%gameState.getNumAgents(),newDepth,gameState.generateSuccessor(agentIndex,action),maxBest,minBest)
                    else:
                        print(action)
                        print("agentindex" + str(agentIndex))
                        actionValue = minMax((agentIndex + 1),depth,gameState.generateSuccessor(agentIndex,action),maxBest,minBest)
                    if (actionValue):
                        if actionValue[0] < minimal:
                            minimal = actionValue[0]
                            chosenAction = (actionValue[0],action)
                            if minimal < maxBest:
                                return (minimal,action)
                            minBest = min(minimal,minBest)
                if (chosenAction != None):
                    print(chosenAction)
                    return chosenAction
        return minMax(0,0,gameState,float("-inf"),float("inf"))[1]
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        def expectiMax(agentIndex,depth,gameState: GameState):

            index = 0
            """if (depth == self.depth):
                return gameState.getLegalActions(agentType)"""
            print(gameState.getNumAgents())
            print(depth)
            if (gameState.isWin() or gameState.isLose() or depth >= self.depth or len(gameState.getLegalActions()) == 0):
                return (self.evaluationFunction(gameState),None)
             
            if (agentIndex == 0):
                maximum = float("-inf")
                chosenAction = (0,gameState.getLegalActions(agentIndex)[0])
                print(gameState.getLegalActions(agentIndex))
                for action in gameState.getLegalActions(agentIndex):
                    print(action)
                    print("agentindex" + str(agentIndex))
            
                    actionValue = expectiMax((agentIndex + 1)%gameState.getNumAgents(),depth,gameState.generateSuccessor(agentIndex,action))
                   
                    if (actionValue):
                        if actionValue[0] > maximum:
                            maximum = actionValue[0]
                            chosenAction = (actionValue[0],action)
                   
                    
                if (chosenAction != None):
                    print(chosenAction)
                    return chosenAction
                
            elif (agentIndex >= 1):
                minimal = float("inf")
                chosenAction = (0,gameState.getLegalActions(agentIndex)[0])
                print(gameState.getLegalActions(agentIndex))
                value = []
                for action in gameState.getLegalActions(agentIndex):
                    if ((agentIndex + 1)%gameState.getNumAgents() == 0):
                        print("go to next depth")
                        print(action)
                        print("agentindex" + str(agentIndex))
                        newDepth = depth + 1
                        print("new depth" + str(newDepth))
                        actionValue = expectiMax((agentIndex + 1)%gameState.getNumAgents(),newDepth,gameState.generateSuccessor(agentIndex,action))
                        value.append(actionValue[0])
                    else:
                        print(action)
                        print("agentindex" + str(agentIndex))
                       
                        actionValue = expectiMax((agentIndex + 1),depth,gameState.generateSuccessor(agentIndex,action))
                        value.append(actionValue[0])
                    chosenAction = (sum(value)/len(gameState.getLegalActions(agentIndex)),gameState.getLegalActions(agentIndex)[0])
                    
                if (chosenAction != None):
                    print(chosenAction)
                    return chosenAction
                
        return expectiMax(0,0,gameState)[1]
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    numFood = currentGameState.getNumFood()
    ghostNumber = currentGameState.getNumAgents() - 1
    pacmanPosition = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    capsulesDistance = []
    if (currentGameState.isWin()):
        return 10000000000
    elif (currentGameState.isLose()):
        return -10000000000
    elif (numFood < 1):
        return 100000
    distanceToGhost = 0
    distances = []
    food_distances = []
    min_d = 0 
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    for i in range(ghostNumber):
        distanceToGhost += manhattanDistance(pacmanPosition,currentGameState.getGhostPosition(i+1))
        distances.append(manhattanDistance(pacmanPosition,currentGameState.getGhostPosition(i+1)))
    closest = min(distances)
    for food in newFood.asList():
        food_distances.append(manhattanDistance(pacmanPosition,food))
        if (len(food_distances) > 0):
            min_d = min(food_distances)
    for caps in currentGameState.getCapsules():
        capsulesDistance.append(manhattanDistance(caps,pacmanPosition))
        if (len(capsulesDistance) > 0):
            capCloset = min(capsulesDistance)
    if (len(currentGameState.getCapsules()) == 0):
        haveCaps = 0 
    else:
        haveCaps = 1
    return  currentGameState.getScore() + closest - numFood - min_d - 10 * haveCaps + min(newScaredTimes)
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
