import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def gossip_generator(n, p = 0.3):
    #N - number of nodes
    #p - probability of edge creation
    flag = 1
    while flag:
        G = nx.fast_gnp_random_graph(n, p)
        flag = not(nx.is_connected(G))

    size = len(G)
    matrix = np.zeros((size, size))

    for i in range(size):
        neighbors = list(G.neighbors(i))
        degree = len(neighbors)
        for j in neighbors:
            matrix[i][j] = 1/(degree+1)
            matrix[i][i] = 1/(degree+1)
    return matrix






