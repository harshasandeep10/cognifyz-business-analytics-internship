import pandas as pd

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# List of all reason columns
reason_columns = [
    "Reason_Equity",
    "Reason_Mutual",
    "Reason_Bonds",
    "Reason_FD"
]

# Combine all reasons into one series
all_reasons = pd.Series(dtype=str)

for col in reason_columns:
    if col in df.columns:
        all_reasons = pd.concat([all_reasons, df[col].dropna()])

# Convert to string, split multiple reasons if comma separated
all_reasons = all_reasons.astype(str).str.split(",").explode()

# Clean extra spaces
all_reasons = all_reasons.str.strip()

# Count frequency of reasons
reason_counts = all_reasons.value_counts()

# Display results
print("Reasons for Investment (Frequency):")
print(reason_counts)

print("\nTop Reasons for Investment:")
print(reason_counts.head())

print("\nTask 5 completed successfully.")
