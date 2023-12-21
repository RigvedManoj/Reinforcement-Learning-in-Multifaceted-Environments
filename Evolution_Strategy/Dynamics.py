import math

from Agent import Agent


# This Class sets environment dynamics like mass and gravity. It calculates next state given current state and action.
class Dynamics:
    def __init__(self):
        self.gravity = 9.8
        self.massCart = 1.0
        self.massPole = 0.1
        self.massTotal = self.massPole + self.massCart
        self.lengthPole = 0.5
        self.timeInterval = 0.02
        self.discount = 1.0
        self.force = 0.0
        self.b = 0.0
        self.c = 0.0
        self.d = 0.0

    # Sets force according to given action.
    def setForce(self, action):
        if action == 0:
            self.force = -10
        else:
            self.force = 10

    # Sets intermediates for environment dynamics.
    def setIntermediates(self, agent: Agent):
        self.b = (self.force + (
                self.massPole * self.lengthPole * math.pow(agent.w0, 2) * math.sin(agent.w))) / self.massTotal

        cDenominator = self.lengthPole * (4 / 3 - (self.massPole * math.pow(math.cos(agent.w), 2) / self.massTotal))
        self.c = ((self.gravity * math.sin(agent.w)) - (self.b * math.cos(agent.w))) / cDenominator

        self.d = self.b - ((self.massPole * self.c * math.cos(agent.w)) / self.massTotal)

    # Calculates next state from environment dynamics and action taken.
    def calculateNextState(self, agent: Agent):
        x = agent.x + (self.timeInterval * agent.v)
        v = agent.v + (self.timeInterval * self.d)
        w = agent.w + (self.timeInterval * agent.w0)
        w0 = agent.w0 + (self.timeInterval * self.c)
        t = agent.t + 1
        nextState = Agent(x, v, w, w0, t)
        return nextState
