import pandas as pd

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# STEP 1: Identify numerical columns
numerical_columns = df.select_dtypes(include=["int64", "float64"])

print("Numerical Columns:")
print(numerical_columns.columns)

# STEP 2: Calculate descriptive statistics
print("\nDescriptive Statistics for Numerical Columns:")
print(numerical_columns.describe())

# STEP 3: Mean, Median, Standard Deviation separately
print("\nMean:")
print(numerical_columns.mean())

print("\nMedian:")
print(numerical_columns.median())

print("\nStandard Deviation:")
print(numerical_columns.std())

print("\nTask 3 completed successfully.")
