"""
Author: Amelia Cortez
This is part of the Reimbusement Report Generator GUI
This module creates and displays a simple popup message window that informs the user that a reimbursement report has been created and saved.
It allows the user to start a new report or to close the popup if no further action is needed.
"""

# Import necessary modules
import tkinter as tk


def main():
  '''
  Function to display the popup message
  '''
  global popup                         # Declare popup as a global variable to be used across functions
  popup = tk.Tk()                      # Create the main window for the popup
  popup.wm_title("Report Status")

  # Create frame
  frame = tk.Frame(popup)
  frame.pack(padx=20, pady=20)

  # Message label
  msg_label = tk.Label(frame, text="Reimbursement Report has been created and saved! \n Do you want to start a new report?")
  msg_label.pack()

  # Yes button that starts a new report
  yes_button = tk.Button(frame, text="Yes", command=start_over)         # Triggers start_over function
  yes_button.pack(side="left", padx=5, pady=15)

  # No button that closes popup
  no_button = tk.Button(frame, text="No", command=close_window)         # Triggers close_window function
  no_button.pack(side="right", padx=5, pady=15)
    
  # Start event loop for the popup window
  popup.mainloop()


def start_over():
  '''
  Function to restart report_form new_report function
  '''
  global popup                                   # Access the global popup variable
  popup.destroy()                                # Close the popup window
  root = tk.Tk()                                 # Create a new main application window
  
  from report_form import Reimbursement_Form     # Import the Reimbursement_Form class
  Reimbursement_Form(root)                       # Create a new instance of Reimbursement_Form within the new window
  root.mainloop()                                # Start event loop for the new window
  

def close_window():
  '''
  Function to close pop up box
  '''
  popup.destroy()
  
# Call the main function to run the application 
if __name__ == "__main__":
    main() 