import pandas as pd

df = pd.read_csv("Data_set 2 - Copy.csv")
print(df.columns)
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# Extract gender column and count values
gender_counts = df["gender"].value_counts()

# Print gender distribution
print("gender Distribution:")
print(gender_counts)

# Create bar chart
plt.figure()
gender_counts.plot(kind="bar")
plt.title("gender Distribution")
plt.xlabel("gender")
plt.ylabel("Count")
plt.show()

# Create pie chart
plt.figure()
gender_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("gender Distribution")
plt.ylabel("")
plt.show()

print("Task 2 completed successfully.")
