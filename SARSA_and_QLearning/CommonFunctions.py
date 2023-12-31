def clearStateValues(states):
    for i in range(0, len(states)):
        for j in range(0, len(states[i])):
            state = states[i][j]
            state.value = 0
            state.oldValue = 0


def initialiseQValues(states, value=10):
    for i in range(0, len(states)):
        for j in range(0, len(states[i])):
            state = states[i][j]
            if state.actionCount != 0:
                state.qValue = [value, value, value, value]


def updateOldValues(states):
    for i in range(0, len(states)):
        for j in range(0, len(states[i])):
            state = states[i][j]
            state.oldValue = state.value


def incrementStateValues(states, values):
    for i in range(0, len(states)):
        for j in range(0, len(states[i])):
            state = states[i][j]
            values[i][j] += state.value
    return values


def updateStateValuesfromQ(states, epsilon):
    for i in range(0, len(states)):
        for j in range(0, len(states[i])):
            state = states[i][j]
            state.setActionProbabilities(epsilon)
            state.value = 0
            for action in range(0, state.actionCount):
                state.value += state.qValue[action] * state.actionProbabilities[action]
            state.oldValue = state.value


def calculateMSE(states, optimalValues):
    mse = 0
    count = 0
    for i in range(0, len(states)):
        for j in range(0, len(states[i])):
            state = states[i][j]
            if state.actionCount != 0:
                mse += pow(state.value - optimalValues[i][j], 2)
                count += 1
    return mse / count


def printGrid(values, iterations):
    for i in range(0, len(values)):
        for j in range(0, len(values[i])):
            print("%.4f" % round(values[i][j] / iterations, 4), end="\t")
        print(" ")
    print(" ")


def calculateDelta(states):
    delta = 0
    for i in range(0, len(states)):
        for j in range(0, len(states[i])):
            state = states[i][j]
            if state.actionCount != 0:
                delta = max(delta, abs(state.oldValue - state.value))
    return delta


def printStates(states):
    for i in range(0, len(states)):
        for j in range(0, len(states[i])):
            state = states[i][j]
            print("%.4f" % round(max(state.qValue), 4), end="\t")
        print(" ")
    print(" ")


def printVStates(states):
    for i in range(0, len(states)):
        for j in range(0, len(states[i])):
            state = states[i][j]
            print("%.4f" % round(state.value, 4), end="\t")
        print(" ")
    print(" ")


def printPolicy(states):
    for i in range(0, len(states)):
        for j in range(0, len(states[i])):
            state = states[i][j]
            action = state.qValue.index(max(state.qValue))
            if i == 2 and j == 2:
                print(" ", end=" ")
                continue
            if i == 3 and j == 2:
                print(" ", end=" ")
                continue
            if state.actionCount == 0:
                print("G", end=" ")
                continue
            if action == 0:
                print("\u2190", end=" ")
            elif action == 1:
                print("\u2191", end=" ")
            elif action == 2:
                print("\u2193", end=" ")
            elif action == 3:
                print("\u2192", end=" ")
        print(" ")
