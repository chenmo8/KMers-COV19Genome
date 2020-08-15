import pandas as pd
import os
cols = []
data = []
all_directory = r'C:\Users\aarus\Documents\STEM2SHTEM\Canonical Counts\mer_counts_dumps_k29_c.fa'
my_directory = r'C:\Users\aarus\Documents\STEM2SHTEM\canonical29mers'

with open(all_directory, "r") as a_file:
    for line in list(a_file)[1::2]:
        my_line = line.strip()
        cols.append(my_line)

for x in range(3970):
    my_row = [0] * len(cols)
    data.append(my_row)

indexer = 0

weirds = []

for filename in os.listdir(my_directory):
    with open(os.path.join(my_directory, filename), "r") as n_file:
        for count, seq in zip(n_file, n_file):
            if seq.strip() not in cols:
                weirds.append(filename + " " + seq.strip())
                continue
            ind = cols.index(seq.strip())
            data[indexer][ind] = int(count[1::].strip())
    data[indexer].insert(0, filename)
    indexer += 1
    print(filename)

cols.insert(0, "File Name")
print(weirds)
df = pd.DataFrame(data, columns=cols)
print(df.head())
df.to_csv('canonical29mers.csv')
