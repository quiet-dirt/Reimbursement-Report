import tkinter
from tkinter import ttk


window = tkinter.Tk()
window.title("Reimbursement Report Form")

frame = tkinter.Frame(window)
frame.pack()

# label for first and last name
firstname_label =  tkinter.Label(frame, text = "First Name")
firstname_label.grid(row=0, column=0)
lastname_label =  tkinter.Label(frame, text = "Last Name")
lastname_label.grid(row=0, column=1)
# entry for first and last name
firstname_entry = tkinter.Entry(frame)
lastname_entry = tkinter.Entry(frame)
firstname_entry.grid(row=1, column=0)
lastname_entry.grid(row=1, column=1)

# Location label and entry
location_label =  tkinter.Label(frame, text = "Location")
location_label.grid(row=0, column=2)
location_entry = tkinter.Entry(frame)
location_entry.grid(row=1, column=2)

# quantity label and counter
quanity_label =  tkinter.Label(frame, text = "Quanity")
quanity_label.grid(row=2, column=0)
quanity_spinbox = tkinter.Spinbox(frame, from_ = 1, to = 30)
quanity_spinbox.grid(row=3, column=0)

# description label and entry
description_label =  tkinter.Label(frame, text = "Expense Description")
description_label.grid(row=2, column=1)
description_entry = tkinter.Entry(frame)
description_entry.grid(row=3, column=1)

# Cost label and counter
cost_label =  tkinter.Label(frame, text = "Cost")
cost_label.grid(row=2, column=2)
cost_spinbox = tkinter.Spinbox(frame, from_ = 0.0, to= 1e10, increment=0.01)
cost_spinbox.grid(row=3, column=2)













window.mainloop()