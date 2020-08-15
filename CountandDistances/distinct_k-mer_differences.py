import pandas as pd
import os
#import difflib

directory = r'C:\Users\aarus\Documents\STEM2SHTEM\canonical25mers'
ref_directory = r'C:\Users\aarus\Documents\STEM2SHTEM\canonical25mers\EPI_ISL_402124.fa'
fasta_directory = r'C:\Users\aarus\Documents\STEM2SHTEM\fasta_files'

with open(ref_directory, "r") as ref_file:
    ref_distinct = len(list(ref_file)[::2])

for filename in os.listdir(directory):
    if (filename == "EPI_ISL_402124.fa"):
        continue
    else:
        print(filename)
    with open(os.path.join(directory, filename), "r") as n_file:
        num_distinct = len(list(n_file)[::2])
        print(num_distinct-ref_distinct)


#df = pd.DataFrame(data = [countries, states, dates], columns=["Countries", "Region/State/Province", "Date Reported"])
#df.to_csv("kmer_differences.csv")



