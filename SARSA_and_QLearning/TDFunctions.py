# TD function to estimate state values
def calculateTDEstimate(currentState, newState, alpha, gamma):
    TDError = newState.reward + gamma * newState.value - currentState.value
    currentState.value = currentState.value + alpha * TDError


def calculateActionValue(currentState, newState, action, nextAction, alpha, gamma):
    qTDError = newState.reward + gamma * newState.qValue[nextAction] - currentState.qValue[action]
    currentState.qValue[action] = currentState.qValue[action] + alpha * qTDError


def calculateQLearning(currentState, newState, action, alpha, gamma):
    qTDError = newState.reward + gamma * max(newState.qValue) - currentState.qValue[action]
    currentState.qValue[action] = currentState.qValue[action] + alpha * qTDError
