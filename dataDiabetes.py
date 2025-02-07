import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
data = pd.read_csv('diabetes.csv', encoding='latin1') 

# Display first few rows
print(data.head())

# Find total records
totalRecords = len(data)
print("Total Records:", totalRecords)

# Get statistics for numerical columns
print(data.describe())

# Find column-wise average
average = data.mean() #mean will get the average
print("Column Averages:\n", average)

# Count patients with diabetes (Outcome = 1)
diabeteCount = data['Outcome'].sum()
print("Diabetes Cases:", diabeteCount)

# Calculate percentage of diabetic patients
diabetePerc = (diabeteCount / totalRecords) * 100
print("Percentage of Diabetic Patients:", diabetePerc, "%")

# Diabetes cases by age group
diabeteAge = data.groupby('Age')['Outcome'].sum()
print("Diabetes Cases by Age:\n", diabeteAge)

# Calculate average BMI for diabetic vs. non-diabetic patients
avg_bmi = data.groupby("Outcome")["BMI"].mean()
print("Average BMI by Diabetes Outcome:\n", avg_bmi)

# Analyze blood glucose levels for diabetic vs. non-diabetic patients
glucose_stats = data.groupby("Outcome")["Glucose"].describe()
print("\nBlood Glucose Statistics by Diabetes Outcome:\n", glucose_stats)