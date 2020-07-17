from tkinter import *

root = Tk()
root.title('Calgary Traffic Database')
root.geometry("1000x700")

left = Frame(root, width=100, borderwidth=1, relief="solid")
right = Frame(root, borderwidth=1, relief="solid")
Status = Frame(left, width =100, borderwidth=1, relief="solid")

Button_read=Button(left,text="Read", padx=50)
Button_sort=Button(left,text="Sort", padx=50)
Button_analysis=Button(left,text="Analysis", padx=50)
Button_map=Button(left,text="Map", padx=50)

Status_label = Label(left, text="Status:",anchor=W,justify=LEFT)

Button_read.pack(fill='x')
Button_sort.pack(fill='x')
Button_analysis.pack(fill='x')
Button_map.pack(fill='x')
Status_label.pack(fill='x')
Status.pack(expand=True, fill="both", padx=5, pady=5)

left.pack(side="left", expand=True, fill="both")
right.pack(side="right", expand=True, fill="both")




root.mainloop()