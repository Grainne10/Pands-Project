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

# Output a summary of the each variables to a single text file.

from io import StringIO

# Capture the output of df.info() into a string - for this String IO section, I could not find why the info section would not print to the file
# So I looked it up on chat GPT and it suggested using this. I did further research and added it to the readme file. 
# Without this it was printing to code rather than returning a value to the file. 
#StringIO allows you to treat strings like file-like objects and captures the output of your dataframe info as a string
buffer = StringIO()
df.info(buf=buffer)
info_output = buffer.getvalue()
buffer.close()

# This section I created myself .

with open(r"iris_summary.txt", "w") as f:

    describe = str(df.describe())
    info = str(df.info()) 
    null = str(df.isnull().sum)
    summary =  info_output + "\n\n" + describe + "\n\n" + null

    # Write the summary to the file
    f.write(summary)



# The data set is clean, has no missing values and is ready for analysis.



# We will look at how some of these individual variables look different charts and plots.
# In order to do this, we must import matplotlib, it is a library for data visualization.
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt


# We will install Numpy

import numpy as np





# Seaborn can be imported and used by matplotlib to draw its plots
import seaborn as sns
# We can pull in the colour palette from seaborn and set our colours to distinguish the different iris species.

#To ignore warnings, re: the figure layout changes, we import the warnings module
import warnings
warnings.filterwarnings('ignore')


# Draw a scatterplot of the sepal length vs sepal width and show the plots in different shapes to identify them clearly
sns.scatterplot(df, x="sepal_length", y="sepal_width", hue="species", style="species", markers={"setosa": "^", "versicolor": "s", "virginica": "o"})
plt.title("Scatter Plot of Sepal Length vs. Sepal Width")
plt.xlabel("Sepal Length (Cm) ")
plt.ylabel("Sepal Width (Cm) ")
plt.legend(loc='upper right', bbox_to_anchor=(1.30, 1))
plt.savefig('Scatter plot of Sepal Length vs Sepal Width ', bbox_inches='tight')
plt.show()# Show a boxplot of the four variables

sns.scatterplot(df, x="petal_length", y="petal_width", hue="species", style="species", markers={"setosa": "^", "versicolor": "s", "virginica": "o"})
plt.title("Scatter Plot of Peta Length vs. Petal Width")
plt.xlabel("Petal Length (Cm) ")
plt.ylabel("Petal Width (Cm) ")
plt.legend(loc='upper right', bbox_to_anchor=(1.30, 1)) 
plt.savefig('Scatter plot of Petal Length vs Petal Width ', bbox_inches='tight')
plt.show()

# Show the variable in a pairplot using seaborn. This shows the scatter plots and kernal density plots for all variables
sns.pairplot(df, hue="species", markers=["o", "s", "^"])
plt.suptitle("Pairplot of Iris Dataset", y=1.02)
plt.savefig('Pairplot of Iris Dataset', bbox_inches='tight')
plt.show()



# From the scatterplot, 
# We can show the scatterplots separately using facet grids:

g = sns.FacetGrid(df, col="species",  hue="species", height=5, aspect=1.2)
g.map(sns.scatterplot, "sepal_length", "sepal_width")
g.set_axis_labels("Sepal Length (cm)", "Sepal Width (cm)")
g.set_titles("{col_name}")

plt.subplots_adjust(top=0.85) 
plt.suptitle("Facet Grid Sepal Length  vs. Sepal Width ", fontsize=18)
plt.savefig('Facet Grid Scatter plot of Sepal Length vs Sepal Width of Iris Species', bbox_inches='tight')
plt.show()

g = sns.FacetGrid(df, col="species",  hue="species", height=5, aspect=1.2)
g.map(sns.scatterplot, "petal_length", "petal_width")
g.set_axis_labels("Petal Length (cm)", "Petal Width (cm)")
g.set_titles("{col_name}")

plt.subplots_adjust(top=0.85) 
plt.suptitle("Facet Grid Petal Length  vs. Petal Width ", fontsize=18)
plt.savefig('Facet Grid Scatter plot of Petal Length vs Petal Width of Iris Species', bbox_inches='tight')
plt.show()



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

# To show correlation coefficient for numeric values we can use do a matrix. Select only numeric columns for correlation calculation
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Calculate correlation matrix
correlation_matrix = numeric_df.corr()

# Print correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# We can use the correlation matrix to plot a heatmap
# We can use annot to show the values and fmt for decimal places
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='YlGnBu', fmt=".2f", linewidths=0.5) 
plt.title('Correlation Heatmap of Iris Dataset Variables')
plt.savefig('Iris DataSet HeatMap')
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
