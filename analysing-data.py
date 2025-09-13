#Task 1: Load and Explore the Dataset
import pandas as pd
import matplotlib.pyplot as plt

try:
    #Read the CSV file directly with pandas
    df = pd.read_csv('school_data.csv')
    print("File loaded successfully.")
except FileNotFoundError:
    print("File not found. Please Check the filname")
    df = None #makes sure df exists to prevent crashes

# Only proceed if df was successfully loaded
if df is not None:
# First few rows
    print(df.head())

# Missing values per column
print(df.isnull().sum())


#Task 2: Basic Data Analysis

#Number 1
# Compute the basic statistics of the 
# numerical columns (e.g., mean, median, 
# standard deviation) using .describe().
print(df.describe())

#Number 2
#Perform groupings on a categorical column 
# (for example, species, region, or department)
#  and compute the mean of a numerical column for 
# each group.

#filtering rows where age is 15
df_15 = df[df['Age'] == 15]

#Grouping by Name,Age and Grade
grouped = df_15.groupby(['Name','Age','Grade']).agg({'Math': 'mean'})
print(grouped)


#Number 3
#Create at least four different types of visualizations
#Line chart

# Filter for Grade 10 only
df_grade10 = df[df['Grade'] == 10]

# Line chart Plot
plt.plot(df_grade10['Grade'], df_grade10['Math'], marker='o', label='Grade 10 Math')

plt.xlabel('Grade 10')
plt.ylabel('Math Score')
plt.title('Math performance across grade 10')
plt.legend('Grade 10 Math')
plt.show()

#Observation: Most grade 10 students score between 75-80 math scores


#Bar chart
df.groupby('Math')['Age'].mean().plot(kind='bar')
plt.xlabel('Math')
plt.ylabel('Average age')
plt.title('Math performance by Average Age')
plt.show()
#Observation: ges 15 and above are the best performing in Math

#Histogram
df['Age'].plot(kind='hist', bins=10)
plt.xlabel('Age')
plt.title('Number of individuls in each age')
plt.show()
#Observation: The school has more students around the age of 14 years old

#scatter plot
df.plot(kind='scatter', x='English', y='studentID')
plt.title('Student performance per individual')
plt.show()
#Observation: Many students scored between 85 and 90 in English