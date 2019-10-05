import numpy as np
import cv2

def tick(A):
    return (np.roll(A, 1) != ((A == 1)+(np.roll(A, -1) == 1))).astype(int)

PPS = 4
Y, X = int(380), int(500)
p = .04

A = np.zeros(X)

# A[int(X/2)] = 1
A = np.random.choice([0, 1], size=X, p=[1-p, p])

grid = np.zeros((Y, X))


# A = np.random.randint(2, size=(Y,X))
# A = np.random.choice([0,1], size=(Y,X), p=[1-p,p])


for i in range(Y):
    if i%1 == 0:
        grid[i] = A
        im = np.kron(1-grid, np.ones((PPS, PPS)))
        cv2.imshow('Life',im)
        if cv2.waitKey(1)==27:
            break
    if False:
        grid[i] = A = np.random.choice([0, 1], size=X)
        im = np.kron(1-grid, np.ones((PPS, PPS)))
        cv2.imshow('Life',im)
        if cv2.waitKey(1)==27:
            break
    A = tick(A)

cv2.waitKey(1000000)
