import State
from Environment import setInitialState
from TDFunctions import calculateTDEstimate, calculateActionValue, calculateQLearning


def runEpisodeTDEstimate(states, alpha, gamma):
    [x, y] = setInitialState()
    currentState: State = states[x][y]
    while not currentState.checkEndState():
        currentState.setMove()
        [newX, newY] = currentState.getNextState()
        newState = states[newX][newY]
        calculateTDEstimate(currentState, newState, alpha, gamma)
        currentState = newState


def runEpisodeSARSA(states, alpha, gamma, epsilon):
    steps = 0
    [x, y] = setInitialState()
    currentState: State = states[x][y]
    currentState.setActionProbabilities(epsilon)
    currentState.takeAction()
    while not currentState.checkEndState():
        steps += 1
        currentState.setMove()
        [newX, newY] = currentState.getNextState()
        newState = states[newX][newY]
        newState.setActionProbabilities(epsilon)
        if newState.actionCount != 0:
            newState.takeAction()
            calculateActionValue(currentState, newState, currentState.action, newState.action, alpha, gamma)
        else:
            calculateActionValue(currentState, newState, currentState.action, 0, alpha, gamma)
        currentState = newState
    return steps


def runEpisodeQLearning(states, alpha, gamma, epsilon):
    steps = 0
    [x, y] = setInitialState()
    currentState: State = states[x][y]
    while not currentState.checkEndState():
        steps += 1
        currentState.setActionProbabilities(epsilon)
        currentState.takeAction()
        currentState.setMove()
        [newX, newY] = currentState.getNextState()
        newState = states[newX][newY]
        newState.setActionProbabilities(epsilon)
        calculateQLearning(currentState, newState, currentState.action, alpha, gamma)
        currentState = newState
    return steps
