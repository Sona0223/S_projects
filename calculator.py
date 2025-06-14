#Function will called when button press This digit function will join all press button # text into variable var, which further display in textbox. 
from tkinter import *  # importing tkinter module
 
# Function to append digit/operator to the input
def digit(n):
    var.set(var.get() + n)

# Function to evaluate the expression
def equal():
    try:
        var.set(eval(var.get()))
    except:
        var.set("Error")

# Main application window
window = Tk()
window.title("Basic Calculator") 

var = StringVar()  # Variable for entry display

# UI layout
Label(window, text='Basic Calculator', font='Times 16 bold', fg='red').grid(row=0, columnspan=3)
Entry(window, textvariable=var, font='Times 14').grid(row=1, columnspan=3) 

# Row 2
Button(window, text='7', width=10, command=lambda: digit('7')).grid(row=2, column=0)
Button(window, text='8', width=10, command=lambda: digit('8')).grid(row=2, column=1)
Button(window, text='9', width=10, command=lambda: digit('9')).grid(row=2, column=2)

# Row 3
Button(window, text='4', width=10, command=lambda: digit('4')).grid(row=3, column=0)
Button(window, text='5', width=10, command=lambda: digit('5')).grid(row=3, column=1)
Button(window, text='6', width=10, command=lambda: digit('6')).grid(row=3, column=2)

# Row 4
Button(window, text='1', width=10, command=lambda: digit('1')).grid(row=4, column=0)
Button(window, text='2', width=10, command=lambda: digit('2')).grid(row=4, column=1)
Button(window, text='3', width=10, command=lambda: digit('3')).grid(row=4, column=2)

# Row 5
Button(window, text='0', width=10, command=lambda: digit('0')).grid(row=5, column=0)
Button(window, text='+', width=10, command=lambda: digit('+')).grid(row=5, column=1)
Button(window, text='-', width=10, command=lambda: digit('-')).grid(row=5, column=2)

# Row 6
Button(window, text='*', width=10, command=lambda: digit('*')).grid(row=6, column=0)
Button(window, text='/', width=10, command=lambda: digit('/')).grid(row=6, column=1)
Button(window, text='=', width=10, command=equal).grid(row=6, column=2)

# Row 7
Button(window, text='C', width=10, command=lambda: var.set("")).grid(row=7, column=0)

# Run the application
window.mainloop()