import tensorflow as tf
import matplotlib.pyplot as plt
from scipy.io import loadmat
import networkx as nx
import numpy as np
import os 
from scipy.sparse import csgraph
from scipy.linalg import eigh
import gudhi as gd



file = 'data/MUTAG/mat/nodes_10_gid_116_lb_0_index_1_adj.mat'
data = loadmat(file)

def HKS(egvec, egval, t):
    return np.square(egvec).dot(np.diag(np.exp(-t*egval))).sum(axis=1)

adj = np.array(data['A'], dtype = np.float32)
L = csgraph.laplacian(adj, normed = True)
egval, egvect = eigh(L)
sig = HKS(egvect,egval,10)
print(sig)
# rows, cols = np.where(adj == 1)
# edges = zip(rows.tolist(), cols.tolist())
# gr = nx.Graph()
# gr.add_edges_from(edges)
# nx.draw(gr, node_size=500, node_color = sig, with_labels = True)
# plt.show()

num_vertices = adj.shape[0]
(xs, ys) = np.where(np.triu(adj))
st = gd.SimplexTree()
for i in range(num_vertices):
    st.insert([i], filtration=-1e10)
for idx, x in enumerate(xs):        
    st.insert([x, ys[idx]], filtration=-1e10)
for i in range(num_vertices):
    st.assign_filtration([i], sig[i])
print(st)

# def extended_persistance():


# folder = 'data/MUTAG/mat'
# files = os.listdir(folder)
# labels = np.zeros(len(files), dtype = int)
# matrix = []

# for i, file in enumerate(files):
#     data = loadmat(folder + '/' + file)
#     labels[i] = int(file[file.index('lb')+3])
#     A = np.array(data['A'], dtype = np.float32)
#     L = csgraph.laplacian(A, normed = True)
#     egvals, egvect = eigh(L)
    



# print(egvect.shape)


# print(labels)
