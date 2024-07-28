import math as m
import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.configure(bg="grey")
window.geometry("400x600")
window.resizable(True, True)

bHeight = 2
bwidth = 4

label_font = ("Courier", 24, "bold")
label = tk.Label(text="0", fg="black", bg="grey", font=label_font)

add = tk.Button(text="+", height=bHeight, width=bwidth)
subtract = tk.Button(text="-", height=bHeight, width=bwidth)
multiply = tk.Button(text="*", height=bHeight, width=bwidth)
divide = tk.Button(text="/", height=bHeight, width=bwidth)
one = tk.Button(text="1", height=bHeight, width=bwidth)
two = tk.Button(text="2", height=bHeight, width=bwidth)
three = tk.Button(text="3", height=bHeight, width=bwidth)
four = tk.Button(text="4", height=bHeight, width=bwidth)
five = tk.Button(text="5", height=bHeight, width=bwidth)
six = tk.Button(text="6", height=bHeight, width=bwidth)
seven = tk.Button(text="7", height=bHeight, width=bwidth)
eight = tk.Button(text="8", height=bHeight, width=bwidth)
nine = tk.Button(text="9", height=bHeight, width=bwidth)
zero = tk.Button(text="0", height=bHeight, width=bwidth)
decimal = tk.Button(text=".", height=bHeight, width=bwidth)
equals = tk.Button(text="=", height=bHeight, width=bwidth)
clear = tk.Button(text="C", height=bHeight, width=bwidth)
delete = tk.Button(text="DEL", height=bHeight, width=bwidth)
square = tk.Button(text="x^2", height=bHeight, width=bwidth)
sqrt = tk.Button(text="sqrt", height=bHeight, width=bwidth)
openParen = tk.Button(text="(", height=bHeight, width=bwidth)
closeParen = tk.Button(text=")", height=bHeight, width=bwidth)
# blank1 = tk.Button(text="", height=bHeight, width=bwidth)
# blank2 = tk.Button(text="", height=bHeight, width=bwidth)

# Configure the grid to allow dynamic resizing
for i in range(7):  # There are 7 rows including the labels and buttons
    window.grid_rowconfigure(i, weight=1)
for j in range(4):
    window.grid_columnconfigure(j, weight=1)

# Place the widgets in the grid with sticky properties
label.grid(row=0, column=0, columnspan=4, sticky="nsew")

add.grid(row=1, column=3, sticky="nsew")
subtract.grid(row=2, column=3, sticky="nsew")
multiply.grid(row=3, column=3, sticky="nsew")
divide.grid(row=4, column=3, sticky="nsew")
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
decimal.grid(row=4, column=2, sticky="nsew")
clear.grid(row=4, column=0, sticky="nsew")
equals.grid(row=5, column=3, sticky="nsew")
delete.grid(row=5, column=0, sticky="nsew")
square.grid(row=5, column=1, sticky="nsew")
sqrt.grid(row=5, column=2, sticky="nsew")
openParen.grid(row=6, column=0, sticky="nsew")
closeParen.grid(row=6, column=1, sticky="nsew")
# blank1.grid(row=6, column=2, sticky="nsew")
# blank2.grid(row=6, column=3, sticky="nsew")

window.mainloop()



