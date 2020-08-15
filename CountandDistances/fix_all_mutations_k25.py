import os
import pandas as pd
import numpy as np

csv_directory = r'C:\Users\aarus\Documents\STEM2SHTEM\CSV data\all_mutations_k25.csv'
all_data = pd.read_csv(csv_directory, low_memory=False, index_col=0)
print("read csv")

all_data["File Name"] = all_data["File Name"].shift(-1)
all_data.at[3969, "File Name"] = "EPI_ISL_422186.fa"
#all_data["File Name"][99] = "EPI_ISL_422186.fa"

all_data.to_csv("all_mutations_k25_v2.csv")