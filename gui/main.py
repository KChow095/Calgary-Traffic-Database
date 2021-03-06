from tkinter import *
from tkinter import ttk
from analysis_commands import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

import numpy as np
import webbrowser
import ReadData as rd
import matplotlib.pyplot as plt

def main():
    #window design
    root = Tk()
    root.title('Calgary Traffic Database')
    root.geometry("1000x600")

    left = Frame(root, width=150, borderwidth=1, relief="solid")
    right = Frame(root, width=750, borderwidth=1, relief="solid")
    global right_canvas
    right_canvas = Frame(right)


    Status = Frame(left, borderwidth=1, relief="solid")

    Year_values=['2016','2017','2018']
    Type_values=['Incidents','Traffic Volume']

    #creat Type and Year ComboBox
    Type_label = Label(left, text="Type",anchor=W,justify=LEFT)
    CB_type=ttk.Combobox(left, justify=LEFT,value= Type_values)

    Year_label = Label(left, text="Year",anchor=W,justify=LEFT)
    CB_year=ttk.Combobox(left, justify=LEFT,value= Year_values)
    
    global Status_out
    Status_out=Label(Status)

    #Button click commands
    def read_click(type_,year_):

        #updates Status
        global Status_out
        Status_out.destroy()
        Message ,Colour = read_msg(type_,year_)
        Status_out=Label(Status,text=Message,anchor=W,justify=LEFT,background=Colour)
        Status_out.pack(fill='x')

        #Calls function
        if Colour == 'green':
            global right_canvas
            right_canvas.destroy()

            right_canvas=Frame(right,width=750,background='green')
            right_canvas.pack(expand=True,fill=BOTH)

            header_label = Label(right_canvas,text = type_)
            r=rd.ReadData(year_)
            if type_ == 'Traffic Volume':
                data = r.read_volume(year_)
                cols = ('Year','Section Name', 'Latitude','Longitude','Shape Length','Volume')
            else:
                data = r.read_incidents(year_)
                cols = ('Incident Info','Description', 'Start Date','End Date','Quadrant','Longitude','Latitude')
            
            list_box = ttk.Treeview(right_canvas, columns=cols, show ='headings')
            vsb = Scrollbar(right_canvas, orient = VERTICAL, command=list_box.yview)
            vsb.pack(side = RIGHT, fill = Y)
            hsb = Scrollbar(right_canvas, orient = HORIZONTAL, command = list_box.xview)
            hsb.pack(side = BOTTOM, fill = X)

            for col in cols:
                list_box.heading(col, text = col)
            #list_box.grid(row = 1, column=0, columnspan = 1)
            for data_set in data:
                list_box.insert("","end", values= data_set)
            list_box.pack(expand=True,fill=BOTH)
    
    def write_click(type_):

        #updates Status
        global Status_out
        Status_out.destroy()
        Message ,Colour = write_msg(type_)
        Status_out=Label(Status,text=Message,anchor=W,justify=LEFT,background=Colour)
        Status_out.pack(fill='x')

        #Calls function
        if Colour == 'green':
            global right_canvas
            right_canvas.destroy()

            right_canvas=Frame(right,width=750,background='green')
            right_canvas.pack(expand=True,fill=BOTH)
            entry_canvas = Canvas(right_canvas)
            entry_canvas.pack(expand = True, fill = BOTH)

            if type_ == "Traffic Volume":
                labels = ['Year:','Sector Name: ', 'Location: ','Shape Leng: ','Volume: ']
                list_entries =[]
                for i in range(len(labels)):
                    cur_label = 'label' + str(i)
                    cur_label = Label(entry_canvas, text = labels[i])
                    cur_label.grid(row=i, column=4, pady = 20, padx = 5)
                row_count = 0
                for i in range(len(labels)):
                    entry_box = Entry(entry_canvas, width=50)
                    entry_box.grid(column=5, row=row_count)
                    list_entries.append(entry_box)
                    row_count += 1
                input_but = Button(entry_canvas, text ="Insert into Database", command = lambda: submit(list_entries,type_))
                input_but.grid(column = 5, row = 9)
            else:
                labels = ['Incident Info: ', 'Description: ', 'Start Date: ','Modified Date: ','Quadrant: ','Longitude: ','Latitude: ',
                            'Location: ', 'Count: ', 'Id: ']
                list_entries =[]
                for i in range(len(labels)):
                    cur_label = 'label' + str(i)
                    cur_label = Label(entry_canvas, text = labels[i])
                    cur_label.grid(row=i, column=4, pady = 10, padx = 5)
                row_count=0
                for i in range(len(labels)):
                    entry_box = Entry(entry_canvas, width=50)
                    entry_box.grid(column=5, row=row_count)
                    list_entries.append(entry_box)
                    row_count += 1
                input_but = Button(entry_canvas, text ="Insert into Database", command = lambda: submit(list_entries,type_))
                input_but.grid(column = 5, row = 16)
    
    def submit(new_entry, type_):
        entry = []
        for entries in new_entry:
            entry.append(entries.get())
        r = rd.ReadData('2016')
        r.insert_data(entry,type_)
        for entries in new_entry:
            entries.delete(0, 'end')
        
    def sort_click(type_,year_):

        #updates Status
        global Status_out
        Status_out.destroy()
        Message, Colour,= sort_msg(type_,year_)
        Status_out=Label(Status,text=Message,anchor=W,justify=LEFT,background=Colour)
        Status_out.pack(fill='x')

        #Calls function
        if Colour == 'green':
            global right_canvas
            right_canvas.destroy()
            right_canvas=Frame(right,width=750,background='green')
            right_canvas.pack(expand=True,fill="both")
            
            
            header_label = Label(right_canvas,text = type_)
            r=rd.ReadData(year_)
            if type_ == 'Traffic Volume':
                data = r.sort_volume(year_)
                cols = ('Year','Section Name', 'Latitude','Longitude','Shape Length','Volume')
            else:
                data = r.sort_incidents(year_)
                cols = ('Number of Incidents','Location', 'Quadrant', 'Latitude','Longitude')
            
            list_box = ttk.Treeview(right_canvas, columns=cols, show ='headings')
            vsb = Scrollbar(right_canvas, orient = VERTICAL, command=list_box.yview)
            vsb.pack(side = RIGHT, fill = Y)
            hsb = Scrollbar(right_canvas, orient = HORIZONTAL, command = list_box.xview)
            hsb.pack(side = BOTTOM, fill = X)

            for col in cols:
                list_box.heading(col, text = col)
            #list_box.grid(row = 1, column=0, columnspan = 1)
            for data_set in data:
                list_box.insert("","end", values= data_set)
            list_box.pack(expand=True,fill=BOTH)

    def analysis_click(type_):

        #updates Status
        global Status_out
        Status_out.destroy()
        Message , Colour= analysis_msg(type_)
        Status_out=Label(Status,text=Message,anchor=W,justify=LEFT,background=Colour)
        Status_out.pack(fill='x')

        #Calls function
        if Colour == 'green':
            #removes previous right_canvas
            global right_canvas
            right_canvas.destroy()
            right_canvas=Frame(right,width=750,background='green')

            f=analysis_func(type_)
            canvas= FigureCanvasTkAgg(f,right_canvas)
            canvas.draw()
            canvas.get_tk_widget().pack(side=TOP, fill = BOTH, expand=True)

            toolbar=NavigationToolbar2Tk(canvas,right_canvas)
            toolbar.update()
            canvas._tkcanvas.pack(side=TOP, fill = BOTH, expand=True)

            #updates to new right_canvas
            
            right_canvas.pack(expand=True,fill="both")


    def map_click(type_,year_):

        #updates Status
        global Status_out
        Status_out.destroy()
        Message , Colour = map_msg(type_,year_)
        Status_out=Label(Status,text=Message,anchor=W,justify=LEFT,background=Colour)
        Status_out.pack(fill='x')

        #Calls function
        if Colour == 'green':
            global right_canvas
            right_canvas.destroy()

            right_canvas=Frame(right,width=750)
            right_canvas.pack(expand=True,fill="both")

            r = rd.ReadData(year_)
            r.draw_map(type_,year_)
            url = 'CalgaryMap.html'
            webbrowser.register('chrome',
	        None,
	        webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)

    #Create Buttons
    Button_read=Button(left,text="Read", padx=50,pady=10,command=lambda: read_click(CB_type.get(),CB_year.get()))
    Button_write=Button(left,text="Write", padx=50,pady=10,command=lambda: write_click(CB_type.get()))
    Button_sort=Button(left,text="Sort", padx=50,pady=10,command=lambda:  sort_click(CB_type.get(),CB_year.get()))
    Button_analysis=Button(left,text="Analysis",padx=50,pady=10,command=lambda: analysis_click(CB_type.get()))
    Button_map=Button(left,text="Map", padx=50,pady=10,command=lambda: map_click(CB_type.get(),CB_year.get()))

    #display Combobox and header labels
    Type_label.pack(fill='x')
    CB_type.pack(fill='x')
    Year_label.pack(fill='x')
    CB_year.pack(fill='x')

    #display function buttons
    Button_read.pack(fill='x')
    Button_write.pack(fill='x')
    Button_sort.pack(fill='x')
    Button_analysis.pack(fill='x')
    Button_map.pack(fill='x')

    #display status box
    Status_label = Label(left, text="Status:",anchor=W,justify=LEFT)
    Status_label.pack(fill='x')
    Status.pack(expand=True, fill="both", padx=5, pady=5)

    #display left and right frames
    left.pack(side="left", expand=True, fill="both")
    right.pack(side="right", expand=True, fill="both")

    root.mainloop()

if __name__ == "__main__":
    main()

