import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import string

fig = plt.figure(figsize=(12,12))
ax = plt.subplot(111)
ax.set_title('Graph - Shapes', fontsize=10)

cluster_filepath = r'C:\Users\aarus\Documents\STEM2SHTEM\CSV data\fixedlabelsmsa_diffs.csv' 
df = pd.read_csv(cluster_filepath, index_col="File Name")
df = df.drop(columns = ["Unnamed: 0", "Unnamed: 0.1", "Unnamed: 0.1.1"])

'''
bad_files = ['EPI_ISL_402131.fa', 'EPI_ISL_408514.fa', 'EPI_ISL_408515.fa', 'EPI_ISL_410721.fa', 'EPI_ISL_417024.fa', 'EPI_ISL_418206.fa', 'EPI_ISL_418207.fa', 'EPI_ISL_418208.fa', 'EPI_ISL_418209.fa', 'EPI_ISL_418796.fa', 'EPI_ISL_418810.fa', 'EPI_ISL_419529.fa', 'EPI_ISL_419530.fa', 'EPI_ISL_419531.fa', 'EPI_ISL_419532.fa', 'EPI_ISL_419533.fa', 'EPI_ISL_419534.fa', 'EPI_ISL_419535.fa', 'EPI_ISL_419536.fa', 'EPI_ISL_419537.fa', 'EPI_ISL_419538.fa', 'EPI_ISL_419539.fa', 'EPI_ISL_419540.fa', 'EPI_ISL_419561.fa']
df = df.drop(bad_files, axis=1)
df = df.drop([10, 80, 81, 105, 990, 1768, 1769, 1770, 1771, 2058, 2071, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2327])
print(df.shape)
'''
DistMatrix = df.to_numpy()
G = nx.from_numpy_matrix(DistMatrix)
G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),string.ascii_uppercase)))  

nx.draw(G)

plt.tight_layout()
plt.show()
plt.savefig("Graph.png", format="PNG")