import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib
from time import sleep
import seaborn


matplotlib.rcParams['figure.figsize'] = (20.0, 15.0)


N = 1000000
sampling_rate = 60
psr = 20

a1 = (1, 5, 10)
a2 = (1, 5.000000000000001, 10)

def step(a, dt = .0001, sigma=10, r=28, b=(8/3)):
    x, y, z = a
    xp = x + (sigma*(y-x))*dt
    yp = y + (x*(r-z)-y)*dt
    zp = z + (x*y-b*z)*dt
    return tuple((xp, yp, zp))

x1, y1, z1 = [], [], []
x2, y2, z2 = [], [], [] 
for i in range(N):
    x1.append(a1[0])
    y1.append(a1[1])
    z1.append(a1[2])
    a1 = step(a1)

    x2.append(a2[0])
    y2.append(a2[1])
    z2.append(a2[2])
    a2 = step(a2)

xn1, yn1, zn1 = [], [], []
for i in range(N):
    if i%sampling_rate == 0:
        xn1.append(x1[i])
        yn1.append(y1[i])
        zn1.append(z1[i])

xn2, yn2, zn2 = [], [], []
for i in range(N):
    if i%sampling_rate == 0:
        xn2.append(x2[i])
        yn2.append(y2[i])
        zn2.append(z2[i])

plt.ion()
plt.pause(0.01)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.axis('off')


for i in range((N//psr)-1):
    p1 =  ax.scatter([xn1[i*psr]], [yn1[i*psr]], [zn1[i*psr]], s=200, c='b', marker='o')
    p2 =  ax.scatter([xn2[i*psr]], [yn2[i*psr]], [zn2[i*psr]], s=200, c='r', marker='o')
    plt.plot(xn1[0:i*psr], yn1[0:i*psr], zn1[0:i*psr],'k-')
    plt.plot(xn2[0:i*psr], yn2[0:i*psr], zn2[0:i*psr],'k-')
    plt.pause(.000001)
    plt.clf()
    # fig = plt.figure(s)
    ax = fig.add_subplot(111, projection='3d')
    plt.axis('off')

while True:
    sleep(10)
