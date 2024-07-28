"""
Author: Amelia Cortez
This is part of the Reimbusement Report GUI
This module is for managing and creating a reimbursement report. 
This code allows user to input details, add expenses, create and save reports, or start a new report.
Program uses Tkinter for the GUI, docxtpl for generating Word documents, and regex for date validation.
"""

# Import required modules and libraries
import tkinter
from tkinter import ttk, messagebox
from docxtpl import DocxTemplate
import popupmessage
import re


class Reimbursement_Form:
    '''
    Class for creating, managing and displaying the reimbursement report form window. 
    Handles input, validation, and report document generation
    '''

    def __init__(self,master):
        '''
        sets the report form window and GUI components
        '''
        self.master = master
        self.master.title("Reimbursement Report Form")
        
        
        self.expense_list = []              # list to store current report expenses entries
        
        # Create Frame
        self.frame = tkinter.Frame(master)  # Frame for organizing widgets
        self.frame.pack(padx=30, pady=15)
        
        # Creates widgets
        self.create_widgets()
    

    def create_widgets(self):
        '''
        Function to create and place widgets
        '''
    # Input fields
        # name entry and label
        tkinter.Label(self.frame, text = "Name").grid(row=0, column=0)
        self.name_entry = tkinter.Entry(self.frame)    # Entry for user to input name                
        self.name_entry.grid(row=1, column=0)

        # Travel Dates entry and label
        tkinter.Label(self.frame, text = "Travel Dates").grid(row=0, column=1)
        self.traveldates_entry = tkinter.Entry(self.frame)      # Entry for user to input travel date
        self.traveldates_entry.grid(row=1, column=1)

        # Location label and entry
        tkinter.Label(self.frame, text = "Location").grid(row=0, column=2)
        self.location_entry = tkinter.Entry(self.frame)         # Entry for user to input location
        self.location_entry.grid(row=1, column=2)

    # Expense details
        # quantity label and spinbox
        tkinter.Label(self.frame, text = "Quantity").grid(row=2, column=0)
        self.quantity_spinbox = tkinter.Spinbox(self.frame, from_ = 1, to = 30)  # Spinbox for selecting quantity
        self.quantity_spinbox.grid(row=3, column=0)

        # expense description label and entry
        tkinter.Label(self.frame, text = "Expense Description").grid(row=2, column=1)
        self.exdescription_entry = tkinter.Entry(self.frame)       # Entry for user to input expense description
        self.exdescription_entry.grid(row=3, column=1)

        # Cost label and spinbox
        tkinter.Label(self.frame, text = "Cost").grid(row=2, column=2)
        self.cost_spinbox = tkinter.Spinbox(self.frame, from_ = 0.00, to= 1e10, increment=0.01)   # Spinbox for cost
        self.cost_spinbox.grid(row=3, column=2)
        
    # Action Buttons
        # Button to add expense
        tkinter.Button(self.frame, text="Add Expense", command=self.add_expense).grid(row=4,column=2,pady=4)
        
        # Button to Create/save Reimbursement report
        tkinter.Button(self.frame, text="Create and Save Reimbursement Report", command=self.create_report).grid(row=6, column=2, sticky="news", padx=15, pady=5)
        
        # Button to start a new reimbursement report
        tkinter.Button(self.frame, text="Start New Reimbursement Report", command=self.new_report).grid(row=7, column=2, sticky="news", padx=15, pady=5)
        
    # Expense Display
        # treeveiw to create added expense list area with title headings
        titles = ("Quantity", "Expense", "Cost", "Total")                        # Column titles for the treeview
        self.tree = ttk.Treeview(self.frame, columns=titles, show= "headings")   # Treeview to show expense details
        self.tree.grid(row=5, column=0, columnspan=3, padx=30, pady=15)
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Expense", text="Expense")
        self.tree.heading("Cost", text="Cost")
        self.tree.heading("Total", text="Total")
        

   
    def clear_entry(self):
        '''
        Function that clears quantity, expense description, and cost entries, resets default values 
        '''
        # Clear the quantity spinbox and reset to default value
        self.quantity_spinbox.delete(0, tkinter.END)
        self.quantity_spinbox.insert(0,"1")  
        # Clear the expense description entry
        self.exdescription_entry.delete(0,tkinter.END)
        # Clear the cost spinbox and reset to default value
        self.cost_spinbox.delete(0,tkinter.END)
        self.cost_spinbox.insert(0, "0.00")



    def add_expense(self):
        '''
        Function to retrieve and validate input, calculate total
        and add expense details in list and show on display
        '''
        # Retrieve values from the input fields
        quantity = self.quantity_spinbox.get()                    # Get the quantity from spinbox
        expense = self.exdescription_entry.get()                  # Get the expense description from entry
        cost = self.cost_spinbox.get()                            # Get the cost from spinbox

        # Input Validation
        if not self.validate_input(quantity, expense, cost):
            return 
        
        # Convert and calculate values
        quantity = int(quantity)                                  # Convert quantity to integer
        cost = float(cost)                                        # Convert cost to float
        total = round(quantity * cost, 2)                                   # Calculate total cost and round the nearest hundredths 
        report_variables = [quantity, expense, cost, total]       # Data to be inserted into the treeview
        
        # Insert new expense into the treeview
        self.tree.insert('', 0, values=report_variables)
        # Clear the input fields
        self.clear_entry()
        # Add the expense to the list
        self.expense_list.append(report_variables)



    def new_report(self):
        '''
        Function to clear and start a new report
        '''
        # Clear input fields
        self.name_entry.delete(0,tkinter.END)                    # Clear name entry
        self.location_entry.delete(0,tkinter.END)                # Clear location entry
        self.traveldates_entry.delete(0,tkinter.END)             # Clear travel date entry
        self.clear_entry()                                       # Clear input fields
        # Clear the treeview
        self.tree.delete(*self.tree.get_children())              # Remove all items from treeview
        # Clear expense list
        self.expense_list.clear()



    def validate_input(self,quantity,expense,cost):
        '''
        Function to validate input and display error if not valid
        '''
        
        # Name entry validation
        if not self.name_entry.get():
            tkinter.messagebox.showerror("Error", "Please enter a name.")
            return False

        # Travel Dates validation
        travel_dates = self.traveldates_entry.get()                      # Get travel dates from entry
        pattern = r"^\d{2}/\d{2}/\d{4}-\d{2}/\d{2}/\d{4}$"               # Expected travel dates format

        if not re.match(pattern, travel_dates):                          # Validate travel dates format
            messagebox.showerror("Error", "Please enter valid travel dates in MM/DD/YYYY-MM/DD/YYYY format.")
            return False

        # Location entry validation
        if not self.location_entry.get():
            messagebox.showerror("Error", "Please enter a location.")
            return False

        # Quantity validation
        try:
            quantity = int(quantity)                                      # Convert quantity to integer
            if quantity <= 0:
                raise ValueError
        except ValueError:                                                # Handle invalid quantity
            messagebox.showerror("Error", "Please enter a positive integer quantity.")
            return False

        # Cost validation
        try:
            cost = float(cost)                                            # Convert cost to float
            if cost <= 0:
                raise ValueError
        except ValueError:                                                # Handle invalid cost
            messagebox.showerror("Error", "Please enter a positive decimal cost.")
            return False
        
        # Expense entry validation
        if not expense:
            messagebox.showerror("Error", "Please enter an expense description.")
            return False

        return True


    
    def create_report(self):
        '''
        Function to create and save the reimbursement report as a word doc using template
        then display a pop up message
        '''
        # Load the Word template
        doc = DocxTemplate("reimbursement_template.docx")
        # Retrieve values from input fields and calculate total
        name = self.name_entry.get()                                       # Get the name from entry
        traveldates = self.traveldates_entry.get()                         # Get travel dates from entry
        location = self.location_entry.get()                               # Get location from entry
        total = round(sum(item[3] for item in self.expense_list), 2)       # Calculate the total cost of all expenses and round to the nearest hundredths 
        
        # Render the template with data
        doc.render({"name":name,
                    "traveldates":traveldates,
                "location":location,
                "expense_list": self.expense_list,
                "total":total})
        
        # Create file name and save the report
        doc_name = "Reimbursement Report" + " " + name + " " + location + ".docx"      # Create file name for the report
        doc.save(doc_name)                                                 # Save the report
        
        # Display a popup message
        popupmessage.main()

# sets and runs the Tkinter main application window
if __name__ == "__main__":
    root = tkinter.Tk()                                                    # Create the main application window
    app = Reimbursement_Form(root)                                         # Set the Report_Form application
    root.mainloop()                                                        # Run the application