# Returns new average given old average and new value.
import networkx as nx
from matplotlib import pyplot as plt


def calculateExpectedReturns(initialExpectedValue, size, newValue):
    newExpectedValue = ((size - 1) * initialExpectedValue + newValue) / size
    return newExpectedValue


# Returns variance given list of values and average value.
def calculateVariance(rewardList, averageReward):
    if len(rewardList) <= 1:
        return 0
    variance = 0
    for reward in rewardList:
        variance += (reward - averageReward) ** 2
    variance = variance / (len(rewardList) - 1)
    return variance


# To make sum of probability to 1.
def generateProbability(tempList):
    tempListSum = sum(tempList)
    checkSum = 0
    for i in range(0, len(tempList)):
        tempList[i] = tempList[i] / tempListSum
        checkSum += tempList[i]
    if checkSum < 1:
        tempList[tempList.index(min(tempList))] += 1 - checkSum
    if checkSum > 1:
        tempList[tempList.index(max(tempList))] -= checkSum - 1
    assert sum(tempList) == 1
    return tempList


def drawGraph(s):
    G = nx.DiGraph()
    for state in s:
        G.add_node(state.state)
    for state in s:
        for i in range(0, state.actionCount):
            for j in range(0, len(state.transition[i])):
                if state.transition[i][j] != 0:
                    G.add_edge(state.state, j, weight=state.reward[i])
    pos = nx.circular_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.savefig("environment.png")
    plt.clf()


def drawPolicyGraph(s):
    G = nx.DiGraph()
    for state in s:
        G.add_node(state.state)
    for state in s:
        if state.actionCount != 0:
            i = state.policies.index(1)
            for j in range(0, len(state.transition[i])):
                if state.transition[i][j] != 0:
                    G.add_edge(state.state, j, weight=state.reward[i])
    pos = nx.circular_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.savefig("policy.png")
    plt.clf()
