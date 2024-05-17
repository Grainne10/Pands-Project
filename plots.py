# Set up modules to import into main analysis.py file
# Author: Grainne Boyle

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
import seaborn as sns
import matplotlib.pyplot as plt


def scatter1(df):
    sns.scatterplot(df, x="sepal_length", y="sepal_width", hue="species", style="species", markers={"setosa": "^", "versicolor": "s", "virginica": "o"})
    plt.title("Iris Dataset Scatter Plot of Sepal Length vs. Sepal Width")
    plt.xlabel("Sepal Length (Cm) ")
    plt.ylabel("Sepal Width (Cm) ")
    plt.legend(loc='upper right', bbox_to_anchor=(1.30, 1))
    plt.savefig('Scatter plot of Sepal Length vs Sepal Width ', bbox_inches='tight')
    plt.show()

scatter1(df)
  


def scatter2(df):
    sns.scatterplot(df, x="petal_length", y="petal_width", hue="species", style="species", markers={"setosa": "^", "versicolor": "s", "virginica": "o"})
    plt.title("Iris Dataset Scatter Plot of Petal Length vs. Petal Width")
    plt.xlabel("Petal Length (Cm) ")
    plt.ylabel("Petal Width (Cm) ")
    plt.legend(loc='upper right', bbox_to_anchor=(1.30, 1)) 
    plt.savefig('Scatter plot of Petal Length vs Petal Width ', bbox_inches='tight')
    plt.show()
   
scatter2(df)

def facetgrid1(df):
    g = sns.FacetGrid(df, col="species",  hue="species", height=5, aspect=1.2)
    g.map(sns.scatterplot, "sepal_length", "sepal_width")
    g.map(sns.regplot, "sepal_length", "sepal_width", scatter=False)
    g.set_axis_labels("Sepal Length (cm)", "Sepal Width (cm)")
    g.set_titles("{col_name}")
    plt.subplots_adjust(top=0.85) 
    plt.suptitle("Iris Dataset Facet Grid Sepal Length vs. Sepal Width ", fontsize=18)
    plt.savefig('Facet Grid of Sepal Length vs Sepal Width', bbox_inches='tight')
    plt.show()

facetgrid1(df)

def facetgrid2(df):
    g = sns.FacetGrid(df, col="species",  hue="species", height=5, aspect=1.2)
    g.map(sns.scatterplot, "petal_length", "petal_width")
    g.map(sns.regplot, "petal_length", "petal_width", scatter=False)
    g.set_axis_labels("Petal Length (cm)", "Petal Width (cm)")
    g.set_titles("{col_name}")
    plt.subplots_adjust(top=0.85) 
    plt.suptitle("Iris Dataset Facet Grid Petal Length  vs. Petal Width ", fontsize=18)
    plt.savefig('Facet Grid Scatter plot of Petal Length vs Petal Width', bbox_inches='tight')
    plt.show()

facetgrid2(df)  

def pairplot(df):

    sns.pairplot(df, hue="species", markers=["o", "s", "^"])
    plt.suptitle("Iris Dataset Pairplot", y=1.02)
    plt.savefig('Pairplot of Iris Dataset', bbox_inches='tight')
    plt.show()

pairplot(df)

def histogram1(df):
    plt.figure(figsize=(6, 6))
    sns.histplot(df, x='sepal_length', hue="species", edgecolor = "white", multiple="layer", kde=True, bins=18, alpha=0.3)
    plt.title('Iris Dataset Histogram Sepal Length')
    plt.legend
    plt.xlabel('Sepal Length')
    plt.ylabel('Count')
    plt.xticks(rotation=45) 
    plt.savefig('Histogram Sepal Length')
    plt.show()

histogram1(df)

def histogram2(df):
    plt.figure(figsize=(6, 6))
    sns.histplot(df, x='sepal_width', hue="species", edgecolor = "white", multiple="layer", kde=True, bins=16, alpha=0.3)
    plt.title('Iris Dataset Histogram Sepal Width')
    plt.legend
    plt.xlabel('Sepal Width')
    plt.ylabel('Count')
    plt.savefig('Histogram Sepal Width')
    plt.show()

histogram2(df)
   
def histogram3(df):
    plt.figure(figsize=(6, 6))
    sns.histplot(df, x='petal_length', hue="species", edgecolor = "white", multiple="layer", kde=True, bins=18, alpha=0.3)
    plt.title('Iris Dataset Histogram Petal Length')
    plt.legend
    plt.xlabel('Petal Length')
    plt.ylabel('Count')
    plt.savefig('Histogram Petal Length')
    plt.show()
   
histogram3(df)

def histogram4(df):
    plt.figure(figsize=(6, 6))
    sns.histplot(df, x='petal_length', hue="species", edgecolor = "white", multiple="layer", kde=True, bins=18, alpha=0.3)
    plt.title('Iris Dataset Histogram Petal Width')
    plt.legend
    plt.xlabel('Petal Width')
    plt.ylabel('Count')
    plt.savefig('Histogram Petal Width')
    plt.show()
    
histogram4(df)

def boxplot(df):

    plt.figure(figsize=(10, 8))
    sns.boxplot(data=df, orient="v", palette="Set2")
    plt.ylabel('Measurement (cm)')
    plt.title('Iris Dataset Box Plot')
    plt.savefig('Box Plot of Iris Dataset')
    plt.show()

boxplot(df)

# To show correlation coefficient for numeric values we can use do a matrix. Select only numeric columns for correlation calculation
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Calculate correlation matrix
correlation_matrix = numeric_df.corr()

def heatmap(df):
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='YlGnBu', fmt=".2f", linewidths=0.5) 
    plt.title('Correlation Heatmap of Iris Dataset Variables')
    plt.savefig('Iris DataSet HeatMap')
    plt.show()
       
heatmap(df)   

def violin(df):

    fig, axes = plt.subplots(2, 2, figsize=(18, 10))
    fig.suptitle('Iris Data Set Violin Plots')
    sns.violinplot(df, x='species', y='sepal_length', ax=axes[0, 0] )
    sns.violinplot(df, x='species', y='sepal_width', ax=axes[0, 1] )
    sns.violinplot(df, x='species', y='petal_length', ax=axes[1, 0] )
    sns.violinplot(df, x='species', y='petal_width', ax=axes[1, 1])
    plt.savefig('Iris DataSet Violin Plots')
    plt.show()

violin(df)

def andrewscurves(df):

    plt.figure(figsize=(10, 8))
    pd.plotting.andrews_curves(df, 'species', colormap='plasma')
    plt.title('Iris Dataset Andrews Curves')
    plt.legend(loc='upper right')
    plt.savefig('Iris DataSet Andrews Curves')
    plt.show()

andrewscurves(df)



   
