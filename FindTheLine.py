import numpy as np

# finding the line y = w*x + b that best fits some data.

x = np.random.rand(100) # creates a list of 100 random numbers between 0-1
y = 3 * x + 2 + np.random.randn(100) * 0.1 # creates a list y which is (3x + 2) + random fuzziness

w, b = 0.0, 0.0 # create weight and bias
learning_rate = 0.2 # how fast the algorithm changes the weights and biases


for step in range(100): # we will improve the algorithm 1000 times
    y_pred = w * x + b # list of all predictions
    loss = (y_pred - y) ** 2 # average value of all the losses. np.mean()

    dw = np.mean(x * 2 * (y_pred - y)) # calculate the slope of the function loss = f(weight)
    db = np.mean(2 * (y_pred - y)) # calculate the slope of the function loss = f(bias)

    w -= learning_rate * dw # change the weight based on the slope of the function loss = f(weight) and the learning rate
    b -= learning_rate * db # change the bias based on the slope of the function loss = f(bias) and the learning rate

print(w, b)
