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
    ifDead = ((neighbors == 3)+(neighbors==4)).astype(int)
    return ifLive*(A)+ifDead*(1-A)

PPS = 2
Y, X = 1080, 1920
Y, X = int(Y/2), int(X/2)
p = .01

A = np.zeros((Y, X))

B = np.array([
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,0,1,0,1,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
    ])

A[int(Y/2)-5:int(Y/2)+5, int(X/2)-5:int(X/2)+5] = B


for i in range(100000):
    #if i % speed == 0:
    im = np.kron(1-A, np.ones((PPS, PPS)))
    cv2.imshow('Life',im)
    if cv2.waitKey(1)==27:
        break
    A = life(A)
