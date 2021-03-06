﻿import numpy as np
import pandas as pd
import os

gap_penalty = -2
match_award = 2
mismatch_penalty = -3

def zeros(rows, cols):
    # Define an empty list
    retval = []
    # Set up the rows of the matrix
    for x in range(rows):
        # For each row, add an empty list
        retval.append([])
        # Set up the columns in each row
        for y in range(cols):
            # Add a zero to each column in each row
            retval[-1].append(0)
    # Return the matrix of zeros
    return retval

# A function for determining the score between any two bases in alignment
def match_score(alpha, beta):
    if alpha == beta:
        return match_award
    elif alpha == '-' or beta == '-':
        return gap_penalty
    else:
        return mismatch_penalty

def needleman_wunsch(seq1, seq2):
    
    # Store length of two sequences
    n = len(seq1)  
    m = len(seq2)
    
    # Generate matrix of zeros to store scores
    score = zeros(m+1, n+1)
   
    # Calculate score table
    
    # Fill out first column
    for i in range(0, m + 1):
        score[i][0] = gap_penalty * i
    
    # Fill out first row
    for j in range(0, n + 1):
        score[0][j] = gap_penalty * j
    
    # Fill out all other values in the score matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calculate the score by checking the top, left, and diagonal cells
            match = score[i - 1][j - 1] + match_score(seq1[j-1], seq2[i-1])
            delete = score[i - 1][j] + gap_penalty
            insert = score[i][j - 1] + gap_penalty
            # Record the maximum score from the three possible scores calculated above
            score[i][j] = max(match, delete, insert)
    
    # Traceback and compute the alignment 
    
    # Create variables to store alignment
    align1 = ""
    align2 = ""
    
    # Start from the bottom right cell in matrix
    i = m
    j = n
    
    # We'll use i and j to keep track of where we are in the matrix, just like above
    while i > 0 and j > 0: # end touching the top or the left edge
        score_current = score[i][j]
        score_diagonal = score[i-1][j-1]
        score_up = score[i][j-1]
        score_left = score[i-1][j]
        
        # Check to figure out which cell the current score was calculated from,
        # then update i and j to correspond to that cell.
        if score_current == score_diagonal + match_score(seq1[j-1], seq2[i-1]):
            align1 += seq1[j-1]
            align2 += seq2[i-1]
            i -= 1
            j -= 1
        elif score_current == score_up + gap_penalty:
            align1 += seq1[j-1]
            align2 += '-'
            j -= 1
        elif score_current == score_left + gap_penalty:
            align1 += '-'
            align2 += seq2[i-1]
            i -= 1

    # Finish tracing up to the top left cell
    while j > 0:
        align1 += seq1[j-1]
        align2 += '-'
        j -= 1
    while i > 0:
        align1 += '-'
        align2 += seq2[i-1]
        i -= 1
    
    # Since we traversed the score matrix from the bottom right, our two sequences will be reversed.
    # These two lines reverse the order of the characters in each sequence.
    align1 = align1[::-1]
    align2 = align2[::-1]
    
    score = np.array(score)
    print(score)
    return(align1, align2)

fasta_directory = r'/home/ec2-user/fasta_files'
ref_path = r'/home/ec2-user/fasta_files/EPI_ISL_402124.fasta'

cols = ["File Name", "Positional Differences"]
data = []
ref_genome = ""

fasta_file = open(ref_path, "r")
lines = fasta_file.readlines()
genome = [x.strip().upper() for x in lines[1:]]
ref_genome = ''.join(genome)
fasta_file.close()

for filename in os.listdir(fasta_directory):
    curr_genome = ""
    with open(os.path.join(fasta_directory, filename), "r") as n_file:
        lines = n_file.readlines()
        genome = [x.strip().upper() for x in lines[1:]]
        curr_genome = ''.join(genome)
    output1, output2 = needleman_wunsch(ref_genome, curr_genome)
    diffs = 0
    for i in range(len(output1)):
        if output1[i] != output2[i]:
            diffs += 1
    data.append([filename, diffs])
    #print(filename, diffs)
    log_obj = open("log.txt", "a")
    log_obj.write(str(filename) + str(diffs) + "\n")
    log_obj.close()
    
df = pd.DataFrame(data, columns=cols)
print(df.head())
df.to_csv('reference_genome_nw.csv')
