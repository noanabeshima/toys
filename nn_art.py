# nn-art.py
# From http://blog.otoro.net/2015/06/19/neural-network-generative-art/

import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.nn.functional as F

sigmoid = nn.Sigmoid()
m = nn.Tanh()

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.l = [nn.Linear(3,14)]
        for i in range(9):
            self.l.append(nn.Linear(14,14))
        self.l.append(nn.Linear(14,3))

    def forward(self, x):
        for i in range(len(self.l)-1):
            x = 4.5*m(self.l[i](x))
        x = sigmoid(self.l[-1](x))
        return x

net = Net()

L = 200

def main(L):
    arr = np.zeros((L,L,3),dtype=np.int32)
    with torch.no_grad():
        for i in range(L):
            for j in range(L):
                ip, jp= i/L, j/L
                r = np.sqrt(ip**2+jp**2)
                result = net(torch.tensor([[[ip,jp, r]]]))
                arr[i,j,0] = int(255*result[0][0][0])
                arr[i,j,1] = int(255*result[0][0][1])
                arr[i,j,2] = int(255*result[0][0][2])
    return arr

fig = plt.imshow(main(L))
plt.axis('off')
plt.savefig("art.png", bbox_inches='tight')
plt.show()
