from tkinter import *
from tkinter import ttk

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def read_msg(type_,year_):
    if type_=="" and year_=="":
        return 'please enter: \ntype and year to read' , 'red'
    elif type_ =="":
        return 'please enter: \ntype to read' ,'red'
    elif year_=="":
        return 'please enter: \nyear to read','red'
    else:
        return 'Read '+type_+" "+year_ ,'green'

    

def sort_msg(type_,year_):

    if type_=="" and year_=="":
        return 'please enter: \ntype and year to sort','red'
    elif type_ =="":
        return 'please enter: \ntype to sort' ,'red'
    elif year_=="":
        return 'please enter: \nyear to sort' , 'red'
    else:
        return 'Sorted '+type_+" "+year_, 'green'
    
    

def analysis_msg(type_,year_):

    if type_=="" and year_=="":
        return 'please enter: \ntype and year to analyze','red'
    elif type_ =="":
        return 'please enter: \ntype to analyze','red'
    elif year_=="":
        return 'please enter: \nyear to analyze' , 'red'
    else:
        return 'Analyzed '+type_+" "+year_ , 'green'
    
    

def map_msg (type_,year_):
    
    if type_=="" and year_=="":
        return 'please enter: \ntype and year to map','red'
    elif type_ =="":
        return 'please enter: \ntype to map','red'
    elif year_=="":
        return 'please enter: \nyear to map','red'
    else:
        return 'Mapped '+type_+" "+year_,'green'
    
    

def read_func(type_,year_):

    #header to print to gui
    if type_== 'Traffic Volume':
        header =["year", "secname", "the_geom", "shape_leng", "volume"]
    elif type_ == 'Accidents':
        header =["incident info", "description", "start_dt", "modified_dt", "quadrant", "longitude", "latitude", "location", "count"]

    return header

def sort_func(type_,year_):
    
    #header to print to gui
    if type_== 'Traffic Volume':
        header =["year", "secname", "the_geom", "shape_leng", "volume"]
    elif type_ == 'Accidents':
        header =["incident info", "description", "start_dt", "modified_dt", "quadrant", "longitude", "latitude", "location", "count"]

    return header
        

def analysis_func(type_,year_):

    # TO be Removed and replaced with database plot, must return figure to plot
    #here
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
        title='About as simple as it gets, folks')

    #to here defines the figure to display

    return fig 
    


values = np.arange(0, 2500, 500)
value_increment = 1000


def map_func(type_,year_):
    pass
    