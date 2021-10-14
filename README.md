
# Note to Self - next time update and use Mito? : https://trymito.io/


# Python Data Analysis and Visualization using Pandas + Matplotlib



## **About Me**

Erich Purpur

    Research Librarian for Science & Engineering
    epurpur@virginia.edu
    Brown Science & Engineering Library room I046


I'm a part of a group called [research data services](https://data.library.virginia.edu/) and I do these things:
    
    1. Serve as Liaison to various engineering and social sciences departments
    2. Teach workshops and classes (like this one)
    3. Help people with research projects
    4. Internal Library Projects
    5. Random other things as they come up
    
## **Upcoming Workshops**

More Information Available here: https://data.library.virginia.edu/training/#py

  - Version control with Git and Github  |  9/21  |  10:00 - 11:30am
  - Python and APIs                      |  9/22  |  10:00 - 12:00pm
  - Python Web Scraping                  |  9/29  |  10:00 - 12:00pm
    
    
## **Background**
I can't think of a research project, class assignment, or other kind of analysis that doesn't involve data.  Can you? 

In this workshop today we will be walking through the steps of using python to read a dataset and manipulate it. This involves working it into the shape and size we like before looking at it in a meaningful way. (ie: visualizing the data)

Data visualization is the act of taking information (data) and placing it into a visual context, such as a map or graph. Data 
visualizations make data easier for the human brain to understand. You can more easily detect patterns, trends, and outliers 
in groups of data. 

Good data visualizations should give meaning to your data and clearly communicate what is happening in your analysis. Excel 
has been a go-to data visualization tool for many years. Often, data visualization does not need to be fancy. As long as your 
audience understands your work, it is effective data visualization.

## **Pandas**
*[Pandas Homepage](https://pandas.pydata.org/)*

Pandas is an open source python library providing high-performance, easy-to-use data structures and data analysis tools. We 
will be using pandas to work with our data before feeding it into matplotlib.

## **Matplotlib**
*Excerpt taken from [MatPlotLib's Website](https://matplotlib.org/):*

Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and 
interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the 
Jupyter notebook, web application servers, and four graphical user interface toolkits.

Matplotlib tries to make easy things easy and hard things possible. You can generate plots, histograms, power spectra, bar 
charts, errorcharts, scatterplots, etc., with just a few lines of code.

*From [MatPlotLib's Wikipedia page](https://en.wikipedia.org/wiki/Matplotlib):*
Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It 
provides an object-oriented API for embedding plots into applications

## **Matplotlib History**
*From this [github blog](http://jakevdp.github.io/blog/2013/03/23/matplotlib-and-the-future-of-visualization-in-python/):*

Matplotlib was conceived by John Hunter in 2002, originally as a patch to IPython to enable interactive MATLAB-style plotting 
via the IPython command line. Version 0.1 of Matplotlib was released in 2003. It became the plotting package of choice by the 
Space Telescope Science Institute, which financially supported Matplotlib's development at that time. 

Matplotlib currently has a large, active developer base, and is now widely used in the scientific Python world. 
But, it is not the only data visualization tool available!

## **ggplot for python**
[ggplot Homepage](http://ggplot.yhathq.com/)

The ggplot python library evolved out of the ggplot2 R-specific package. It seems to be accepted that ggplot2 (in R) is a 
more sophisticated graphics tool and provides more high end functionality. It is not clear to me if ggplot for python 
integrates all the functionality that ggplot2 has in R. 

## **Seaborn**
*[Seaborn Homepage](https://seaborn.pydata.org/)*

Seaborn is a python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive 
and informative statistical graphics. Seems to be accepted as an extension to matplotlib functionality, particularly for 
statistical visualization.

## **Bokeh**
*[Bokeh Homepage](https://docs.bokeh.org/en/latest/index.html)*

Bokeh is different in that it does not depend on matplotlib and is geared toward generating visualizations in the web 
browser. It is meant to make interactive web visualizations.  

## **Which one should I use?**

There is no right or wrong answer. It depends what you are doing, what you are familiar with, or other influences in your 
life. Matplotlib is a good jack of all trades package for relatively basic plotting and graphing. It also integrates nicely with numpy and pandas, two other very common scientific packages. 

All these packages have large user communities and good documentation. My advice is to choose one you like and stick with it 
unless you find it does not have the functionality you are looking for.

Reasons to use any given data visualization package/tool in python:
1. You are already familiar with it
2. Your advisor/professor already likes one and you live with that decision
3. You inherited code that is already using that package
4. You found a code example you liked online for a specific package


## **Anaconda**
*[Anaconda Homepage](https://www.anaconda.com/)*

A freely available software distribution containing various data science softwares and accompanying libraries. Inside are Spyder (IDE), R Studio, Jupyter Notebooks, Jupyter Lab, etc.

## **Jupyter Notebook/JupyterLab**
*[Jupyter Homepage](https://jupyter.org/)*

Another topic to cover is Jupyter Notebooks and/or JupyterLab. 
Jupyter Notebooks are a web-based interactive computational environment for creating notebook-like documents. It supports 
several languages like python, R, Julia, etc.
JupyterLab is the next generation user interface, which includes Jupyter Notebooks. 

In my opinion, they seem almost exactly the same. We will be using Jupyter Notebooks today.

## **Self Help - You don't need to remember all of this!**

Honestly, you don't need to remember any of it. Here are the resources I use when looking for answers:

[Matplotlib Documentation](https://matplotlib.org/3.1.1/index.html)

[Stack Overflow](https://stackoverflow.com/) is a huge user community Q&A type site. Odds are very high that someone has 
asked your question before, just google something like "how to make scatter plot matlplotlib python". I'm pretty certain a 
StackOverflow thread will be one of the first few search results

*Stack Overflow Etiquette*
Don't just ask questions right away. Odds are high that for widely used packages, like matplotlib, a question and answer 
already exists. It is good practice to use that (and upvote it) if you like the answer. 

If you do ask a question, make sure it is specific and reproducible. People will downvote you and moderators will close the 
question if it is vague, incoherent, not-reproducible, or not clear in some other way. StackOverflow's purpose is to act as 
a reference guide, not as a forum to debate open ended questions such as "what is better, matplotlib or ggplot?". Go on 
Reddit if you want to do that. 
