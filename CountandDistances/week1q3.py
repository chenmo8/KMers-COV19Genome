import pandas as pd
import numpy as np
from csv import reader
csv_directory = r'C:\Users\aarus\Documents\STEM2SHTEM\CSV data\canonical31mers.csv'
            
'''
dtypes = {"File Name":'str'}
with open(csv_directory, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        for col_name in row:
            if col_name == "File Name":
                continue
            print(col_name)
            dtypes[col_name] = 'int64'
        break
'''
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
only_one = 0
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
    if counts[x] == 1:
        inds.append(x)
        only_one += 1

for ind in inds:
    my_list.append(cols[ind])

print(my_list)
print(only_one)