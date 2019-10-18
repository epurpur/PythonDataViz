#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:04:04 2019

@author: ep9k
"""

import pandas as pd
import matplotlib.pyplot as plt     #I am pretty sure pyplot is the original functionality of matplotlib
import matplotlib.ticker as ticker

#read data from the csv file into an object called 'df'
df = pd.read_csv("MikeTroutData.csv")

#first let's take a look at the data frame to see that it read correctly
#print(df)

#prints just the keys of the 
#print(df.keys())

#Access the columns of the pandas data frame like this
#This is basically the same syntax as a python dictionary
#print(df['Year'])

year = df['Year']
hits = df['H']
at_bats = df['AB']
home_runs = df['HR']
salary = df['Salary']

#Our first simple plot. Let's Plot the year and the # of hits
#plt.bar(year, hits)




#This is nice, but lets add some more labels
#plt.xlabel('Year')
#plt.ylabel('# of Hits')           
#plt.suptitle('Mike Trout Hits per year')
#plt.bar(year, hits)


#Or we can turn this horizontal using plt.barh()
#plt.xlabel('# of Hits')
#plt.ylabel('Year')
#plt.suptitle('Mike Trout Hits per year')
#plt.barh(year, hits, color='red')


#We can do a simple line plot
#plt.xlabel('Year')
#plt.ylabel('# of Hits')
#plt.grid()
#plt.plot(year, hits)


#You can stick them together. Except now our old labels don't work any more
#plt.xlabel('Year')
#plt.ylabel('# of Hits')
#plt.plot(year, at_bats, color='red')
#plt.bar(year, hits)


#A legend is probably what we are looking for!
#plt.xlabel('Year')
#plt.plot(year, at_bats, color='red', label='At Bats')
#plt.bar(year, hits, label='Hits')
#plt.legend()         #makes the legend happen!


#You can do a stacked bar chart using plt.bar()
#plt.xlabel('Year')
#plt.bar(year, hits, label='Hits')
#plt.bar(year, home_runs, label='Home Runs')
#plt.legend()


#You can do a grouped bar chart also using plt.bar()
#but we must move the 2nd bar, so it doesn't sit on top of the first
#plt.xlabel('Year')
#plt.xticks(rotation=45)
#plt.xticks(year)                #shows all years in label

#plt.bar(year, hits, width=.2, label='Hits')
#plt.bar(year+.2, home_runs, width=.2, label='Home Runs')
#plt.legend()


#How about if I want to see the exact number of hits per year? I can add annotation to my objects
#plt.xlabel('Year')
#plt.xticks(rotation=45)
#plt.xticks(year)                #shows all years in label
#
#plt.ylabel('# of Hits')           
#plt.suptitle('Mike Trout Hits per year')
#
#for bar in plt.bar(year, hits):        
#    plt.text(bar.get_x() + .4,              #x position of label
#             bar.get_height() - 20,           #y position of label
#             bar.get_height(),              #actual value of label
#             ha='center',
#             va='bottom')



#Remember, you can do math with your pandas dataframe objects
cost_per_home_run = salary/home_runs

plt.xlabel('Year')
plt.xticks(rotation=45)
plt.xticks(year)     

####START HERE, CHANGE Y AXIS TO BE DOLLAR AMOUNT
fig, ax = plt.subplots()
formatter = ticker.FormatStrFormatter('$%1.0f')
ax.yaxis.set_major_formatter(formatter)

plt.ylabel('Price')           
plt.suptitle('Mike Trout Yearly Cost Per Home Run')
plt.bar(year, cost_per_home_run)



