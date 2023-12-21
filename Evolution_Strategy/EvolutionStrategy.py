import random

from Episode import runEpisode


# This class is to determine optimal theta. It will iteratively determine newer theta's that give better rewards.
class EvolutionStrategy:
    def __init__(self, sigma, alpha, iterationNumber, perturbationNumber, m, fourier):
        self.sigma = sigma
        self.alpha = alpha
        self.iterationNumber = iterationNumber
        self.perturbationNumber = perturbationNumber
        self.m = m
        self.thetaLength = self.m * 4 + 1  # Stores length of theta calculated from m
        self.theta = [0] * self.thetaLength
        self.unPerturbedTheta = [0] * self.thetaLength
        self.fourier = fourier  # to determine which fourier basis to use, 0 for cosine, 1 for sine.

    # Implementation of ES algorithm to find next theta
    def setNextTheta(self):
        estimateTheta = [0] * self.thetaLength
        for j in range(0, self.perturbationNumber):
            epsilon = []
            self.resetTheta()  # reset theta to unperturbed value.
            for i in range(0, self.thetaLength):
                epsilon.append(random.gauss(0, 1))  # get epsilon value from normal distribution.
            estimatedReturn = self.getEstimatedReturn(epsilon)
            for i in range(0, self.thetaLength):
                estimateTheta[i] += epsilon[i] * estimatedReturn
        for j in range(0, self.thetaLength):
            self.unPerturbedTheta[j] += (self.alpha * estimateTheta[j]) / (self.sigma * self.perturbationNumber)
        self.resetTheta()  # set theta to new unperturbed value.

    # Resets perturbed theta to its unperturbed value (stored in unPerturbedTheta).
    def resetTheta(self):
        for i in range(0, self.thetaLength):
            self.theta[i] = self.unPerturbedTheta[i]

    # Returns reward for theta.
    def estimateTheta(self):
        reward = runEpisode(self.m, self.theta, self.fourier)
        return reward

    # Create new theta with epsilon value and gives its estimated return.
    def getEstimatedReturn(self, epsilon):
        for i in range(0, self.thetaLength):
            self.theta[i] += self.sigma * epsilon[i]
        totalReward = 0
        for i in range(0, self.iterationNumber):
            reward = runEpisode(self.m, self.theta, self.fourier)
            totalReward += reward
        estimatedReward = totalReward / self.iterationNumber
        return estimatedReward
