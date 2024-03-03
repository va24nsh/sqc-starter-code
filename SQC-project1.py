import tkinter
from tkinter import END
import qiskit
from qiskit.visualization import visualize_transition as vs



def initialize_circuits():
    global circuits
    circuits  = qiskit.QuantumCircuit(1,1)
    # circuits.x(0)
    # circuits.measure_all(0,0)
    

initialize_circuits()

def visualize_circuit(circuit , window):
    try:
        vs(circuit, window)
    except:
        window.destroy()





# creating the canvas
root = tkinter.Tk()
root.title("Super Quant Coders")

# icon and scaling the window
root.geometry("380x390")
root.resizable(0,0)

# creating the display frames 
display_screen = tkinter.LabelFrame(root , bd = 10 , bg = 'green')
button_screen = tkinter.LabelFrame(root , bg = 'black')

display_screen.pack(ipadx= 10 , ipady= 10)
button_screen.pack(fill = 'both' , expand = True)

# Designing the entry screen
display = tkinter.Entry(display_screen , width = 120 , font = ('Arial' , 32) , bg = 'blue' , fg = 'white' , justify= 'left')
display.pack(fill = 'both',expand= True,padx= 2 , pady= 2 )

def gate_display(input_gate):
    display.insert(END , input_gate)


# clear functionality 
def clear_gates():
    display.delete(0 ,END)
    initialize_circuits() #reititialising the cicuits to be used again

# creating buttons

x_gate = tkinter.Button(button_screen , bg = "pink" , fg = "red" , text='X', font = ('arial' , 15), command = lambda : [gate_display("X") , circuits.x(0)])
y_gate = tkinter.Button(button_screen , bg = 'pink' , foreground= 'red' , text = 'Y' , font = ('arial' , 15), command= lambda : [gate_display("Y") , circuits.y(0)])
z_gate = tkinter.Button(button_screen , bg = 'pink' , foreground= 'red' , text = 'Z' , font = ('arial' , 15), command= lambda : [gate_display("Z") , circuits.z(0)])
h_gate = tkinter.Button(button_screen , bg = 'pink' , fg = 'red' , text = 'H' , font = ('arial' , 15), command= lambda : [gate_display("H") , circuits.h(0)])
quit_button = tkinter.Button(button_screen , bg = 'red' , fg = 'white' , text = 'Quit' , font = ('arial' , 15) , command= lambda : root.destroy())
visualize = tkinter.Button(button_screen , bg = 'red' , fg = 'white' , text = 'Visualize' , font = ('arial' , 15), command = lambda: visualize_circuit(circuits, root))
clear = tkinter.Button(button_screen , bg = 'red' , fg = 'white' , text = 'Clear' , font = ('arial' , 15), command= lambda :clear_gates())
sqc = tkinter.Button(button_screen , bg = 'yellow', fg= 'blue' , text= 'Super Quant Coders' , font= ('algerian' , 20) )

# we can use gate.config state = DISABLE to disable buttons if 10 buttons are pressed

# Displayiing the buttons in the botton_screen frame
x_gate.grid(row = 0 , column = 0 , ipadx= 45 , ipady= 20 , padx= 1 , pady= 1 , sticky= 'WE')
y_gate.grid(row = 0 , column= 1 , ipadx= 45 , ipady= 20, padx= 1 , pady= 1, sticky= 'WE')
z_gate.grid(row = 0 , column= 2 , ipadx= 45 , ipady= 20 , padx= 1 , pady= 1, sticky= 'WE' )
h_gate.grid(  column= 0, ipadx= 50  , padx= 1, pady= 1 , sticky= "NSWE" , rowspan= 3)
quit_button.grid(row = 1 , column= 1, columnspan= 2 , sticky= "NWE")
visualize.grid(row = 2 , column= 1, columnspan= 2 , sticky= "NWE" )
clear.grid(row = 3 , column= 1, columnspan= 2 , sticky= "NWE")
sqc.grid(row = 4 , column= 0 , columnspan= 3 , sticky= "WE" ,ipady= 20) 


# circuits  = qiskit.QuantumCircuit(1,1)
# circuits.h(0)
# circuits.z(0)
# vs(circuits)

# initializing circuit
# vs(circuits)




root.mainloop()