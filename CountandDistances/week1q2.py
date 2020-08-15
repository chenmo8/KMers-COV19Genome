import pandas as pd
import numpy as np
from csv import reader
csv_directory = r'C:\Users\aarus\Documents\STEM2SHTEM\CSV data\canonical31mers.csv'
'''
with open(csv_directory, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        for col_name in row:
            print(type(col_name))

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

#print(dtypes)
df = pd.read_csv(csv_directory, low_memory=False)
print("read")
commons = []

for (columnName, columnData) in df.iteritems():
    flag = True
    for item in columnData.values:
        if not isinstance(item, (int, np.integer)):
            continue
        if int(item) == 0:
            flag = False
            break
    if flag:
        commons.append(columnName)
        print(columnName)

print(commons)
print(len(commons))
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

#print(dtypes)
df = pd.read_csv(csv_directory, low_memory=False)
print("read")
commons = 0
my_list = []
inds = []

all_data = np.array( [columnData.values for columnName, columnData in df.iteritems()] )
my_data = np.count_nonzero(all_data, axis = 1)
counts = my_data.tolist()

counts.pop(0)
counts.pop(0)

for x in range(len(counts)):
    print(counts[x])
    if counts[x] == 3970:
        commons += 1
        inds.append(x)

for ind in inds:
    my_list.append(cols[ind])

print(my_list)
print(commons)