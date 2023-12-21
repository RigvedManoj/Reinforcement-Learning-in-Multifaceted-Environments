import numpy
from matplotlib import pyplot as plt


# Some Common functions used
def plotGraph(expectedValues, label):
    x_axis = numpy.arange(0, len(expectedValues))
    plt.plot(x_axis, expectedValues, label=label)
    plt.legend(loc='lower right')


def normalizeCos(value, minimum, maximum):
    newValue = (value - minimum) / (maximum - minimum)
    return newValue


def normalizeSin(value, minimum, maximum):
    newValue = 2 * ((value - minimum) / (maximum - minimum)) - 1
    return newValue


def dotProduct(arr1, arr2):
    dotProductSum = 0
    for i in range(0, len(arr2)):
        dotProductSum += arr1[i] * arr2[i]
    return dotProductSum
