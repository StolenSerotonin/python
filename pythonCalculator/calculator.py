import math as m
from tkinter import *

# Create the main window
window = Tk()
window.title("Calculator")
window.configure(bg="grey")
window.geometry("400x600")
window.resizable(True, True)

# Create a frame with a border
frame = Frame(window, bg="grey",borderwidth=5 ,relief="solid")
frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Global variables ew yucky
bypass_val = False
first_number = None
operator = None

# Entry validation
def validate_input(char):
    if bypass_val: return True
    elif char.isdigit() or char == ".":
        return True
    return False

validate_cmd = window.register(validate_input)

# Create entry box
e_font = ("Courier", 24, "bold")
e = Entry(frame, fg="green", bg="black", font=e_font, borderwidth=15, validate="key", validatecommand=(validate_cmd, "%S"))

# Create functions for buttons
def button_click(number):
    global bypass_val
    current = e.get()
    e.delete(0, END)
    bypass_val = True
    e.insert(0, str(current) + str(number))
    bypass_val = False

def button_clear():
    e.delete(0, END)
    
def button_function(func):
    global first_number
    global operator
    first_number = e.get()
    operator = func
    e.delete(0, END)
    
def button_equals():
    global bypass_val
    second_number = e.get()
    e.delete(0, END)
    bypass_val = True
    if operator == None:
        e.insert(0, 0)
    elif second_number == "":
        e.insert(0, 0)
    elif operator == "+" and first_number == str(9) and second_number == str(10):
        e.insert(0, str(21))
    elif operator == "+":
        e.insert(0, str(float(first_number) + float(second_number)))
    elif operator == "-":
        e.insert(0, str(float(first_number) - float(second_number)))
    elif operator == "*":
        e.insert(0, str(float(first_number) * float(second_number)))
    elif operator == "/":
        e.insert(0, str(float(first_number) / float(second_number)))
    bypass_val = False

# Create buttons
bFont = ("Courier", 14, "bold")

add = Button(frame, text="+", font=bFont, command=lambda: button_function("+"))
subtract = Button(frame, text="-", font=bFont, command=lambda: button_function("-"))
multiply = Button(frame, text="*", font=bFont, command=lambda: button_function("*"))
divide = Button(frame, text="/", font=bFont, command=lambda: button_function("/"))
one = Button(frame, text="1", font=bFont, command=lambda: button_click(1))
two = Button(frame, text="2", font=bFont, command=lambda: button_click(2))
three = Button(frame, text="3", font=bFont, command=lambda: button_click(3))
four = Button(frame, text="4", font=bFont, command=lambda: button_click(4))
five = Button(frame, text="5", font=bFont, command=lambda: button_click(5))
six = Button(frame, text="6", font=bFont, command=lambda: button_click(6))
seven = Button(frame, text="7", font=bFont, command=lambda: button_click(7))
eight = Button(frame, text="8", font=bFont, command=lambda: button_click(8))
nine = Button(frame, text="9", font=bFont, command=lambda: button_click(9))
zero = Button(frame, text="0", font=bFont, command=lambda: button_click(0))
decimal = Button(frame, text=".", font=bFont, command=lambda: button_click())
equals = Button(frame, text="=", font=bFont, command=lambda: button_equals())
clear = Button(frame, text="C", font=bFont, command=lambda: button_clear())
delete = Button(frame, text="DEL", font=bFont, command=lambda: button_click())
square = Button(frame, text="x^2", font=bFont, command=lambda: button_click())
sqrt = Button(frame, text="sqrt", font=bFont, command=lambda: button_click())
openParen = Button(frame, text="(", font=bFont, command=lambda: button_click())
closeParen = Button(frame, text=")", font=bFont, command=lambda: button_click())

# Configure the frame to allow dynamic resizing
for i in range(5):
    frame.grid_rowconfigure(i, weight=1)
for j in range(4):
    frame.grid_columnconfigure(j, weight=1)
# Same for window
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
    
# Place the widgets in the frame
e.grid(row=0, column=0, columnspan=4, sticky="nsew")

add.grid(row=1, column=3, sticky="nsew")
subtract.grid(row=2, column=3, sticky="nsew")
multiply.grid(row=3, column=3, sticky="nsew")
divide.grid(row=4, column=2, sticky="nsew")
equals.grid(row=4, column=3, sticky="nsew")
one.grid(row=1, column=0, sticky="nsew")
two.grid(row=1, column=1, sticky="nsew")
three.grid(row=1, column=2, sticky="nsew")
four.grid(row=2, column=0, sticky="nsew")
five.grid(row=2, column=1, sticky="nsew")
six.grid(row=2, column=2, sticky="nsew")
seven.grid(row=3, column=0, sticky="nsew")
eight.grid(row=3, column=1, sticky="nsew")
nine.grid(row=3, column=2, sticky="nsew")
zero.grid(row=4, column=1, sticky="nsew")
clear.grid(row=4, column=0, sticky="nsew")


window.mainloop()



