import pandas as pd
import numpy as np

from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import load_iris #Trial Dataset
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering, DBSCAN
from sklearn.cluster import KMeans

import scipy.spatial.distance as ssd
import csv

cluster_filepath = r'C:\Users\aarus\Documents\STEM2SHTEM\CSV data\distancesk25L2.csv'
k_value = "25"
method = "L2"
num_clusters = 2
csv_file = method + "_k" + k_value + "_kmeans_c" + str(num_clusters) + ".csv"
df = pd.read_csv(cluster_filepath)
#df = df.drop(columns = ["Unnamed: 0", "Unnamed: 0.1"])

print(df.head)
#dropping faulty rows and columns (bat and pangolin, 4 senegal genomes)

bad_files = ['EPI_ISL_402131.fa', 'EPI_ISL_408514.fa', 'EPI_ISL_408515.fa', 'EPI_ISL_410721.fa', 'EPI_ISL_417024.fa', 'EPI_ISL_418206.fa', 'EPI_ISL_418207.fa', 'EPI_ISL_418208.fa', 'EPI_ISL_418209.fa', 'EPI_ISL_418796.fa', 'EPI_ISL_418810.fa', 'EPI_ISL_419529.fa', 'EPI_ISL_419530.fa', 'EPI_ISL_419531.fa', 'EPI_ISL_419532.fa', 'EPI_ISL_419533.fa', 'EPI_ISL_419534.fa', 'EPI_ISL_419535.fa', 'EPI_ISL_419536.fa', 'EPI_ISL_419537.fa', 'EPI_ISL_419538.fa', 'EPI_ISL_419539.fa', 'EPI_ISL_419540.fa', 'EPI_ISL_419561.fa']
df = df.drop(bad_files, axis=1)
df = df.drop([10, 80, 81, 105, 990, 1768, 1769, 1770, 1771, 2058, 2071, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2327])

np.fill_diagonal(df.values, 0)

print(df.head)

filenames = list(df.columns)
X = df.to_numpy()

'''
clusters = AgglomerativeClustering(n_clusters=num_clusters, affinity="precomputed", linkage='complete')
clusters.fit(X)
clusters_labels = list(clusters.labels_)
'''

clusters = KMeans(n_clusters=num_clusters, random_state=0)
clusters.fit(X)
clusters_labels = list(clusters.labels_)


totallist = []
for e in range(0,num_clusters):
    lists = []
    for r in range(0, 3946):
        if e == clusters_labels[r]:
            lists.append(filenames[r])
    totallist.append(lists)

with open(csv_file, "w") as f:
    writer = csv.writer(f)
    writer.writerows(totallist)

#print(totallist[1], totallist[2], totallist[3], totallist[4])

'''
labeldict = {}
e = 0
for clas in totallist:
    for value in clas:
        labeldict.update({value:e})
    e+=1

distArray = ssd.squareform(X)
clsuter = linkage(X, method='ward', metric='euclidean')

Z = linkage(clsuter, 'single')
fig = plt.figure(figsize=(50, 50))
dn = dendrogram(Z)
plt.xticks(rotation="vertical")
plt.xticks(fontsize="15")
plt.savefig("jaccard_k25_dendrogram.png")
plt.show()

'''

#print(df.shape)

'''
#FINDING CONSERVED K-Mers (METHOD 1):

data3 = pd.read_csv("canonical25mers.csv")
data3.head()
names = list(data3['File Name'])
filenames = list(df.columns)

groupednames = []
 
for label in range(0, num_clusters):
    labe = []
    for i in range(0, len(filenames)):
        if clusters_labels[i] == label:
            labe.append(filenames[i])
    groupednames.append(labe)

print(groupednames)

totalcounts = []
i=0
for group in groupednames:
    groupcounts = {}
    for value in group:
        groupcounts.update({value:list(data3.iloc[names.index(value)])[2:]})
    totalcounts.append(groupcounts)  
    i+=1

print(totalcounts)
kmers = list(data3.columns)[2:]
print(kmers)

kcountsgroup = []

for group in totalcounts:
    sumcounts = []
    genes = list(group.keys())
    for kk in range(0, len(kmers)):
        kmerc = 0
        for gene in genes:
            ccs = list(group[str(gene)])
            kmerc += ccs[kk]
        sumcounts.append(kmerc)
    kcountsgroup.append(sumcounts)

maxkmer = []
#Print k-mers with maximum counts. 
for i in kcountsgroup:
    print(i[0]) 
    maxe = max(i) 
    iindcs = [] 
    for value in i: 
        if value == maxe: 
            iindcs.append(i.index(maxe)) 
            kmer = [] 
            for i in iindcs: 
                kmer.append(kmers[i]) 
                maxkmer.append(kmer)

print(len(maxkmer[3])
#Check if k-mer is unique across all genomes 
unqiuekmers = [] 
for maxes in maxkmer: 
    inde = 0 
    for al in range(0, len(maxkmer)): 
        if maxes in al: 
            inde+=1 
            if inde == 1:

#Finding Unique K-mers (Second Way)
kmers = list(data3.columns)[2:]
kmerspergroup = []         

for group in kcountsgroup:
    kme = []
    if k in range(0, len(group)):
        if group[k] > 0:
            kme.append(kmers[k])
    kmerspergroup.append(kme)        
    
print(len(kmerspergroup)) #Should be 10

tolkmercounts = []
for kn in kmers:
    thatkncount = 0
    for group in kmerspergroup:
        if kn in group:
            thatkncount +=1
    totalkmercounts.append(thatkncount)

print(len(tolkmercounts))

uniquemers = []
for i in range(0, len(tolkmercounts)):
    mersofthatcat = []
    if tolkmercounts[i] <2:
        mersofthatcat.append(kmers[i])  
    uniquemers.append(mersofthatcat)
print(len(uniquemers)) #Should be 10

ukmersdict = {}

e = 0
for group in uniquemers:
    for km in group:
        ukmersdict.update({km:e})
    e+=1

ucounts = {}
for k in list(ukmersdict.keys()):
    category = ukmersdict[k]
    inde = kmers.index(k)
    clas = kcountsgroup[category]
    ucounts.update({k:clas[inde]})

for k in uniquemers:
    print(k)
    print("The count is")
    print(ucounts[k])
    print("Category")
    print(ukmersdict[k])

'''