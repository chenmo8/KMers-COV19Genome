import os

count = 0
directory = r'C:\Users\aarus\Documents\STEM2SHTEM\Regular Counts\mer_counts_dumps_k25.fa'
with open(directory, "r") as a_file:
    for line in list(a_file)[::2]:
        my_line = line.strip()
        if int(my_line[1:len(my_line)]) == 1:
            print(my_line)
            count += 1
            print(count)
print(count)
