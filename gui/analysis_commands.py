from tkinter import *
from tkinter import ttk

def read_func(type_,year_):
    if type_=="" and year_=="":
        return 'please enter: \ntype and year to read'
    elif type_ =="":
        return 'please enter: \ntype to read'
    elif year_=="":
        return 'please enter: \nyear to read'
    else:
        return 'Read '+type_+" "+year_
    

def sort_func(type_,year_):

    if type_=="" and year_=="":
        return 'please enter: \ntype and year to sort'
    elif type_ =="":
        return 'please enter: \ntype to sort'
    elif year_=="":
        return 'please enter: \nyear to sort'
    else:
        return 'Sort '+type_+" "+year_
    
    

def analysis_func(type_,year_):

    if type_=="" and year_=="":
        return 'please enter: \ntype and year to analyze'
    elif type_ =="":
        return 'please enter: \ntype to analyze'
    elif year_=="":
        return 'please enter: \nyear to analyze'
    else:
        return 'Analyze '+type_+" "+year_
    
    

def map_func(type_,year_):
    
    if type_=="" and year_=="":
        return 'please enter: \ntype and year to map'
    elif type_ =="":
        return 'please enter: \ntype to map'
    elif year_=="":
        return 'please enter: \nyear to map'
    else:
        return 'Map '+type_+" "+year_
    
    