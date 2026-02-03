import pandas as pd

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# Extract savings objectives column
savings_series = df["What are your savings objectives?"].dropna()

# Split multiple objectives if comma separated
all_objectives = savings_series.astype(str).str.split(",").explode()

# Remove extra spaces
all_objectives = all_objectives.str.strip()

# Count frequency of each objective
objective_counts = all_objectives.value_counts()

# Display results
print("Savings Objectives (Frequency):")
print(objective_counts)

print("\nMain Savings Objectives:")
print(objective_counts.head())

print("\nTask 6 completed successfully.")
