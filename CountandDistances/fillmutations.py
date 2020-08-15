#Fills the empty cells of the distance matrix.

import pandas as pd
import csv
import numpy as np
import math

df = pd.read_csv('distancesk25L2.csv')
df = df.drop(columns = "File Name")  
print("PD CSV Done", flush=True)

fil= list(df.columns)
files = fil[1:]
#print(files.index("EPI_ISL_422146.fa")) #3934
print(len(files), flush=True)
#'''
ro = 0
for index, row in df.iterrows():
    for value in files:
        vw = row[value]
        print(files[ro],flush=True)
        #print("Running", flush=True)
        if math.isnan(vw) == False:
            print("BLUB")
            df.at[files.index(value), files[ro]] = vw
    ro +=1

#Checks for any errors (below). This part of the code can be commented out as it can be very inefficient to run.
'''
r=0
wvat = 0
for index, row in df.iterrows():
    for value in files:
        vw = row[value]
        print("Checking")
        ix = files.index(value)
        wv = df.iloc[ix][files[r]]
        if vw != wv:
            wvat +=1
            print("!WHAT?",flush=True)
    r+=1
'''
print("Going to write CSV", flush=True)
df.to_csv("fixedL2k25.csv")
'''
#print(row["EPI_ISL_422146.fa"]) 
    for value in df.columns:
        if row[value] != float("NaN"):
            value[row] == row[value]
'''
