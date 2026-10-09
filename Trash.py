import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

d = np.array([1, 2, 3])
e = np.array([4, 5, 6])
f = np.array([7, 8, 9])

g = np.random.randn(3, 2)
h = np.zeros(2)

#print(h)

#print(g)
#print(g[0])

vstack1 = np.vstack((a, b, c))
vstack2 = np.vstack((d, e, f))

#print(vstack1)
#print(vstack2)

#print(vstack1)
#print(vstack2)

lr = 0.1
w = np.ones(2)

print("w")
print((lr * w).shape)

matrix1 = np.ones((200,))
matrix2 = np.ones((200,2))
print(matrix2)
print(w)
print("shapes")
print(matrix1.shape)
print(matrix2.shape)
dw = (matrix2.T @ matrix1) - matrix1.T
print(dw.shape)
w -= lr * dw
print(w.shape)