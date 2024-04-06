# analysis.py
# This project is for the programme and scripting module in the Higher Diploma in Science in Data Analytics
# It is based on the Fisher's Iris Data Set
# Author Grainne Boyle

from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 
  
# metadata 
print(iris.metadata) 
  
# variable information 
print(iris.variables) 

# The first step is to import Pandas, a python library used for working with datasets



import pandas as pd

# Next I load the Iris data set into a data frame using df in pandas
