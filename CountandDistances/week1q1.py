directory = r'C:\Users\aarus\Documents\STEM2SHTEM\Canonical Counts\mer_counts_dumps_k31_c_v2.fa'

uniques = 0
with open(directory, "r") as a_file:
    for count, seq in zip(a_file, a_file):
        if int(count[1::].strip()) == 1:
            uniques += 1

print(uniques)
