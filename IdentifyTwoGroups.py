import numpy as np
import matplotlib.pyplot as plt

n = 100
X = np.vstack([np.random.randn(n, 2) - 1, np.random.randn(n, 2) + 1]) # (200, 2)
y = np.concatenate([np.zeros(n), np.ones(n)]) # (200,)

w, b, lr = np.zeros(2), 0.0, 0.1

for step in range(1000):
    p = 1 / (1 + np.exp(-(X @ w + b)))   # sigmoid: probability of class 1    p = (200,)
    loss = -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)) # loss = a number

    dw = (X.T @ (p - y)) / len(y)
    db = np.mean(p - y)

    w -= lr * dw
    b -= lr * db

print(w, b)
print(loss, np.mean((p > 0.5) == y))  # loss and accuracy

x1 = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
x2 = (-(w[0] * x1 + b)) / w[1]

plt.plot(x1, x2)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()