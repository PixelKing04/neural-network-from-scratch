import numpy as np

# finding the line y = w*x + b that best fits some data.

x = np.random.rand(100) # creates a list of 100 random numbers between 0-1
y = 3 * x + 2 + np.random.randn(100) * 0.1 # creates a list y which is (3x + 2) + random fuzziness