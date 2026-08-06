# Day 20 Python File
# Purpose: Basic analysis of Mobile Repair Shop dataset

import pandas as pd

# Load dataset
df = pd.read_csv("Mobile_Repair_Shop_Synthetic_Dataset_20000.csv")

# Display first five rows
print(df.head())

# Total repairs
print("Total Repairs:", len(df))
