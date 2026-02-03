import pandas as pd

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# Extract information source column
source_series = df["Source"].dropna()

# Split multiple sources if comma separated
all_sources = source_series.astype(str).str.split(",").explode()

# Remove extra spaces
all_sources = all_sources.str.strip()

# Count frequency of each source
source_counts = all_sources.value_counts()

# Display results
print("Investment Information Sources (Frequency):")
print(source_counts)

print("\nMost Common Information Sources:")
print(source_counts.head())

print("\nTask 7 completed successfully.")
