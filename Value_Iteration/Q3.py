from Environment import setStaticStates
from ValueIteration import runValueIteration

states = setStaticStates()
states[0][2].setReward(5)
gamma = 0.9
theta = 0.0001

runValueIteration(states, gamma, theta)
