# Step 1: importing
from tkinter import *
from tkinter import ttk
from tkinter import font

# Step 2: GUI Interaction
window = Tk()
window.geometry("300x400")
window.title("Calculator")

# Step 3: Adding inputs
# Entry Box
entry_font = font.Font(size=14, weight="bold")
e = ttk.Entry(window, width=21, justify="right", font=entry_font)
e.place(x=30, y=20, height=50)

# Initialize variables
math = ""
i = 0

# Number button logic
def click(num):
    e.insert(END, num)

# Number Buttons
b=ttk.Button(window, text='1', width=12, command=lambda: click(1))
b.place(x=30, y=90, height=40)
b=ttk.Button(window, text='2', width=12, command=lambda: click(2))
b.place(x=110, y=90, height=40)
b=ttk.Button(window, text='3', width=12, command=lambda: click(3))
b.place(x=190, y=90, height=40)
b=ttk.Button(window, text='4', width=12, command=lambda: click(4))
b.place(x=30, y=140, height=40)
b=ttk.Button(window, text='5', width=12, command=lambda: click(5))
b.place(x=110, y=140, height=40)
b=ttk.Button(window, text='6', width=12, command=lambda: click(6))
b.place(x=190, y=140, height=40)
b=ttk.Button(window, text='7', width=12, command=lambda: click(7))
b.place(x=30, y=190, height=40)
b=ttk.Button(window, text='8', width=12, command=lambda: click(8))
b.place(x=110, y=190, height=40)
b=ttk.Button(window, text='9', width=12, command=lambda: click(9))
b.place(x=190, y=190, height=40)
b=ttk.Button(window, text='0', width=12, command=lambda: click(0))
b.place(x=30, y=240, height=40)

# Operator functions
def add():
    global i, math
    if e.get():
        i = int(e.get())
        math = "addition"
        e.delete(0, END)

def sub():
    global i, math
    if e.get():
        i = int(e.get())
        math = "subtraction"
        e.delete(0, END)

def multi():
    global i, math
    if e.get():
        i = int(e.get())
        math = "multiplication"
        e.delete(0, END)

def div():
    global i, math
    if e.get():
        i = int(e.get())
        math = "division"
        e.delete(0, END)

# Operator Buttons
b=ttk.Button(window, text='+', width=12, command=add)
b.place(x=110, y=240, height=40)
b=ttk.Button(window, text='-', width=12, command=sub)
b.place(x=190, y=240, height=40)
b=ttk.Button(window, text='*', width=12, command=multi)
b.place(x=30, y=290, height=40)
b=ttk.Button(window, text='/', width=12, command=div)
b.place(x=110, y=290, height=40)

# Equal button logic
def equal():
    try:
        n2 = int(e.get())
        e.delete(0, END)

        if math == "addition":
            e.insert(0, i + n2)
        elif math == "subtraction":
            e.insert(0, i - n2)
        elif math == "multiplication":
            e.insert(0, i * n2)
        elif math == "division":
            if n2 == 0:
                e.insert(0, "Error")
            else:
                e.insert(0, i / n2)
        else:
            e.insert(0, "Error")

    except ZeroDivisionError:
        e.insert(0, "Error")

b=ttk.Button(window, text='=', width=12, command=equal)
b.place(x=190, y=290, height=40)

# Clear function
def clear():
    e.delete(0, END)

b= ttk.Button(window, text='Clear', width=20, command=clear)
b.place(x=90, y=350, height=40)

# Step 4: mainloop
window.mainloop()
