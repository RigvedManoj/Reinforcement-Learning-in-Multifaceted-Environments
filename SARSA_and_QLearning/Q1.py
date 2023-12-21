from CommonFunctions import clearStateValues, incrementStateValues, printGrid, calculateDelta, updateOldValues
from Environment import setStaticStates
from Episode import runEpisodeTDEstimate
from ValueIteration import runValueIteration

# Initialise Grid and set values
states = setStaticStates()
gamma = 0.9
alpha = 0.1
theta = 0.0001

# Run value iteration to set policy to optimal policy
runValueIteration(states, gamma, 0.0001)

values = [[0] * 5 for i in range(5)]
iterationList = []
for i in range(0, 50):
    clearStateValues(states)  # Reset state values to initial value 0.
    iterations = 0
    while True:
        iterations += 1
        runEpisodeTDEstimate(states, alpha, gamma)
        delta = alpha * calculateDelta(states)
        updateOldValues(states)  # Reset past values with current values after an episode ends.
        if delta < theta:
            break
    print("iteration " + str(i) + " of 50")
    values = incrementStateValues(states, values)  # add state values to find average.
    iterationList.append(iterations)

printGrid(values, 50)

# Get state values for optimal policy.
clearStateValues(states)
runValueIteration(states, gamma, 0.0001)

# Get Max Norm between actual state values and approx state values
maxDiff = 0
for i in range(0, 5):
    for j in range(0, 5):
        maxDiff = max(maxDiff, abs((values[i][j] / 50) - states[i][j].value))
print("Max Norm is " + str(maxDiff))

# Get average and standard deviation of Iterations
mean = sum(iterationList) / len(iterationList)
variance = sum([((x - mean) ** 2) for x in iterationList]) / len(iterationList)
res = variance ** 0.5
print("Average of Iterations is " + str(mean))
print("Standard Deviation is " + str(res))
