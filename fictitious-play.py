# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.axislines import SubplotZero
from random import uniform
import numpy as np

t = 1000

def fict(t):
    pay0 = np.array([[1, -1], [-1, 1]])
    pay1 = np.array([[-1, 1], [1, -1]])
    cur_x0, cur_x1 = uniform(0, 1), uniform(0, 1)
    x0s = []
    x1s = []

    for i in range(t):
        pro0 = np.array([1-cur_x1, cur_x1])
        pro1 = np.array([1-cur_x0, cur_x0])
        exp0 = np.dot(pay0, pro1)
        exp1 = np.dot(pay1, pro0)
    
        if exp0[0] > exp0[1]:
            cur_a0 = 0
        elif exp0[0] < exp0[1]:
            cur_a0 = 1
        else:
            cur_a0 = random.choice([0, 1])
            
        if exp1[0] > exp1[1]:
            cur_a1 = 0
        elif exp1[0] < exp1[1]:
            cur_a1 = 1
        else:
            cur_a1 = random.choice([0, 1])

        x0s.append(cur_x0)
        x1s.append(cur_x1)
        cur_x0 = cur_x0 + (cur_a1 - cur_x0)/(i + 2)
        cur_x1 = cur_x1 + (cur_a0 - cur_x1)/(i + 2)

    return x0s, x1s

def ficthist(t):
    x0_last = []
    for i in range(t):
        x0s, x1s = fict(t)
        x0_last.append(x0s[-1])
    return x0_last

x0s, x1s = fict(t)

fig, ax = plt.subplots()
ax.plot(x0s, 'r-')
ax.plot(x1s, 'b-')
#plt.savefig('fictitious.png')
#plt.savefig('fictitious.pdf')
plt.show()


fig = plt.figure()
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)
ax.hist(ficthist(t))
#plt.savefig('fictitious_hist.png')
#plt.savefig('fictitious_hist.pdf')
plt.show()

