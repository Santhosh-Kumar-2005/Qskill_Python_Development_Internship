import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file

data = pd.read_csv("students.csv")

print("Dataset")
print(data)

# Basic Information

print("\nDataset Information")
print(data.info())

# Statistical Summary

print("\nSummary Statistics")
print(data.describe())

# Calculate Average Marks

average_marks = data["Marks"].mean()
print("\nAverage Marks:", average_marks)

# Bar Chart

plt.figure(figsize=(8,5))
plt.bar(data["Name"], data["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Scatter Plot

plt.figure(figsize=(8,5))
plt.scatter(data["Age"], data["Marks"])
plt.title("Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.show()

# Heatmap

correlation = data.corr(numeric_only=True)

plt.figure(figsize=(6,4))
plt.imshow(correlation, cmap='coolwarm')
plt.colorbar()

plt.xticks(range(len(correlation.columns)),
           correlation.columns)

plt.yticks(range(len(correlation.columns)),
           correlation.columns)

plt.title("Correlation Heatmap")
plt.show()
