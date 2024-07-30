import math as m
from tkinter import *

window = Tk()
window.title("Calculator")
window.configure(bg="grey")
window.geometry("400x600")
window.resizable(True, True)

bHeight = 0
bWidth = 0
bPadX = 0
bPadY = 0

# Create a frame with a border
frame = Frame(window, bg="grey",borderwidth=5 ,relief="solid")
frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

label_font = ("Courier", 24, "bold")
e = Entry(frame, text="0", fg="green", bg="black", font=label_font, borderwidth=15)

def button_add():
    return

add = Button(frame, text="+", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
subtract = Button(frame, text="-", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
multiply = Button(frame, text="*", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
divide = Button(frame, text="/", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
one = Button(frame, text="1", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
two = Button(frame, text="2", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
three = Button(frame, text="3", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
four = Button(frame, text="4", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
five = Button(frame, text="5", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
six = Button(frame, text="6", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
seven = Button(frame, text="7", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
eight = Button(frame, text="8", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
nine = Button(frame, text="9", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
zero = Button(frame, text="0", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
decimal = Button(frame, text=".", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
equals = Button(frame, text="=", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
clear = Button(frame, text="C", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
delete = Button(frame, text="DEL", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
square = Button(frame, text="x^2", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
sqrt = Button(frame, text="sqrt", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
openParen = Button(frame, text="(", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)
closeParen = Button(frame, text=")", height=bHeight, width=bWidth, padx=bPadX, pady=bPadY, command=button_add)

# Configure the grid to allow dynamic resizing
for i in range(5):
    frame.grid_rowconfigure(i, weight=1)
for j in range(4):
    frame.grid_columnconfigure(j, weight=1)
    
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
    
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



