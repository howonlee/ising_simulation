import numpy as np
import numpy.random as npr
import math
import matplotlib.pyplot as plt

class Bak_lattice:

    def __init__(self, N):
        npr.seed(1337)
        self._N = N
