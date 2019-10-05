import numpy as np
import cv2

def roll(A, *coord):
    if (len(A.shape) != len(coord)):
        raise Exception('Number of dimensions of input array ['+str(len(A.shape))+\
                        '] and coordinate for rolling ['+str(len(coord))+'] don\'t match')
    for i in range(len(coord)):
        if coord[i] != 0:
            A = np.roll(A, coord[i], axis=i)
    return A

def life(A):
    neighbors = np.roll(A, 1, axis=0)+np.roll(A, 1, axis=1)+np.roll(A, -1, axis=0)+np.roll(A,-1, axis=1)+(roll(A, 1, 1)+roll(A, 1, -1)+roll(A, -1, 1)+roll(A, -1, -1))
    ifLive = ((2 <= neighbors)*(neighbors <= 3)).astype(int)
    ifDead = (neighbors == 3).astype(int)
    return ifLive*(A)+ifDead*(1-A)

PPS = 2
Y, X = 1080, 1920
Y, X = int(Y/2), int(X/2)
p = .1

A = np.random.randint(2, size=(Y,X))
A = np.random.choice([0,1], size=(Y,X), p=[1-p,p])

for i in range(100000):
    im = np.kron(1-A, np.ones((PPS, PPS)))
    cv2.imshow('Life',im)
    if cv2.waitKey(1)==27:
        break
    A = life(A)
