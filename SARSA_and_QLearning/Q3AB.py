from CommonFunctions import initialiseQValues, updateStateValuesfromQ, clearStateValues, calculateMSE, printStates
from Environment import setStaticStates
from Episode import runEpisodeQLearning
from matplotlib import pyplot as plt

from ValueIteration import runValueIteration

states = setStaticStates()
gamma = 0.9
alpha = 0.1

clearStateValues(states)
runValueIteration(states, gamma, 0.0001)
optimalValues = [[0] * 5 for i in range(5)]

for i in range(0, 5):
    for j in range(0, 5):
        optimalValues[i][j] = states[i][j].value

clearStateValues(states)

maxIterations = 500
stepList = [0] * maxIterations
MSE = [0] * maxIterations
for i in range(0, 20):
    initialiseQValues(states, 20)
    iterations = 0
    steps = 0
    while iterations < maxIterations:
        epsilon = max(0.9 - 0.002 * iterations, 0.002)
        step = runEpisodeQLearning(states, alpha, gamma, epsilon)
        updateStateValuesfromQ(states, epsilon)
        MSE[iterations] += calculateMSE(states, optimalValues)
        steps += step
        stepList[iterations] += steps
        iterations += 1
    print("iteration " + str(i) + " of 20")

for i in range(0, maxIterations):
    stepList[i] /= 20
    MSE[i] /= 20

episodeList = [i for i in range(maxIterations)]
plt.plot(stepList, episodeList)
plt.title("Average Steps over Episodes")
plt.xlabel("Steps")
plt.ylabel("Episodes")
plt.show()

plt.plot(episodeList, MSE)
plt.title("Average MSE over Episodes")
plt.xlabel("Episodes")
plt.ylabel("MSE")
plt.show()
