import pandas as pd 
import numpy as np
import os

#counts_directory = r'C:\Users\aarus\Documents\STEM2SHTEM\CSV data\canonical25mers.csv'
dumps_directory = r'/home/ec2-user/canonical29mers'

files = os.listdir(dumps_directory)
dict_counts = {}
cols = ["File Name"]

data = []

for ind in range(len(files)):
    curr_list = []
    with open(os.path.join(dumps_directory, files[ind]), "r") as curr_file:
        cols.append(files[ind])
        for count, seq in zip(curr_file, curr_file):
            if int(count[1::].strip()) == 0:
                print(seq.strip())
                continue
            curr_list.append(seq.strip())
    dict_counts[files[ind]] = curr_list

keys = list(dict_counts.keys())
used = 0

for key_ind in range(len(keys)):
    log_obj = open("29jaccard.txt", "a")
    log_obj.write(str(used) + "\n")
    log_obj.close()
    curr_row = [cols[key_ind + 1]]
    for u in range(used):
        curr_row.append('')
    curr_key = keys[key_ind]
    for key_jnd in range(key_ind, len(keys)): 
        other_key = keys[key_jnd]
        if key_ind == key_jnd:
            curr_row.append(1)
            continue
        intersect = abs(len(list(set(dict_counts[curr_key]).intersection(set(dict_counts[other_key])))))
        union = abs(len(list(set(dict_counts[curr_key]).union(set(dict_counts[other_key])))))
        jaccard = intersect / union
        curr_row.append(1 - jaccard)
    data.append(curr_row)
    used += 1
        
df = pd.DataFrame(data, columns=cols)
print(df.head())
df.to_csv("jaccard_k29.csv")

'''
counts = pd.read_csv(counts_directory, 'r')
print("read csv")

listOfDFRows = all_data.to_numpy().tolist()
print("converted to numpy")
cols = ["File Name"]

for row in listOfDFRows:
    cols.append(row[1])
    del row[0:2]

print(len(cols))
'''