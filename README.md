# Neural Network from scratch
I am building a neural network from scratch to learn how neural networks work.

## FindTheLine
what did i learn?
The problem was to find the best line from some amount of dots. These dots where generated through the given function y = 3x + 2 and then some random fuzzyness where added to the dots. The problem boiled down to figuring out how to minimizing the loss, this would be acomplished by changing the weights and biases closer to the number 3 and 2. But remember, the 3 and 2 are unknown.

So, how do you minimize the loss? You have to calculate the slope of the function loss = f(weight) and the slope of the function loss = f(bias). to calculate this slope we use the chain rule: dloss/dw = dloss /dy_pred * dy_pred/dw. dloss/dy_pred = 2(dy_pred - y) and dy_pred/dw = x. The same process was repeated for db.