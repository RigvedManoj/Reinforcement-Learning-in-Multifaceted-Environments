import math

from Agent import Agent
from CommonFunctions import dotProduct, normalizeCos, normalizeSin


# This class determines policy by determining value of phi and taking dotProduct with theta.
class PolicyDetermination:
    def __init__(self, m, theta, fourier):
        self.m = m
        self.theta = theta
        self.fourier = fourier
        self.boundX = 2.4
        self.boundV = 1.67
        self.boundW = math.pi / 15
        self.boundW0 = 1.67

    def determineAction(self, state: Agent):
        if self.fourier == 0:  # Set to Cosine if fourier is 0.
            phi = self.setPhiCos(state)
        else:
            phi = self.setPhiSin(state)
        product = dotProduct(phi, self.theta)
        if product <= 0:
            action = 0  # Take Left
        else:
            action = 1  # Take Right
        return action

    # Set value of Phi using the Cosine Fourier Basis
    def setPhiCos(self, state: Agent):
        phi = [1]
        for j in range(0, 4):
            if j == 0:
                value = normalizeCos(state.x, -1 * self.boundX, self.boundX)
            elif j == 1:
                value = normalizeCos(state.v, -1 * self.boundV, self.boundV)
            elif j == 2:
                value = normalizeCos(state.w, -1 * self.boundW, self.boundW)
            else:
                value = normalizeCos(state.w0, -1 * self.boundW0, self.boundW0)
            for i in range(1, self.m + 1):
                phi.append(math.cos(i * math.pi * value))
        return phi

    # Set value of Phi using the Sine Fourier Basis
    def setPhiSin(self, state: Agent):
        phi = [1]
        for j in range(0, 4):
            value = 0
            if j == 0:
                value = normalizeSin(state.x, -1 * self.boundX, self.boundX)
            elif j == 1:
                value = normalizeSin(state.v, -1 * self.boundV, self.boundV)
            elif j == 2:
                value = normalizeSin(state.w, -1 * self.boundW, self.boundW)
            elif j == 3:
                value = normalizeSin(state.w0, -1 * self.boundW0, self.boundW0)
            for i in range(1, self.m + 1):
                phi.append(math.sin(i * math.pi * value))
        return phi
