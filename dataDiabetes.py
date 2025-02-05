import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#first we need to get the data as a csv, excel or json file
#then look over the columns and understand the data 

#read the csv file 
data = pd.read_csv('diabetes.csv', encoding='latin1') 

print(data.head())

#find total records
totalRecords = data['Age'].count()

print(totalRecords)

#find min and max on the columns
print(data.describe())

#find average on the columns

average = data.sum() / totalRecords

print(average)

#patients with diabetes so where outcome is 1 
diabeteCount = data[data['Outcome'] == 1].count()

print(diabeteCount)


diabetePerc = (diabeteCount / totalRecords) * 100

print(diabetePerc)

#diabetes by age group 
diabeteAge = data.groupby('Age')['Outcome'].count()

print(diabeteAge)

