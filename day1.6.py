import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as np
import scipy.sparse as sp
G = nx.Graph()
G.add_edges_from([(1,2),(2,3),(1,3)])

adj_matrix=nx.adjacency_matrix(G)
adj_matrix_np = adj_matrix.toarray()
print(adj_matrix_np)
