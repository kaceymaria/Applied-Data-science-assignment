# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 17:27:55 2022

@author: User
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('household_power_consumption.csv')
data  = data.drop('index', axis=1)


data['Global_active_power']=pd.to_numeric(data['Global_active_power'],errors='coerce')
data['Global_reactive_power']=pd.to_numeric(data['Global_reactive_power'],errors='coerce')
data['Voltage']=pd.to_numeric(data['Voltage'],errors='coerce')
data['Global_intensity']=pd.to_numeric(data['Global_intensity'],errors='coerce')
data['Sub_metering_1']=pd.to_numeric(data['Sub_metering_1'],errors='coerce')
data['Sub_metering_2']=pd.to_numeric(data['Sub_metering_2'],errors='coerce')
data['Sub_metering_3']=pd.to_numeric(data['Sub_metering_3'],errors='coerce')


data['date'] = pd.to_datetime(data['Date'])
data['time'] = pd.to_datetime(data['Time'])
data['month'] = pd.DatetimeIndex(data['date']).month

data = data.drop(['Date','Time'],axis=1)

month_group = data.groupby('month')[['Global_active_power', 'Global_reactive_power', 'Voltage','Global_intensity', 'Sub_metering_1', 'Sub_metering_2','Sub_metering_3']].mean()

def line_plot(x_axis,y_list,xticks,label,title):
    '''A function that plots a line plot'''
    plt.figure(figsize=(12,7))
    
    for i in range(len(y_list)):
        plt.plot(x_axis,y_list[i],label=label[i])
       
    plt.legend()
    plt.title(title)
    plt.xticks(x_axis,xticks)
    plt.show() 

xticks = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
label = ['Global_active_power','Global_reactive_power','Global_intensity']
x_axis = month_group.index
y_list = [month_group['Global_active_power'],month_group['Global_reactive_power'],month_group['Global_intensity']]
title = 'A line plot to show the monthly average of global active power, global reactive power, global intensity'
line_plot(x_axis,y_list,xticks,label,title)

def scatter_plot(data,x_axis,y_axis,title,xlabel,ylabel):
    '''A function that plots scatter plot between two variables passed'''
    plt.figure(figsize=(20,15))
    plt.scatter(data=data,x=x_axis,y=y_axis)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


data = data
xlabel = x_axis = 'Global_active_power'
ylabel = y_axis = 'Global_reactive_power'
title = 'A scatter plot to show whether or not there is a relationship between Global Active Power and Global Reactive Power'

scatter_plot(data,x_axis,y_axis,title,xlabel,ylabel)

def bar_subplot(x_axis,y_list,title,xticks):
    
    plt.figure(figsize=(15,7))
    for i in range(len(y_list)):
        plt.subplot(1,3,i+1).set_title(title[i])
        plt.bar(x_axis,y_list[i])
        plt.xticks(x_axis,xticks,rotation=90)
                   
    plt.show()
    
x_axis = month_group.index
y_list = [month_group['Sub_metering_2'],month_group['Sub_metering_2'],month_group['Sub_metering_3']]
xticks = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
title = ['Sub_metering_1','Sub_metering_2','Sub_metering_3']

bar_subplot(x_axis,y_list,title,xticks)


    

