import numpy
from matplotlib import pyplot as plt

from Environment import setStates, setInitialState, generateRandomInitialStates
from Episode import runEpisode
from Functions import calculateExpectedReturns, drawGraph, drawPolicyGraph


def run(s, gamma, p, episodeCount):
    expectedValues = []
    for i in range(0, episodeCount):
        initialState = setInitialState(s, p)
        totalReward = runEpisode(s, gamma, initialState)
        if i == 0:
            expectedValues.append(calculateExpectedReturns(0, 1, totalReward))
        else:
            expectedValues.append(calculateExpectedReturns(expectedValues[-1], i + 1, totalReward))
    x_axis = numpy.arange(0, episodeCount)
    plt.ylim(min(expectedValues) - 5, max(expectedValues) + 5)
    plt.plot(x_axis, expectedValues)
    plt.show()


states = setStates(7, 1, 3, 15, 35)
initialDistribution = generateRandomInitialStates(states)
print(initialDistribution)
run(states, 1, initialDistribution, 2000)
drawGraph(states)
drawPolicyGraph(states)
