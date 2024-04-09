# analysis.py
# This project is for the programme and scripting module in the Higher Diploma in Science in Data Analytics
# It is based on the Fisher's Iris Data Set
# Author Grainne Boyle

# The first step is to import pandas . Pandas is an open source library used for data analysis and manipulation of data frames/datasets. 

import pandas as pd

# Next I load the Iris data set into a data frame using df in pandas

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
#print(df.info())
#print(df.describe())
print(df.isnull())
#print(df.head())
#print (df)
#print(df.dtypes)
#print(df.describe)
# To get the petal lengths
#plen = df['petal_length']
# Show
#print(plen)
# type
#print(type(plen))
#just to get the numpy array
#plen.to_numpy()


