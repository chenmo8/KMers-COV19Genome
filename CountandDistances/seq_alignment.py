import os
import pandas as pd
import numpy as np
import itertools

fasta_directory = r'C:\Users\aarus\Documents\STEM2SHTEM\fasta_files'
msa_directory = r'C:\Users\aarus\Documents\STEM2SHTEM\msa_0703.fasta'
#filenames_directory = r'C:\Users\aarus\Documents\STEM2SHTEM\CSV data\mutations_k25.csv'

fasta_headers = []

sequence_dictionary = {}
#length of each aligned sequence is 64459

for filename in os.listdir(fasta_directory):
    fasta_headers.append(filename[0:14])
    #print(filename[0:14])
    '''
    with open(os.path.join(fasta_directory, filename), 'r') as fasta_file:
        fasta_headers.append(list(fasta_file.readlines())[0].strip())
    '''

with open(msa_directory, 'r') as msa_file:
    for header, sequence in itertools.zip_longest(*[msa_file]*2):
        if any(fasta_header in header.strip() for fasta_header in fasta_headers):
            #print(header.strip())
            sequence_dictionary[header.strip()] = sequence.replace(" ", "")

senegal_genomes = ['>hCoV-19/Senegal/003/2020|EPI_ISL_418206|2020-02-28|Africa', '>hCoV-19/Senegal/016/2020|EPI_ISL_418207|2020-03-02|Africa', '>hCoV-19/Senegal/020/2020|EPI_ISL_418208|2020-03-04|Africa', '>hCoV-19/Senegal/026/2020|EPI_ISL_418209|2020-03-03|Africa']

for header in senegal_genomes:
    del sequence_dictionary[header]
#print([i for i in fasta_headers + new_headers if i not in fasta_headers or i not in new_headers])

file_headers = list(sequence_dictionary.keys())
file_headers.insert(0, "File Name")
#print(file_headers)
used = 0
data = []

for i in range(len(file_headers) - 1):
    print(used)
    curr_head = file_headers[i + 1]
    curr_row = [curr_head]
    curr_seq = sequence_dictionary[curr_head]
    for u in range(used):
        curr_row.append("")
    for j in range(i , len(file_headers) - 1):
        if i == j:
            curr_row.append(0)
            continue
        next_head = file_headers[j + 1]
        next_seq = sequence_dictionary[next_head]
        diffs = 0
        for pos in range(len(curr_seq)):
            if curr_seq[pos] != next_seq[pos]:
                diffs += 1
        curr_row.append(diffs)
        #print(diffs)
    print(len(curr_row))
    print(curr_row)
    data.append(curr_row)
    used += 1

df = pd.DataFrame(data=data, columns=file_headers)
df.to_csv("msa_diffs.csv")

    
