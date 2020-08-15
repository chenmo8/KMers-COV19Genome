#Takes in the canonical counts .csv, and outputs the L2 norm distance between each genome.

import os
import pandas as pd
import numpy as np
import math
print("print imported", flush=True)

csv_directory = r"canonical25mers.csv"
all_data = pd.read_csv(csv_directory)
print("read csv", flush=True)

listOfDFRows = all_data.to_numpy().tolist()
print("converted to numpy", flush=True)

cols = ["File Name"]

for row in listOfDFRows:
    cols.append(row[1])
    del row[0:2]

print(len(cols),flush=True)

used = 0
data = []

for i in range(len(listOfDFRows)):
    print(used,flush=True)
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
            resultant.append((curr_row[ind] - next_row[ind])**2)
        print(math.sqrt(sum(resultant)), flush=True)
        my_row.append(math.sqrt(sum(resultant)))
    data.append(my_row)
    used += 1
    print(len(my_row),flush=True)

df = pd.DataFrame(data=data, columns=cols)
print("generating csv", flush=True)
df.to_csv("distancesk25L2.csv")

