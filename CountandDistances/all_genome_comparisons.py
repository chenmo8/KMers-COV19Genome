import os
import pandas as pd
import numpy as np

csv_directory = r'C:\Users\aarus\Documents\STEM2SHTEM\CSV data\toy_setting_k31.csv'
all_data = pd.read_csv(csv_directory, low_memory=False)
print("read csv")

listOfDFRows = all_data.to_numpy().tolist()
print("converted to numpy")

cols = ["File Name"]

for row in listOfDFRows:
    cols.append(row[1])
    del row[0:2]

print(len(cols))

used = 0
data = []

for i in range(len(listOfDFRows)):
    print(used)
    my_row = []
    my_row.append(cols[i + 1])
    curr_row = listOfDFRows[i]
    for u in range(used):
        my_row.append('')
    for j in range(i, len(listOfDFRows)): #previously i + 1
        if i == j:
            my_row.append(0)
            continue
        resultant = []
        next_row = listOfDFRows[j]
        for ind in range(len(curr_row)):
            resultant.append(abs(curr_row[ind] - next_row[ind]))
        my_row.append(sum(resultant))
        print(sum(resultant))
    data.append(my_row)
    used += 1
    print(len(my_row))

df = pd.DataFrame(data=data, columns=cols)
#df.to_csv("kmer_diff_toy_setting_k31.csv")

