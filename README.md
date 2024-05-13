# pands-project

**by Grainne Boyle**

I work a [TE Connectivity] (https://www.te.com/usa-en/home.html)

This repository contains the files for the project for the Programme and Scripting module in the Higher Diploma in Science in Data Analytics.

Description
This project is based on the [Iris Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set). For the project I must research the data set and write documentation and code in Python to investigate the data set, with a view to explaining it to my colleagues.I may be asked to give a presentation on the data , where I explain what investigating a data set entails and how Python can be used to do it. 

Python Script
* Read in the Iris Data  CSV from a URL
* Import pandas to work on the data set using data frames
* Create a summary of the data using tables
* Test the data form missing values
* Use Numpy for working with arrays







Background
This project is based on the [Iris Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set). The Fisher’s Iris data set  is a multivariate data set made famous by the statistician and biologist Ronald Fisher. It is sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspe peninsula,  "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus"

The data set consist of 50 samples from each of three species of Iris ris setosa, Iris virginica and Iris versicolor . Four features were measured from each sample: the length and the width of the  sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. 


Analysis


#References
# Code Sources 


# Research
* [Pandas library](https://pypi.org/project/pandas/) - libary for working with data set. It has functions for analysing , cleansing, exploring and manipulating data.
* [Data Frames](https://www.w3schools.com/r/r_data_frames.asp) - Takes a csv file and loads it into a dataframe, which is like a table with rows and columns.
* [CSV Files](https://docs.python.org/3/library/csv.html) - enables the file to be read in a tabular form.
* [Using Numpy](https://numpy.org/doc/stable/user/absolute_beginners.html) - facilitate advanced mathematical and other types of operations on large numbers of data
* [Expoloring the dataset](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/)- shows how to describe the data and uses visualisation through plots and graphs
* [Multivariate Statistics](https://en.wikipedia.org/wiki/Multivariate_statistics) - observations of more than one variable
* [Univariate and Bivariate Analysis](https://www.geeksforgeeks.org/univariate-bivariate-and-multivariate-data-and-its-analysis/) - univariate looks at one variable and bivariate looks at two variables and how thy may be related.
* [Bivariate Analysis](https://www.questionpro.com/blog/bivariate-analysis/) - looks at the visual methods on how we can measure if two variables are related.

* [Medium](https://medium.com/geekculture/8-best-seaborn-visualizations-20143a4b3b2f) - different visualisations you can use
* [Colour Selection](https://matplotlib.org/mpl_examples/color/named_colors.hires.png)
* [Colour Heatmap](https://python-graph-gallery.com/92-control-color-in-seaborn-heatmaps/) - selecting colours for the heatmap 

* [Geeksfor Geeks Histograms](https://www.geeksforgeeks.org/interpretations-of-histogram/) - Interpretations of Histograms
* [W3 Schools matplotlib](https://www.w3schools.com/python/matplotlib_pyplot.asp) - how to plot using matplotlib
* [W3Schools histograms](https://www.w3schools.com/python/matplotlib_histograms.asp) - how to plot histograms.
* [Wikipedia Correlation Coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) describes the linear relationship between x and y. It ranges from −1 to 1. If the value is close to +1 it implies that  if the data points are on a line as the x increases, the y also increases. If the value is close to – 1 , it implies a line where y increases while x decreases.
* [Real Python](https://realpython.com/visualizing-python-plt-scatter/)- This articles shows you how to do a scatterplot and how to change shapes and colours.
* [Facet Grids](https://www.geeksforgeeks.org/python-seaborn-facetgrid-method/) - I seen the idea for the facet grids in some of the research documents , particularly the Rpubs project above and I researched how to do it using geeksforgeeks.
* [Box plots](https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/) -graphical representation of the distribution of a dataset  
* [Pairplots](https://seaborn.pydata.org/generated/seaborn.pairplot.html) - matrix of graphs enables the visualisation of the relationship between each pair os variables in a data set. 
* [Kernal Density Estimate](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) - like a smoother version of a histogram, while kde produces a probability distribution, the height of the curve at each point gives a density not probability.
* [Disable warnings](https://www.geeksforgeeks.org/how-to-disable-python-warnings/) - This shows how to stop showing warnings that appear for plots etc.
* [Seaborn](https://seaborn.pydata.org/generated/seaborn.pairplot.html) - This shows pairplots using all the numerical variables * [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) - Explanation and examples of different kernal density plots.
*[Violin Plots](https://www.geeksforgeeks.org/violin-plot-for-data-analysis/) - Has been described as a hybrid of a box plot and kernal density plot. It can depict summary statistic and density of each variable.
* [Multiplots](https://www.geeksforgeeks.org/multi-plot-grid-in-seaborn/) - how to do a multiplot for the violinplot
* [Real Python](What Does if __name__ == "__main__" Do in Python? – Real Python) - execute code when  file is run from a script, but not when imported as a module.
[Pandas Plot multivariate](https://pandas.pydata.org/docs/user_guide/visualization.html#andrews-curves) - example of multivariate plot.

*[Geeks for Geeks](https://www.geeksforgeeks.org/how-to-automatically-install-required-packages-from-a-python-script/) - showing what requirements are needed to run a script.
* [Lag Plots](https://www.ncss.com/wp-content/themes/ncss/pdf/Procedures/NCSS/Lag_Plots.pdf) - Check to see if suitable for Iris dataset
*[Exploratory Analysis](https://medium.com/@nirajan.acharya666/exploratory-data-analysis-of-iris-dataset-9c0df76771df) - Analysis of the Iris dataset




* ChatGPT - This was used to tidy up and make some improvements on a few of the graphs.




Libraries Used

* Pandas - for the DataFrame data structure. It allows us to investigate CSV files . It is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.

* CSV - (Comma Separated Values) is a simple file format used to store tabular data. 

* NumPy - is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and it facilitates mathematical on large numbers of data. 

* Matplotlib - used for data visualization, typically in the form of plots, graphs and charts.

* Seaborn library - used for visualizing the explorative statistical plots of data.

* Warnings - we tell Panda to ignore future warning message generated by Pandas.



