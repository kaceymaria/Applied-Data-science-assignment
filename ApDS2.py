# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:00:56 2022

@author: Use
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""

This function manipulate the world bank climate data using pandas dataframes
    Args:
        filename(str): this is the name of the file to read the data from.
        countries: some selected countries to compare
        columns: the columns to be returned.
        indicators: these are the bases on which the comparisom are done 
    Returns:
        dataframe[pandas.core.frame.DataFrame]: A dataframe containing the worldbank data.

"""

def extract(filename,countries,columns,indicator):
    #from the files, gets the data from the countries with specified indicators
    
    df = pd.read_csv(filename,skiprows=4)
    #returns the dataframe of the files, skipping the first four rows not needed
    
    df = df[df['Indicator Name'] == indicator]
    #from the file,returns the dataframe indicator name as a dataframe
    df = df[columns]
    
    #returns the dataframe as columns
    df.set_index('Country Name', inplace = True)
    
    df = df.loc[countries]
    #returns the countries location as dataframe
    
    return df,df.transpose()
#returns the dataframe as the transposed version

filename = 'API_19_DS2_en_csv_v2_4700503.csv'
countries = ['Angola','Ghana','Nigeria','Vietnam','Cameroon']
columns = ['Country Name' ,'2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
indicators = ['Population growth (annual %)', 'Cereal yield (kg per hectare)', 'Access to electricity (% of population)', 'Mortality rate, under-5 (per 1,000 live births)', 'Methane emissions (kt of CO2 equivalent)', 'Urban population']

cout_pop_growth,year_pop_growth = extract(filename,countries,columns,indicators[0])
cout_cereal_yield,year_cereal_yield = extract(filename,countries,columns,indicators[1])
cout_access_elect,year_access_elect = extract(filename,countries,columns,indicators[2])
cout_mort_rate,year_mort_rate = extract(filename,countries,columns,indicators[3])
cout_Meth_emissions,year_Meth_emissions = extract(filename,countries,columns,indicators[4])
cout_urb_pop,year_urb_pop = extract(filename,countries,columns,indicators[5])

#returns the transposed dataframe of the listed countries annual% population growth with country as column 
year_pop_growth

#returns the transposed dataframe of selected countries population growth with year as columns
cout_pop_growth


#returns the transposed dataframe of selected countries cereal yield with countries as columns
year_cereal_yield 


#returns the transposed dataframe of the selected countries with year as columns
cout_cereal_yield


#returns the transposed dataframe of the selected countries with countries as columns
year_access_elect

#this returns the transposed dataframe of countries access to electricity
cout_access_elect

#returns the transposed dataframe of countries urban population growth with countries as columns
year_urb_pop

#returns the transposed dataframes of countries urban population with years as columns
cout_urb_pop

# checks and returns the statistics properties of each of the countries population growth against the years
print(cout_pop_growth.describe())

#checks and returns statistics properties of the countries cereal yield against the years 
print(cout_cereal_yield.describe())

def multiple_line_plot(x_data, y_data, xlabel, ylabel, title, labels, colors):
    '''
    This function defines multiple line plot, below are the attributes
    x_data: this uses years of the indicator to state the index
    y_data: this uses country of the indicator
    xlabel: label for x-axis
    ylabel: label for y-axis
    title:  shows the title of the plot
    labels: these are the labels of each line plot y the legend function
    colors: the colours for each representation
    
    '''
    plt.figure(figsize=(12,7))
    plt.title(title, fontsize=20)
    for i in range(len(y_data)): # this produces choice of plot by looping over the dataframe
        plt.plot(x_data, y_data[i], label=labels[i], color=colors[i])
    plt.xlabel(xlabel, fontsize=20)
    plt.ylabel(ylabel, fontsize=20)
    plt.legend(bbox_to_anchor=(1,1))
    plt.show()
    return

# parameters for plotting multiple line plot of population growth (annual %)
x_data = year_pop_growth.index #this returns the row index as the value of x axis 
y_data = [year_pop_growth['Angola'],
          year_pop_growth['Ghana'],
          year_pop_growth['Nigeria'],
          year_pop_growth['Vietnam'],
          year_pop_growth['Cameroon']]
#labels the x-axis as year
xlabel = 'year'

#labels the y-axis as population growth by annual percentage
ylabel = 'Population Growth(annual %)'

#shows the keys to identify the countries
labels = ['Angola','Ghana','NIgeria','Vietnam','Cameroon']

#shows the color identifier for the countries
colors = ['blue', 'red', 'black', 'green', 'purple']

#plots the title of the line graph
title = 'Population Growth (annual %) for 5 countries'

# the above attribute are passed into the function to give desired plot
multiple_line_plot(x_data, y_data, xlabel, ylabel, title, labels, colors)

def multiple_line_plot(x_data, y_data, xlabel, ylabel, title, labels, colors):
    '''
    This function defines multiple line plot, below are the attributes
    x_data: this uses years of the indicator to state the index
    y_data: this uses country of the indicator
    xlabel: label for x-axis
    ylabel: label for y-axis
    title:  shows the title of the plot
    labels: these are the labels of each line plot y the legend function
    colors: the colours for each representation
    
    '''
    plt.figure(figsize=(12,7))
    plt.title(title, fontsize=20)
    for i in range(len(y_data)): # this produces choice of plot by looping over the dataframe
        plt.plot(x_data, y_data[i], label=labels[i], color=colors[i])
    plt.xlabel(xlabel, fontsize=20)
    plt.ylabel(ylabel, fontsize=20)
    plt.legend(bbox_to_anchor=(1,1))
    plt.show()
    return

# parameters for plotting multiple line plot of these countries Access to electricity (% of population) from 2010 t0 2020
x_data = year_access_elect.index #this returns the row index as the value of x axis 
y_data = [year_access_elect['Angola'],
          year_access_elect['Ghana'],
          year_access_elect['Nigeria'],
          year_access_elect['Vietnam'],
          year_access_elect['Cameroon']]
xlabel = 'year'
ylabel = 'Access to electricity (% of population)'
labels = ['Angola','Ghana','NIgeria','Vietnam','Cameroon']
colors = ['blue', 'red', 'black', 'green', 'purple']
title = 'Access to electricity (% of population)'

# the above attribute are passed into the function to give desired plot
multiple_line_plot(x_data, y_data, xlabel, ylabel, title, labels, colors)




















