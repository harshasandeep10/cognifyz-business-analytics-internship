import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# Convert Duration text to numeric years
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
df["Duration_Years"] = df["Duration"].apply(convert_duration)

# Keep only required numeric columns
numeric_data = df[["age", "Duration_Years"]].dropna()

# -------------------------
# Correlation calculation
# -------------------------
correlation_matrix = numeric_data.corr()
print("Correlation Analysis:")
print(correlation_matrix)

# -------------------------
# Visualization (Scatter Plot)
# -------------------------
plt.figure()
plt.scatter(numeric_data["age"], numeric_data["Duration_Years"])
plt.title("Age vs Investment Duration")
plt.xlabel("Age")
plt.ylabel("Investment Duration (Years)")
plt.show()

print("\nTask 10 visualization completed successfully.")
