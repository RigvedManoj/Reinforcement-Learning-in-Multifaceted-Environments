from CommonFunctions import printStates, printPolicy, initialiseQValues
from Environment import setStaticStates
from Episode import runEpisodeQLearning

states = setStaticStates()
gamma = 0.9
alpha = 0.1
theta = 0.04

maxIterations = 2000
initialiseQValues(states, 20)
iterations = 0
epsilonStep = 1 / maxIterations
while iterations < maxIterations:
    epsilon = 1 - epsilonStep * iterations
    runEpisodeQLearning(states, alpha, gamma, epsilon)
    iterations += 1
    if iterations % 2000 == 0:
        print("iteration " + str(iterations) + " of " + str(maxIterations))

printStates(states)
printPolicy(states)
