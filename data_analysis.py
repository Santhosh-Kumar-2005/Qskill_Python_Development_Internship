import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
data = pd.read_csv("your_dataset.csv")

# Display first few rows
print("Dataset Preview:")
print(data.head())

# Calculate average of a selected column (example: 'Sales')
average_sales = data['Sales'].mean()
print(f"\nAverage Sales: {average_sales:.2f}")

# Bar Chart - Average sales per category
plt.figure(figsize=(8,5))
data.groupby('Category')['Sales'].mean().plot(kind='bar', color='skyblue')
plt.title("Average Sales per Category")
plt.ylabel("Average Sales")
plt.show()

# Scatter Plot - Sales vs Profit
plt.figure(figsize=(8,5))
plt.scatter(data['Sales'], data['Profit'], alpha=0.6, color='green')
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()

# Heatmap - Correlation Matrix
plt.figure(figsize=(8,5))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
