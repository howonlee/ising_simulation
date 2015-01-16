import networkx as nx
import numpy as np
import sys

if __name__ == "__main__":
    mat = np.load("fractal.npy")
    print mat.shape
    mat[mat < 0] = 0
    print mat.shape
    net = nx.from_numpy_matrix(mat, create_using=nx.DiGraph())
    nx.write_edgelist(net, "fractal_edgelist.txt", data=False)
