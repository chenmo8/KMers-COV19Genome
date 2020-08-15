import os
import pandas as pd 
my_list = []
fourth_power = []
adjusted = []
ks = []
directory = r'C:\Users\aarus\Documents\STEM2SHTEM\log_graphs'
num_nucleotides = 29971

lof = []
for i in range(31):
    lof.append(str(i+1) + ".fa")

for filename in lof:
    print(filename)
    with open(os.path.join(directory, filename), "r") as a_file:
        distincts = 0
        for ln in list(a_file)[1::2]:
            distincts += 1
        my_list.append(distincts)

for k in range(1, 32):
    fourth_power.append(4**k)
    adjusted.append(num_nucleotides-k+1)
    ks.append(k)

final_list = []
for i in range(len(ks)):
    temp = []
    temp.append(ks[i])
    temp.append(my_list[i])
    temp.append(fourth_power[i])
    temp.append(adjusted[i])
    final_list.append(temp)
print(final_list)
df = pd.DataFrame(data=final_list, columns=["k", "Number of Distinct k-mers", "4^k", "Estimated k-mers"])
df.to_csv("kmer_graphs_data.csv")
