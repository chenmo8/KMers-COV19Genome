import pandas as pd
import numpy as np
import os

directory = r'C:\Users\aarus\Documents\STEM2SHTEM\fasta_files'

file_names = []
lengths = []
uncertain_counts = []
percentages = []

for filename in os.listdir(directory):
    with open(os.path.join(directory, filename), "r") as fasta_file:
        lines = fasta_file.readlines()
        genome = [x.strip().upper() for x in lines[1:]]
        genome = ''.join(genome)
        uncertains = 0

        for nucleotide in genome:
            if nucleotide == "N" or nucleotide == "W":
                uncertains += 1

        file_names.append(filename)
        lengths.append(len(genome))
        uncertain_counts.append(uncertains)
        percentages.append( 100 * (uncertains / len(genome)))
    print(filename)
    
df = pd.DataFrame(data=zip(file_names, lengths, uncertain_counts, percentages), columns=["File Name", "Genome Length", "# of Uncertain Nucleotides", "Percentage of Uncertainty"])
df.to_csv("uncertainty.csv")