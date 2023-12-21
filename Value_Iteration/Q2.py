from Environment import setStaticStates
from InPlaceIteration import runInPlaceIteration
from ValueIteration import runValueIteration

states1 = setStaticStates()
states2 = setStaticStates()
gamma = 0.25
theta = 0.0001

runValueIteration(states1, gamma, theta)
runInPlaceIteration(states2, gamma, theta)
