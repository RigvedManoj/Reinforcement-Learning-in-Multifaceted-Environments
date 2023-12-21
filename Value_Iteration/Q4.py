from Environment import setStaticStates
from ValueIteration import runValueIteration

states = setStaticStates()
states[0][2].setReward(5)
states[0][2].actionCount = 0
states[0][2].setAction(None)
gamma = 0.9
theta = 0.0001

runValueIteration(states, gamma, theta)

# q4 gamma = 0.9133
# q5 gamma=4.49 gamma=-11.104
