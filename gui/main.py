from tkinter import *
from tkinter import ttk
from analysis_commands import *

#window design
root = Tk()
root.title('Calgary Traffic Database')
root.geometry("1000x500")

left = Frame(root, width=150, borderwidth=1, relief="solid")
right = Frame(root, width=750, borderwidth=1, relief="solid")
Status = Frame(left, borderwidth=1, relief="solid")

Year_values=['2016','2017','2018']
Type_values=['Accidents','Traffic Volume']

Type_label = Label(left, text="Type",anchor=W,justify=LEFT)
CB_type=ttk.Combobox(left, justify=LEFT,value= Type_values)

Year_label = Label(left, text="Year",anchor=W,justify=LEFT)
CB_year=ttk.Combobox(left, justify=LEFT,value= Year_values)

Status_out=Label(Status)

Button_read=Button(left,text="Read", padx=50,pady=10,command=lambda: read_click(CB_type.get(),CB_year.get()))
Button_sort=Button(left,text="Sort", padx=50,pady=10,command=lambda:  sort_click(CB_type.get(),CB_year.get()))
Button_analysis=Button(left,text="Analysis",padx=50,pady=10,command=lambda: analysis_click(CB_type.get(),CB_year.get()))
Button_map=Button(left,text="Map", padx=50,pady=10,command=lambda: view_map_click(CB_type.get(),CB_year.get()))

def read_click(type_,year_):

    #Calls function and updates Status
    global Status_out
    Status_out.destroy()
    Message = read_func(type_,year_)
    Status_out=Label(Status,text=Message,anchor=W,justify=LEFT)
    Status_out.pack(fill='x')

def sort_click(type_,year_):

    #Calls function and updates Status
    global Status_out
    Status_out.destroy()
    Message= sort_func(type_,year_)
    Status_out=Label(Status,text=Message,anchor=W,justify=LEFT)
    Status_out.pack(fill='x')

def analysis_click(type_,year_):

    #Calls function and updates Status
    global Status_out
    Status_out.destroy()
    Message= analysis_func(type_,year_)
    Status_out=Label(Status,text=Message,anchor=W,justify=LEFT)
    Status_out.pack(fill='x')

def view_map_click(type_,year_):

    #Calls function and updates Status
    global Status_out
    Status_out.destroy()
    Message = map_func(type_,year_)
    Status_out=Label(Status,text=Message,anchor=W,justify=LEFT)
    Status_out.pack(fill='x')

Status_label = Label(left, text="Status:",anchor=W,justify=LEFT)

Type_label.pack(fill='x')
CB_type.pack(fill='x')
Year_label.pack(fill='x')
CB_year.pack(fill='x')

Button_read.pack(fill='x')
Button_sort.pack(fill='x')
Button_analysis.pack(fill='x')
Button_map.pack(fill='x')

Status_label.pack(fill='x')
Status.pack(expand=True, fill="both", padx=5, pady=5)

left.pack(side="left", expand=True, fill="both")
right.pack(side="right", expand=True, fill="both")

root.mainloop()