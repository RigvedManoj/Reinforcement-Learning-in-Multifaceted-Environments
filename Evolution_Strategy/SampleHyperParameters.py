from matplotlib import pyplot as plt

from Estimators import run5, run20

# Fourier Value decides which fourier basis to use. 0 for Cosine, 1 for Sine.
# iN decides iteration Number.
# pN decides perturbation Number.
# upperRange decides how many iterations of theta to be calculated.

run5(1, 0.002, 1, 100, 5, 0, 20, "optimalHyperParametersCosine")
plt.show()
run5(0.1, 0.002, 1, 100, 5, 0, 20, "subOptimalSigma")
plt.show()
run5(1, 0.2, 1, 100, 5, 0, 20, "subOptimalAlpha")
plt.show()
run5(1, 0.002, 1, 10, 5, 0, 20, "subOptimalPerturbation")
plt.show()
run5(1, 0.002, 1, 100, 1, 0, 20, "subOptimalM")
plt.show()
run20(1, 0.002, 1, 100, 5, 0, 20, "optimalHyperParameters")
plt.show()
