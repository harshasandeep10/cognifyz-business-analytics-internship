import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# Extract investment avenue column
investment_counts = df["Investment_Avenues"].value_counts()

# Print frequency of each investment avenue
print("Investment Avenue Frequency:")
print(investment_counts)

# Identify the most preferred investment avenue
most_preferred = investment_counts.idxmax()
highest_count = investment_counts.max()

print("\nMost Preferred Investment Avenue:")
print(f"{most_preferred} (Chosen by {highest_count} people)")

# Create a bar chart
plt.figure()
investment_counts.plot(kind="bar")
plt.title("Most Preferred Investment Avenue")
plt.xlabel("Investment Avenue")
plt.ylabel("Number of People")
plt.show()

print("\nTask 4 completed successfully.")
