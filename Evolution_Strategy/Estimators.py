import numpy

from CommonFunctions import plotGraph
from EvolutionStrategy import EvolutionStrategy


# Returns list of expected returns for incremental next theta.
def estimators(sigma, alpha, iterationNumber, perturbationNumber, m, fourier=0, upperRange=10):
    es = EvolutionStrategy(sigma, alpha, iterationNumber, perturbationNumber, m, fourier)
    expectedValues = [es.estimateTheta()]
    for k in range(1, upperRange):
        es.setNextTheta()
        expectedValues.append(es.estimateTheta())
    return expectedValues


# Runs Estimator 5 times and plots averageExpected Return.
def run5(sigma, alpha, iN, pN, m, fourier, upperRange, label):
    averageExpectedValues = [0.0] * upperRange
    for k in range(0, 5):
        tempExpectedValues = estimators(sigma, alpha, iN, pN, m, fourier, upperRange)
        for i in range(0, len(averageExpectedValues)):
            averageExpectedValues[i] += tempExpectedValues[i]
    for i in range(0, len(averageExpectedValues)):
        averageExpectedValues[i] /= 5
    plotGraph(averageExpectedValues, label)


# Runs Estimator 20 times and plots mean and std of Expected Return.
def run20(sigma, alpha, iN, pN, m, fourier, upperRange, label):
    averageExpectedValues = []
    for k in range(0, 20):
        tempExpectedValues = estimators(sigma, alpha, iN, pN, m, fourier, upperRange)
        averageExpectedValues.append(tempExpectedValues)
    meanValues = []
    stdValues = []
    for i in range(0, len(averageExpectedValues[0])):
        lst = []
        for j in range(0, len(averageExpectedValues)):
            lst.append(averageExpectedValues[j][i])
        arr = numpy.array(lst)
        meanValues.append((numpy.mean(arr)))
        stdValues.append((numpy.std(arr)))
    plotGraph(meanValues, "Average:" + label)
    plotGraph(stdValues, "Standard Deviation:" + label)

