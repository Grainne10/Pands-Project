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
# Gives youa brief overview of the data by columns, count, types
#print(df.info())
# Brief description of the count, mean, std dev, min
print(df.describe())
# This will show if there are missing data and it shows there are no missing values
print(df.isnull())
# This will show you the type of data that you are analysing,  in this case as the numbers are fractitional it detects they are floating numbers.
print(df.dtypes)
# To show the petal length, it will show the first and last five
plen = df['petal_length']
# Show
print(plen)
# type
print(type(plen))

# to get the numpy array
plen.to_numpy()
# The data set is clean, has no missing values and is ready for analysis.

