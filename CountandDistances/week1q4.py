import pandas as pd
import numpy as np
from csv import reader
csv_directory = r'C:\Users\aarus\Documents\STEM2SHTEM\CSV data\canonical31mers.csv'

cols = []
with open(csv_directory, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        for col_name in row:
            print(col_name)
            cols.append(col_name)
        break

cols.pop(0)
cols.pop(0)
print(len(cols))

df = pd.read_csv(csv_directory, low_memory=False)
print("read")
all_but = 0
my_list = []
inds = []

all_data = np.array( [columnData.values for columnName, columnData in df.iteritems()] )
print("np confirmed")
my_data = np.count_nonzero(all_data, axis = 1)
counts = my_data.tolist()
print("counted nonzeros")

counts.pop(0)
counts.pop(0)

for x in range(len(counts)):
    print(counts[x])
    if counts[x] == 3969:
        inds.append(x)
        all_but += 1

for ind in inds:
    my_list.append(cols[ind])

print(my_list)
print(all_but)