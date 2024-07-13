"""
Author: Amelia Cortez
Date Written: 7/10/2024
Assignment: Final Project
This is a gui program that creates a reimbursement report based on user input
then saves the report to a file
"""

import tkinter as tk
from tkinter import PhotoImage, messagebox

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("300x200")
  
def button_click():
    open_new_window()
    
root = tk.Tk()
root.title("Reimbursement Report Generator")
root.geometry("400x200")

# Load the image
image = PhotoImage(file = "/Users/amilli/Desktop/School/SDEV140/Final Project/ReimbursementGenerator/starticon.png")
# Create the button
button = tk.Button(root, text = "Create New Report", command = button_click, image = image, compound = "top")
button.pack(pady = 20)


root.mainloop()
