"""
    Welcome to SQC - Quantum Computing Club NIT Jalandhar
    
    A warm welcome to this workshop on quantum computing! We are thrilled to have each of you on board for this exciting exploration into the fascinating world of quantum technology.

    Get ready to embark on a journey that will challenge your understanding of computation and open doors to a realm where quantum bits defy classical logic.

    Let us together build a project which will help in visualizing Quantum Gates.
"""

import tkinter
from tkinter import END

def visualize_circuit(circuit , window):
    try:
        # --> Visualize circuit using visualize_transition
        pass
    except:
        window.destroy()

# --> Initialize the circuit


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

# Display the gate visiualization
def gate_display(input_gate):
    display.insert(END , input_gate)


# clear functionality 
def clear_gates():
    display.delete(0 ,END)
    # --> Re-Initialising the cicuits to be used again

# creating buttons

x_gate = tkinter.Button(button_screen , bg = "pink" , fg = "red" , text='X', font = ('arial' , 15), command = lambda : [gate_display("X")])
y_gate = tkinter.Button(button_screen , bg = 'pink' , foreground= 'red' , text = 'Y' , font = ('arial' , 15), command= lambda : [gate_display("Y")])
z_gate = tkinter.Button(button_screen , bg = 'pink' , foreground= 'red' , text = 'Z' , font = ('arial' , 15), command= lambda : [gate_display("Z")])
h_gate = tkinter.Button(button_screen , bg = 'pink' , fg = 'red' , text = 'H' , font = ('arial' , 15), command= lambda : [gate_display("H")])
quit_button = tkinter.Button(button_screen , bg = 'red' , fg = 'white' , text = 'Quit' , font = ('arial' , 15) , command= lambda : root.destroy())
visualize = tkinter.Button(button_screen , bg = 'red' , fg = 'white' , text = 'Visualize' , font = ('arial' , 15)) # --> Add the command lambda to visulize transition of the circuit in root
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

root.mainloop()

"""
    Thank You for showing your enthusiasm.

    For more updates follow us on instagram @sqc_nitj
"""