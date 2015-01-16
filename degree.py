import collections
import math
from nltk.corpus import brown
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import numpy as np

with open("fractal_edgelist.txt", "r") as net_file:
    net = nx.read_edgelist(net_file)
    degree_sequence=sorted(nx.degree(net).values(),reverse=True)
    plt.loglog(degree_sequence, 'b-')
    plt.title("Degree Counts")
    plt.xlabel("Degree")
    plt.ylabel("Count")
    plt.savefig("degree_plot")

