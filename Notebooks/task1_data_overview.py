import pandas as pd

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

print("First 5 rows:")
print(df.head())

print("\nShape of dataset (rows, columns):")
print(df.shape)

print("\nDataset information:")
print(df.info())

print("\nDescriptive statistics:")
print(df.describe())

print("\nColumn names:")
print(df.columns)

print("\nTask 1 completed successfully.")
