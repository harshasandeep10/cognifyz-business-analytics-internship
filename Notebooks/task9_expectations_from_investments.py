import pandas as pd

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# Extract expectations column
expect_series = df["Expect"].dropna()

# Split multiple expectations if comma separated
all_expectations = expect_series.astype(str).str.split(",").explode()

# Remove extra spaces
all_expectations = all_expectations.str.strip()

# Count frequency of each expectation
expect_counts = all_expectations.value_counts()

# Display results
print("Expectations from Investments (Frequency):")
print(expect_counts)

print("\nMost Common Expectations:")
print(expect_counts.head())

print("\nTask 9 completed successfully.")
