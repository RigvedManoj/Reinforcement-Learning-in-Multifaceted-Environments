from Dynamics import Dynamics
from PolicyDetermination import PolicyDetermination
from Agent import Agent


# Run 1 episode given m and theta.
def runEpisode(m, theta, fourier):
    totalReward = 0
    currentState = Agent(0, 0.0, 0.0, 0.0, 0)
    dynamics = Dynamics()  # Sets Environment and Agent Dynamics after every action.
    policy = PolicyDetermination(m, theta, fourier)
    while not currentState.checkEndState():
        action = policy.determineAction(currentState)  # Determines action given current state, theta and m.
        reward = currentState.reward[action]
        totalReward += (dynamics.discount ** currentState.t) * reward
        dynamics.setForce(action)
        dynamics.setIntermediates(currentState)
        newState = dynamics.calculateNextState(currentState)  # Calculates next state given Dynamics and action.
        currentState = newState
    return totalReward
