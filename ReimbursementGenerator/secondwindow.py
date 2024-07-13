import tkinter
from tkinter import ttk


window = tkinter.Tk()
window.title("Reimbursement Report Form")

frame = tkinter.Frame(window)
frame.pack()

# label and entry for name
name_label =  tkinter.Label(frame, text = "Name")
name_label.grid(row=0, column=0)
name_entry = tkinter.Entry(frame)
name_entry.grid(row=1, column=0)

# label and entry for Travel Dates
traveldates_label =  tkinter.Label(frame, text = "Travel Dates")
traveldates_label.grid(row=0, column=1)
traveldates_entry = tkinter.Entry(frame)
traveldates_entry.grid(row=1, column=1)

# Location label and entry
location_label =  tkinter.Label(frame, text = "Location")
location_label.grid(row=0, column=2)
location_entry = tkinter.Entry(frame)
location_entry.grid(row=1, column=2)

# quantity label and counter
quantity_label =  tkinter.Label(frame, text = "Quantity")
quantity_label.grid(row=2, column=0)
quantity_spinbox = tkinter.Spinbox(frame, from_ = 1, to = 30)
quantity_spinbox.grid(row=3, column=0)

# expense description label and entry
exdescription_label =  tkinter.Label(frame, text = "Expense Description")
exdescription_label.grid(row=2, column=1)
exdescription_entry = tkinter.Entry(frame)
exdescription_entry.grid(row=3, column=1)

# Cost label and counter
cost_label =  tkinter.Label(frame, text = "Cost")
cost_label.grid(row=2, column=2)
cost_spinbox = tkinter.Spinbox(frame, from_ = 0.0, to= 1e10, increment=0.01)
cost_spinbox.grid(row=3, column=2)













window.mainloop()
