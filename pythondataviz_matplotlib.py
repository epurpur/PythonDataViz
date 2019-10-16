#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:04:04 2019

@author: ep9k
"""

import pandas as pd
import matplotlib.pyplot as plt

#read data from the csv file into an object called 'df'
df = pd.read_csv("MikeTroutData.csv")

#first let's take a look at the data frame to see that it read correctly
#print(df)

#prints just the keys of the 
#print(df.keys())

#Access the columns of the pandas data frame like this
#This is basically the same syntax as a python dictionary
print(df['Year'])

year = df['Year']
hits = df['H']

#Our first simple plot. Let's Plot the year and the # of hits
plt.bar(year, hits)


