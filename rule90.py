import numpy as np
import cv2

def tick(A):
    return ((np.roll(A, 1) != np.roll(A, -1))).astype(int)

PPS = 6
Y, X = 380, 500
p = .3

A = np.zeros(X)

#A[int(X/2)] = 1
A = np.random.choice([0, 1], size=X, p=[1-p, p])

grid = np.zeros((Y, X))


# A = np.random.randint(2, size=(Y,X))
# A = np.random.choice([0,1], size=(Y,X), p=[1-p,p])


for i in range(Y):
    grid[i] = A
    im = np.kron(1-grid, np.ones((PPS, PPS)))
    cv2.imshow('Life',im)
    if cv2.waitKey(1)==27:
        break
    A = tick(A)

cv2.waitKey(1000000)
