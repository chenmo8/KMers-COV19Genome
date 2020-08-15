import pandas as pd, seaborn as sns
import scipy.spatial as sp, scipy.cluster.hierarchy as hc
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

cluster_filepath = r'C:\Users\aarus\Documents\STEM2SHTEM\CSV data\fixedL1_k25.csv'
#df = pd.read_csv(cluster_filepath, index_col="File Name")
#df = df.drop(columns = ["Unnamed: 0", "Unnamed: 0.1", "Unnamed: 0.1.1"])
df = pd.read_csv(cluster_filepath)
df = df.drop(columns = ["Unnamed: 0", "Unnamed: 0.1"])

bad_files = ['EPI_ISL_402131.fa', 'EPI_ISL_408514.fa', 'EPI_ISL_408515.fa', 'EPI_ISL_410721.fa', 'EPI_ISL_417024.fa', 'EPI_ISL_418206.fa', 'EPI_ISL_418207.fa', 'EPI_ISL_418208.fa', 'EPI_ISL_418209.fa', 'EPI_ISL_418796.fa', 'EPI_ISL_418810.fa', 'EPI_ISL_419529.fa', 'EPI_ISL_419530.fa', 'EPI_ISL_419531.fa', 'EPI_ISL_419532.fa', 'EPI_ISL_419533.fa', 'EPI_ISL_419534.fa', 'EPI_ISL_419535.fa', 'EPI_ISL_419536.fa', 'EPI_ISL_419537.fa', 'EPI_ISL_419538.fa', 'EPI_ISL_419539.fa', 'EPI_ISL_419540.fa', 'EPI_ISL_419561.fa']
df = df.drop(bad_files, axis=1)
df = df.drop([10, 80, 81, 105, 990, 1768, 1769, 1770, 1771, 2058, 2071, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2327])

np.fill_diagonal(df.values, 0)

linkage = hc.linkage(sp.distance.squareform(df), method='complete') #hierarchical clustering

sns.set(font_scale=1)
sns.clustermap(df, row_linkage=linkage, col_linkage=linkage)
plt.figure(figsize=(200,200))
plt.show()
