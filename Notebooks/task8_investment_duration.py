import pandas as pd

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# Extract duration column
duration_series = df["Duration"].dropna()

# Function to convert duration text to numeric (approximate years)
def convert_duration(value):
    value = str(value).lower()
    if "less" in value:
        return 0.5
    elif "1-3" in value:
        return 2
    elif "3-5" in value:
        return 4
    elif "5" in value:
        return 6
    else:
        return None

# Apply conversion
numeric_duration = duration_series.apply(convert_duration)

# Remove invalid values
numeric_duration = numeric_duration.dropna()

# Calculate average investment duration
average_duration = numeric_duration.mean()

print("Average Investment Duration (in years):")
print(round(average_duration, 2))

print("\nTask 8 completed successfully.")
