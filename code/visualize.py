import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from CSV
data = pd.read_csv('../Data/data_python_150.csv')

# Display the first few rows to check the data
print(data.head())

# Create a bar plot showing the count of each observational state per cell
plt.figure(figsize=(10, 6))
sns.countplot(x='Observational states', hue='Cell', data=data)
plt.title("Distribution of Observational States for Each Cell")
plt.xlabel("Observational States")
plt.ylabel("Frequency")
plt.show()

# Create a time series plot of Observational states for each cell
plt.figure(figsize=(10, 6))
sns.lineplot(x=data.index, y='Observational states',
             hue='Cell', data=data, marker='o')
plt.title("Observational States Over Time for Each Cell")
plt.xlabel("Time Step")
plt.ylabel("Observational State")
plt.show()

# Create a box plot to compare the distribution of observational states across cells
plt.figure(figsize=(10, 6))
sns.boxplot(x='Cell', y='Observational states', data=data)
plt.title("Box Plot of Observational States by Cell")
plt.xlabel("Cell")
plt.ylabel("Observational States")
plt.show()

# Save the plot to a file
plt.savefig("plot.png", dpi=300)
