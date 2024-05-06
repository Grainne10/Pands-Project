# analysis.py
# This project is for the programme and scripting module in the Higher Diploma in Science in Data Analytics
# It is based on the Fisher's Iris Data Set
# Author Grainne Boyle

# The first step is to import pandas . Pandas is an open source library used for data analysis and manipulation of data frames/datasets. 

import pandas as pd

# Next I load the Iris data set into a data frame using df in pandas
# A DataFrame is a 2 dimensional data structure, like a 2 dimensional array,or a table with rows and columns.
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

#I do some review of the data, you can remove some of the hashtags to view these
# It gives you a brief overview of the data by columns, count, types
print(df.info())
# Brief description of the count, mean, std dev, min
print(df.describe())
# This will show if there are missing data or if the dataset is complete.  "True" shows that the value is missing in that field.
# There are no missing values.  This is an example of a Boolean.  
print(df.isnull())
# This will show you the type of data that you are analysing. It determines Sepal length, Sepal Width,  Petal Length and Petal Width as the numbers are fractitional it detects they are floating numbers.  
# Species are shown as objects. Typically, objects means that the values in the columns are strings or a mixture of data types. 
print(df.dtypes)
# To show the petal length, it will show the first and last five
plen = df['petal_length']
# Show
print(plen)
# type
print(type(plen))

# to get the numpy array
plen.to_numpy()

# If we want to see the number of each Species column, we can use this:
df["species"].value_counts() 

# The data set is clean, has no missing values and is ready for analysis.

# We will look at how some of these ndividual variables look different charts and plots.
# In order to do this, we must import matplotlib, it is a library for data visualization.
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt


# We will install Numpy

import numpy as np





# Seaborn can be imported and used by matplotlib to draw its plots
import seaborn as sns
# We can pull in the colour palette from seaborn and set our colours to distinguish the different iris species.

# Show a boxplot of the four variables

plt.figure(figsize=(10, 8))
sns.boxplot(data=df, orient="v", palette="Set2")
plt.ylabel('Measurement (cm)')
plt.title('Box Plot of Iris Dataset')
plt.savefig('Box Plot of Iris Dataset')
plt.show()

# Do a histogram of sepal length
plt.figure(figsize=(6, 6))
sns.histplot(df, x='sepal_length', hue="species", edgecolor = "white", multiple="layer", kde=True, bins=18, alpha=0.3)
plt.title('Histogram Sepal Length')
plt.legend
plt.xlabel('Sepal Length')
plt.ylabel('Count')
plt.xticks(rotation=45) 
plt.savefig('Histogram Sepal Length')
plt.show()

# Do a histogram of sepal width
plt.figure(figsize=(6, 6))
sns.histplot(df, x='sepal_width', hue="species", edgecolor = "white", multiple="layer", kde=True, bins=16, alpha=0.3)
plt.title('Histogram Sepal Width')
plt.legend
plt.xlabel('Sepal Width')
plt.ylabel('Count')
plt.savefig('Histogram Sepal Width')
plt.show()

# Do a histogram of petal length
plt.figure(figsize=(6, 6))
sns.histplot(df, x='petal_length', hue="species", edgecolor = "white", multiple="layer", kde=True, bins=18, alpha=0.3)
plt.title('Histogram Petal Length')
plt.legend
plt.xlabel('Petal Length')
plt.ylabel('Count')
plt.savefig('Histogram Petal Length')
plt.show()

# Do a histogram of petal width
plt.figure(figsize=(6, 6))
sns.histplot(df, x='petal_length', hue="species", edgecolor = "white", multiple="layer", kde=True, bins=18, alpha=0.3)
plt.title('Histogram Petal Width')
plt.legend
plt.xlabel('Petal Width')
plt.ylabel('Count')
plt.savefig('Histogram Petal Width')
plt.show()


# Extract data
#data = df.iloc[:, :-1]  # Selecting all rows and all columns except the last one
#feature_names = df.columns[:-1]  # Extracting feature names from DataFrame columns

#plt.figure(figsize=(8, 6))
#plt.boxplot(data, labels=feature_names)
#plt.xlabel('Features')
#plt.ylabel('Feature Values')
#plt.title('Box Plot of Iris Dataset Features')
#plt.grid(True)
#plt.show()
