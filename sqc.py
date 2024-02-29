import qiskit
import tkinter
import warnings
import numpy as np
from tkinter import END
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition

# Ignore warnings 
warnings.simplefilter("ignore")

# Define window
root = tkinter.Tk()
root.title('Super Quant Coders')

# Icon Set-UP
root.iconbitmap()
root.geometry('400x410')
root.resizable(0,0) # Resizing window is blocked

# Define Frames
display_f = tkinter.LabelFrame(root) # Where the frames must go
button_f = tkinter.LabelFrame(root, bg='black')
display_f.pack()
button_f.pack(fill='both', expand=True)

# Define Entry Bar
display = tkinter.Entry(display_f, borderwidth=2, width = 150, font=('Arial', 32), bg='#1D2D12')
display.pack(padx=3, pady=4)







# Quantum Circuit ko initialise



def initialize_circuit(): 
    global circuit
    circuit = QuantumCircuit(1)

initialize_circuit()

def display_gates(input_gate):
    display.insert(END, input_gate)

def clear_gates():
    display.delete(0, END)
    initialize_circuit() # Re Initialize the circuit











# Define gates like X Y Z and H
x_gate = tkinter.Button(button_f, font=('Arial', 18), bg='#0fe43d', text='X', command=lambda:[display_gates('X'), circuit.x(0)])
y_gate = tkinter.Button(button_f, font=('Arial', 18), bg='#0fe43d', text='Y', command=lambda:[display_gates('Y'), circuit.y(0)])
z_gate = tkinter.Button(button_f, font=('Arial', 18), bg='#0fe43d', text='Z', command=lambda:[display_gates('Z'), circuit.z(0)])
h_gate = tkinter.Button(button_f, font=('Arial', 18), bg='#0fe43d', text='H', command=lambda:[display_gates('H'), circuit.h(0)])
# Put the buttons in the button_frame
x_gate.grid(row=0, column=0, columnspan=6, sticky='WE')
y_gate.grid(row=0, column=6, columnspan=6, sticky='WE')
z_gate.grid(row=0, column=12, columnspan=6, sticky='WE')
h_gate.grid(row=1, column=0, columnspan=18, sticky='WE')

#Define the QUIT button
quit = tkinter.Button(button_f, font=('Arial', 18), bg='#0fe43d', text='QUIT', command=root.destroy)
#Define the VISUALIZE button
visualize = tkinter.Button(button_f, font=('Arial', 18), bg='#0fe43d', text='VISUALIZE', command=lambda:[visualize_transition(circuit)])
#Define the CLEAR button
clear = tkinter.Button(button_f, font=('Arial', 18), bg='#0fe43d', text='CLEAR', command=lambda:[clear_gates()])
# Put the buttons in the frame
quit.grid(row=3, column=0, columnspan=18, sticky='WE') # West to Ease ==> WE
visualize.grid(row=4, column=0, columnspan=18, sticky='WE')
clear.grid(row=5, column=0, columnspan=18, sticky='WE')







# Run the tkinter loop
root.mainloop()