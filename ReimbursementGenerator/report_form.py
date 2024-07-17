"""
Author: Amelia Cortez
This is a module for the the Reimbusement Report Generator
In this module, the program displays a screen which takes input from the user
then creates and saves a word doc
"""

import tkinter
from tkinter import ttk
from docxtpl import DocxTemplate

# Function to clear quantity, expense description, and cost entries once added
def clear_entry():
    quantity_spinbox.delete(0, tkinter.END)
    quantity_spinbox.insert(0,"1")
    exdescription_entry.delete(0,tkinter.END)
    cost_spinbox.delete(0,tkinter.END)
    cost_spinbox.insert(0, "0.00")

# list to store current report expenses
expense_list = []

# Function to add expense details in list and calculate the total
def add_expense():
    quantity = int(quantity_spinbox.get())
    expense = exdescription_entry.get()
    cost = float(cost_spinbox.get())
    total = quantity * cost
    report_variables = [quantity, expense, cost, total]
    
    tree.insert('', 0, values=report_variables)
    clear_entry()
    
    expense_list.append(report_variables)

# Function to clear and start a new report
def new_report():
    name_entry.delete(0,tkinter.END)
    location_entry.delete(0,tkinter.END)
    traveldates_entry.delete(0,tkinter.END)
    clear_entry()
    tree.delete(*tree.get_children())
    expense_list.clear()

  
# Function to create and save Reimbursement Report
def create_report():
    doc = DocxTemplate("reimbursement_template.docx")
    name = name_entry.get()
    traveldates = traveldates_entry.get()
    location = location_entry.get()
    total = sum(item[3] for item in expense_list)
    
    doc.render({"name":name,
                "traveldates":traveldates,
            "location":location,
            "expense_list": expense_list,
            "total":total})
    
    doc_name = "Reimbursement Report" + name + location + ".docx"
    doc.save(doc_name)
    
    import popupmessage
    popupmessage.main()
    
     
# Create the main window
window = tkinter.Tk()
window.title("Reimbursement Report Form")

# Create a frame widget to hold other widgets
frame = tkinter.Frame(window)
frame.pack(padx=30, pady=15)

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
location_label = tkinter.Label(frame, text = "Location")
location_label.grid(row=0, column=2)
location_entry = tkinter.Entry(frame)
location_entry.grid(row=1, column=2)

# quantity label and counter
quantity_label = tkinter.Label(frame, text = "Quantity")
quantity_label.grid(row=2, column=0)
quantity_spinbox = tkinter.Spinbox(frame, from_ = 1, to = 30)
quantity_spinbox.grid(row=3, column=0)

# expense description label and entry
exdescription_label = tkinter.Label(frame, text = "Expense Description")
exdescription_label.grid(row=2, column=1)
exdescription_entry = tkinter.Entry(frame)
exdescription_entry.grid(row=3, column=1)

# Cost label and counter
cost_label = tkinter.Label(frame, text = "Cost")
cost_label.grid(row=2, column=2)
cost_spinbox = tkinter.Spinbox(frame, from_ = 0.00, to= 1e10, increment=0.01)
cost_spinbox.grid(row=3, column=2)

# Add expense button and link to add expense function
addexpense_button = tkinter.Button(frame, text="Add Expense", command=add_expense)
addexpense_button.grid(row=4,column=2,pady=4)

# treeveiw to create added expense list area with title headings
titles = ("Quantity", "Expense", "Cost", "Total")
tree = ttk.Treeview(frame, columns=titles, show= "headings")
tree.grid(row=5, column=0, columnspan=3, padx=30, pady=15)
tree.heading("Quantity", text="Quantity")
tree.heading("Expense", text="Expense")
tree.heading("Cost", text="Cost")
tree.heading("Total", text="Total")

# Create/save Reimbursement report and new Reimbursement report buttons
createreport_button = tkinter.Button(frame, text="Create and Save Reimbursement Report", command=create_report)
createreport_button.grid(row=6, column=2, sticky="news", padx=15, pady=5)
newreport_button = tkinter.Button(frame, text="Start New Reimbursement Report", command=new_report)
newreport_button.grid(row=7, column=2, sticky="news", padx=15, pady=5)
    
    
window.mainloop()
    
