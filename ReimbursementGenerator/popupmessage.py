import tkinter as tk
from tkinter import PhotoImage, messagebox



# Function to restart report_form new_report function
def start_over():
  import report_form
  report_form.new_report()
  close_window()

# function to close pop up box
def close_window():
  msgbox.destroy()
  
  
  
def main():  
  global msgbox
   
  msgbox = tk.Tk()
  msgbox.title("Reimbursement Report Saved!")
  frame = tk.Frame(msgbox)
  frame.pack(padx=30, pady=15)

  # Messge Box label
  msg_image = PhotoImage(file = "/Users/amilli/Desktop/School/SDEV140/Final Project/ReimbursementGenerator/completedicon.png")
  msg_label =  tk.Label(frame, text = "Reimbursment Report has been created and saved! Do you want to start a new report?", image=msg_image, compound = "top")
  msg_label.grid(row=0, column=0, columnspan=2)


  # Create the button
  yes_button = tk.Button(frame, text = "Yes", command = start_over)
  yes_button.grid(row = 1,column=0, sticky="ew", padx=15, pady=5)
  no_button = tk.Button(frame, text= "No", command = close_window)
  no_button.grid(row = 1,column=1, sticky="ew", padx=15, pady=5)


  msgbox.mainloop()


if __name__ == "__main__":
    main()
