import os
import pandas as pd
import numpy as np
import csv

mut25dir = r'C:\Users\aarus\Documents\STEM2SHTEM\CSV data\mutations_k25.csv'
mut29dir = r'C:\Users\aarus\Documents\STEM2SHTEM\CSV data\mutations_k29.csv'
mut31dir = r'C:\Users\aarus\Documents\STEM2SHTEM\CSV data\mutations_k31.csv'
seqdir = r'C:\Users\aarus\Documents\STEM2SHTEM\CSV data\Sequence Alignment Comparisons (Reference Genome) - Sheet1.csv'
mutations_k25 = pd.read_csv(mut25dir)
mutations_k29 = pd.read_csv(mut29dir)
mutations_k31 = pd.read_csv(mut31dir)
seq_file = pd.read_csv(seqdir)
print("all csv's read")

cols = []
data = []

for (columnName, columnData) in seq_file.iteritems():
    for val in columnData.values:
        cols.append(str(val)[0:17])
        print(cols)
    break

'''
all_files = []
for (columnName, columnData) in mutations_k25:
    for name in columnData.values():
        all_files.append(name)
'''


