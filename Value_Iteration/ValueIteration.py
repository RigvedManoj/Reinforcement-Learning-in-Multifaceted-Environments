# Value Iteration Algorithm
def runValueIteration(states, gamma, theta):
    count = 0
    while True:
        count += 1
        delta = 0
        tempValues = [[0] * 5 for i in range(5)]
        # Run for all states
        for i in range(0, len(states)):
            for j in range(0, len(states[i])):
                state = states[i][j]
                initialValue = state.value
                bestAction = state.action
                bestValue = 0

                # Take all actions
                for action in range(0, state.actionCount):
                    value = 0

                    # Take all transition states
                    for move in range(0, len(state.transition[action])):
                        [row, column] = state.getNextState(move)
                        value += state.transition[action][move] * (
                                states[row][column].reward + gamma * states[row][column].value)

                    # First action need not be compared
                    if action == 0:
                        bestValue = value
                        bestAction = action

                    # Assign max value to value and arg max to action
                    if value > bestValue:
                        bestAction = action
                        bestValue = value
                state.setAction(bestAction)
                tempValues[i][j] = bestValue
                finalValue = bestValue

                # Calculate Delta
                delta = max(delta, abs(finalValue - initialValue))
        for i in range(0, len(states)):
            for j in range(0, len(states[i])):
                state = states[i][j]
                state.setValue(tempValues[i][j])
        if delta < theta:
            break

    print("Total Iterations is " + str(count))
    print(" ")
    printStates(states)
    printPolicy(states)


def printStates(states):
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
            if i == 2 and j == 2:
                print(" ", end=" ")
                continue
            if i == 3 and j == 2:
                print(" ", end=" ")
                continue
            if state.action == 0:
                print("\u2190", end=" ")
            elif state.action == 1:
                print("\u2191", end=" ")
            elif state.action == 2:
                print("\u2193", end=" ")
            elif state.action == 3:
                print("\u2192", end=" ")
            else:
                print("G", end=" ")
        print(" ")
