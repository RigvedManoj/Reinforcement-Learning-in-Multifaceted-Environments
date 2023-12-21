from matplotlib import pyplot as plt

from CommonFunctions import plotGraph
from Estimators import estimators


def tuneParametersSigma(sigma):
    expectedSigma = [0.0] * 10
    count = 0
    for tempM in range(1, 6, 2):
        m = tempM
        for tempPN in range(2, 11, 2):
            perturbationNumber = tempPN * 10
            for tempAlpha in range(2, 100, 20):
                alpha = tempAlpha * 0.001
                expectedValues = estimators(sigma, alpha, 1, perturbationNumber, m)
                for i in range(0, len(expectedValues)):
                    expectedSigma[i] += expectedValues[i]
                count += 1
                print(count)
    for i in range(0, len(expectedSigma)):
        expectedSigma[i] = expectedSigma[i] / 75
    plotGraph(expectedSigma, "sigma: " + str(sigma))


def tuneParametersAlpha(alpha):
    count = 0
    expectedAlpha = [0.0] * 10
    for tempM in range(1, 6, 2):
        m = tempM
        for tempPN in range(2, 11, 2):
            perturbationNumber = tempPN * 10
            for tempSigma in range(2, 11, 2):
                sigma = 0.1 * tempSigma
                expectedValues = estimators(sigma, alpha, perturbationNumber, m, 10)
                for i in range(0, len(expectedValues)):
                    expectedAlpha[i] += expectedValues[i]
                count += 1
                print(count)
    for i in range(0, len(expectedAlpha)):
        expectedAlpha[i] = expectedAlpha[i] / 75
    plotGraph(expectedAlpha, "alpha:" + str(alpha))


def tuneParametersPN(pN):
    expectedPN = [0.0] * 10
    count = 0
    for tempM in range(1, 6, 2):
        m = tempM
        for tempSigma in range(2, 11, 2):
            sigma = 0.1 * tempSigma
            for tempAlpha in range(2, 100, 20):
                alpha = tempAlpha * 0.001
                expectedValues = estimators(sigma, alpha, pN, m, 10)
                for i in range(0, len(expectedValues)):
                    expectedPN[i] += expectedValues[i]
                count += 1
                print(count)
    for i in range(0, len(expectedPN)):
        expectedPN[i] = expectedPN[i] / 75
    plotGraph(expectedPN, "pN: " + str(pN))


def tuneParameterM(m):
    expectedM = [0.0] * 10
    count = 0
    for tempPN in range(2, 11, 2):
        pN = tempPN * 10
        for tempSigma in range(2, 11, 2):
            sigma = 0.1 * tempSigma
            for tempAlpha in range(2, 100, 20):
                alpha = tempAlpha * 0.001
                expectedValues = estimators(sigma, alpha, pN, m, 10)
                for i in range(0, len(expectedValues)):
                    expectedM[i] += expectedValues[i]
                count += 1
                print(count)
    for i in range(0, len(expectedM)):
        expectedM[i] = expectedM[i] / 125
    plotGraph(expectedM, "m: " + str(m))

for temporaryAlpha in range(2, 100, 10):
    permAlpha = round(temporaryAlpha * 0.001, 4)
    tuneParametersAlpha(permAlpha)
plt.show()

for temporarySigma in range(2, 11, 2):
    permSigma = round(temporarySigma * 0.1, 4)
    tuneParametersSigma(permSigma)
plt.show()

for temporaryPN in range(2, 11, 2):
    permPN = temporaryPN * 10
    tuneParametersPN(permPN)
plt.show()

for temporaryM in range(1, 6, 2):
    permM = temporaryM
    tuneParameterM(permM)
plt.show()
