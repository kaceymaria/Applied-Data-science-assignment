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