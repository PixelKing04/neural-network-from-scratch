import numpy as np

x = np.random.rand(100) # creates a list of 100 random numbers between 0-1
y = 3 * x + 2 + np.random.randn(100) * 0.1 # creates a list y which is (3x + 2) + random fuzziness

w, b = 0.5, 0.5 # create weight and bias
learning_rate = 0.1

y_pred = w * x + b # list of all predictions
loss = (y_pred - y) ** 2

print(loss)

#print("Step:", step, "Loss:", loss, "W:", w, "b:", b)
    #what does loss[0] want to change?
    #what does loss[1] want to change?
    #what does loss[n] want to change?
    #-> calculate the average?
    #
    #what is dloss/dw?
    #aka how much does w affect loss.
    #a change in w -> a change in y_pred -> change in loss.
    #dy_pred/dw * dloss/dy_pred = dloss/dw.
    #
    #dloss/dy_pred = 2(dy_pred - y)
    #dy_pred/dw = x !!!
    #
    #what is dloss/db?
    #aka how much does w affect loss.
    #a change in b -> a change in y_pred -> change in loss.
    #dy_pred/db * dloss/dy_pred = dloss/db.
    #
    #dloss/dy_pred = 2(dy_pred - y)
    #dy_pred/db = 1 !!!