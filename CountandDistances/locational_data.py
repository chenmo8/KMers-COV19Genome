import pandas as pd
import os
#import difflib

directory = r'C:\Users\aarus\Documents\STEM2SHTEM\fasta_files'
ref_directory = r'C:\Users\aarus\Documents\STEM2SHTEM\fasta_files\EPI_ISL_402124.fasta'

countries = []
states = []
dates = []
differences = []
filenames = []

#ref_genome = []
with open(ref_directory, "r") as ref_file:
    lines = ref_file.readlines()
    ref_genome = [r.strip() for r in lines[1:]]
ref_genome = ''.join(ref_genome)
ref_genome = ref_genome.upper()
#ref_genome = [char for char in ref_genome]

for filename in os.listdir(directory):
    with open(os.path.join(directory, filename), "r") as fasta_file:
        lines = fasta_file.readlines()
        info = lines[0].split("/")
        genome = [x.strip() for x in lines[1:]]
        genome = ''.join(genome)
        genome = genome.upper()
        #genome = [char for char in genome]
        #print(len(genome))
        if len(info) == 3:
            country = "unknown"
            state = info[1]
            date = info[2][20:30]
        else:
            country = info[1]
            state = info[2]
            date = info[3][20:30]
        #count = sum(1 for a, b in zip(genome, ref_genome) if a != b) + abs(len(genome) - len(ref_genome))
        countries.append(country)
        states.append(state)
        dates.append(date)
        match_pattern = zip(genome, ref_genome)                                 #give list of tuples (of letters at each index)
        difference = sum (1 for e in match_pattern if e[0] != e[1])     #count tuples with non matching elements
        difference = difference + abs(len(genome) - len(ref_genome))  
        differences.append(difference)
        filenames.append(filename)
        print(filename)
        print(difference)
        
        #print(count)
df = pd.DataFrame(zip(filenames, countries, states, dates, differences), columns=["File Names", "Countries", "Region/State/Province", "Date Reported", "Differences"])
df.to_csv("differences.csv")



