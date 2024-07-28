"""
Author: Amelia Cortez
Date Written: 7/10/2024
Assignment: Final Project
This is a module for creating and managing the main window
It has command buttons that open a new window with a reimbursement form
and closes the application
"""

# Import necessary modules and classes
import tkinter as tk                                   
from tkinter import PhotoImage                        
from report_form import Reimbursement_Form


def open_new_window():
    '''Opens a new window with a Report_Form instance.'''
    report_form_window = tk.Toplevel(root)                   # Create new top-level window
    Reimbursement_Form(report_form_window)                   # Set up Reimbursement_Form with new window         


def button_click():
    '''Handles the button click event by opening a new window'''
    open_new_window()                                                                  


def close_program():
    '''Closes the main application window and exits the program.'''
    root.destroy()                                      
    
 
# Create the main window, sets title and size     
root = tk.Tk()                                   # set up the main application window                             
root.title("Reimbursement Report Generator")           
root.geometry("400x200")                                

# Load the image for the "Create New Report" button
image = PhotoImage(file="piggybank.png")      
                                                              
# Create button to open new report_form window
button = tk.Button(root, text="Create New Report", command=button_click, image=image, compound="top")     # sets up the button with text, command, image, and layout settings
button.pack(side="left", padx=20, pady=20)                                                                    

# Load the image for close_all_button
close_image = PhotoImage(file="exiticon.png")
                                                                               
# Create button to close app
close_all_button = tk.Button(root, text="Close App", command=close_program,image=close_image, compound="top" )  # sets up the button with text, command, image, and layout settings  
close_all_button.pack(side="right", padx=80, pady=20)                                                                        

# Start the Tkinter event loop
root.mainloop()