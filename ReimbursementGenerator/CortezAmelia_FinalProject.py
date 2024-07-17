"""
Author: Amelia Cortez
Date Written: 7/10/2024
Assignment: Final Project
This is a gui program that creates a reimbursement report based on user input
then saves the report.
"""

import tkinter as tk
from tkinter import PhotoImage

# Function to open new window, which calls the report_form.py
def open_new_window():
    import report_form
    report_form
  
# Function for button command to open report_form.py in a new window
def button_click():
    open_new_window()
 

 # Create the main window      
root = tk.Tk()
root.title("Reimbursement Report Generator")
root.geometry("400x200")

# Load the image
image = PhotoImage(file = "/Users/amilli/Desktop/School/SDEV140/Final Project/ReimbursementGenerator/starticon.png")
# Create the button and tie to function
button = tk.Button(root, text = "Create New Report", command = button_click, image = image, compound = "top")
button.pack(pady = 20)


root.mainloop()

