import os
import pandas as pd
import numpy as np
import random 

csv_directory = r'C:\Users\aarus\Documents\STEM2SHTEM\CSV data\canonical25mers.csv'
all_data = pd.read_csv(csv_directory, low_memory=False)
print("read csv")

listOfDFRows = all_data.to_numpy().tolist()
print("converted to numpy")

random_df_rows = random.sample(listOfDFRows, 100)

cols = ["File Name"]

for row in random_df_rows:
    cols.append(row[1])
    del row[0:2]

print(len(cols))

used = 0
data = []

for i in range(len(random_df_rows)):
    print(used)
    my_row = []
    my_row.append(cols[i])
    curr_row = random_df_rows[i]
    for u in range(used):
        my_row.append('')
    for j in range(i, len(random_df_rows)): #previously i + 1
        if i == j:
            my_row.append(0)
            continue
        resultant = []
        next_row = random_df_rows[j]
        for ind in range(len(curr_row)):
            resultant.append(abs(curr_row[ind] - next_row[ind]))
        my_row.append(sum(resultant))
    data.append(my_row)
    used += 1
    print(len(my_row))

df = pd.DataFrame(data=data, columns=cols)
df.to_csv("all_mutations_k25_100.csv")

