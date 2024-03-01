"""
    Welcome to SQC - Quantum Computing Club NIT Jalandhar
    
    A warm welcome to this workshop on quantum computing! We are thrilled to have each of you on board for this exciting exploration into the fascinating world of quantum technology.

    Get ready to embark on a journey that will challenge your understanding of computation and open doors to a realm where quantum bits defy classical logic.

    Let us together build a project which will help in visualizing Quantum Gates.
"""

import tkinter
import warnings
import numpy as np
from tkinter import END

# Ignore warnings 
warnings.simplefilter("ignore")

# Define window
root = tkinter.Tk()
root.title('SQC')

# Icon Set-UP
root.geometry('225x305')
root.resizable(0,0) # Resizing window is blocked

# Define Frames
display_f = tkinter.LabelFrame(root) # Where the frames must go
button_f = tkinter.LabelFrame(root, bg='black')
display_f.pack()
button_f.pack(fill='both', expand=True)

# Define Entry Bar
display = tkinter.Entry(display_f, borderwidth=2, width = 150, font=('Arial', 32), bg='#1D2D12')
display.pack(padx=3, pady=4)

# --> Function to initialize the circuit here

def display_gates(input_gate):
    display.insert(END, input_gate)

def clear_gates():
    display.delete(0, END)
    # --> Re-Initialize the circuit here

# --> Give command to the buttons
# Define gates like X Y Z and H
x_gate = tkinter.Button(button_f, font=('Arial', 18), bg='#0fe43d', text='X')
y_gate = tkinter.Button(button_f, font=('Arial', 18), bg='#0fe43d', text='Y')
z_gate = tkinter.Button(button_f, font=('Arial', 18), bg='#0fe43d', text='Z')
h_gate = tkinter.Button(button_f, font=('Arial', 18), bg='#0fe43d', text='H', command=lambda:[display_gates('H')])
# Put the buttons in the button_frame
x_gate.grid(row=0, column=0, columnspan=6, sticky='WE')
y_gate.grid(row=0, column=6, columnspan=6, sticky='WE')
z_gate.grid(row=0, column=12, columnspan=6, sticky='WE')
h_gate.grid(row=1, column=0, columnspan=18, sticky='WE')

#Define the QUIT button
quit = tkinter.Button(button_f, font=('Arial', 18), bg='#0fe43d', text='QUIT', command=root.destroy)
#Define the VISUALIZE button
visualize = tkinter.Button(button_f, font=('Arial', 18), bg='#0fe43d', text='VISUALIZE') # --> Add command to visulaize
#Define the CLEAR button
clear = tkinter.Button(button_f, font=('Arial', 18), bg='#0fe43d', text='CLEAR', command=lambda:[clear_gates()])
# Put the buttons in the frame
quit.grid(row=3, column=0, columnspan=18, sticky='WE') # West to Ease ==> WE
visualize.grid(row=4, column=0, columnspan=18, sticky='WE')
clear.grid(row=5, column=0, columnspan=18, sticky='WE')

# Run the tkinter loop
root.mainloop()

"""
    Thank You for showing your enthusiasm.

    For more updates follow us on instagram @sqc_nitj
"""