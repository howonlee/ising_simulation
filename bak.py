import numpy as np
import numpy.random as npr
import math
import collections
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

class BakLattice:

    def __init__(self, n, critLevel):
        npr.seed(1337)
        self.n = n
        self.critLevel = critLevel
        self.array = npr.randint(critLevel, size=(n, n))
        self.numAvalanches = 0

    def get_array(self, start=0, end=None):
        if start==0 and end==None:
            return self.array
        else:
            return self.array[:, start:end]

    def loop(self, steps=1):
        [self.step() for i in xrange(steps)]

    def increase(self, x, y):
        graphs = collections.Counter()
        if x < 0 or x >= self.n or y < 0 or y >= self.n:
            return collections.Counter()
        self.array[x][y] += 1
        if self.array[x][y] >= self.critLevel:
            graphs[(x+1, y)] += 1
            graphs[(x-1, y)] += 1
            graphs[(x, y+1)] += 1
            graphs[(x, y-1)] += 1
            self.numAvalanches += 1
            self.array[x][y] -= 4
            graphs += self.increase(x+1, y)
            graphs += self.increase(x-1, y)
            graphs += self.increase(x, y+1)
            graphs += self.increase(x, y-1)
        return graphs

    def step(self):
        stepgraph = self.increase(npr.randint(self.n-1), npr.randint(self.n-1))
        self.graphs.append(stepgraph)
