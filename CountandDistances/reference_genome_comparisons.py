import os
import pandas as pd
import numpy as np

csv_directory = r'C:\Users\aarus\Documents\STEM2SHTEM\CSV data\canonical31mers.csv'
all_data = pd.read_csv(csv_directory, low_memory=False)
k = 31
print("read csv")

ref_data = all_data.loc[4, :]
ref_data = ref_data.tolist()
ref_data.pop(0)
ref_filename = ref_data.pop(0)
filenames = []
total_differences = []
max_mutations = []

for index, row in all_data.iterrows():
    row_data = row.tolist()
    row_data.pop(0)
    row_filename = row_data.pop(0)
    resultant = []
    for ind in range(len(ref_data)):
        resultant.append(abs(ref_data[ind] - row_data[ind]))
    filenames.append(row_filename)
    total_differences.append(sum(resultant))
    max_mutations.append(sum(resultant) / k)
    print(row_filename)

df = pd.DataFrame(data=zip(filenames, total_differences, max_mutations), columns=["File Name", "Total k-mer Differences", "Max Mutations"])
df.to_csv("mutations_k31.csv")
    
