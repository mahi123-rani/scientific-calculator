import tkinter as tk
import math

def press(key):
    entry_var.set(entry_var.get() + str(key))

def clear():
    entry_var.set("")

def delete():
    entry_var.set(entry_var.get()[:-1])

def calculate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

def scientific(func):
    try:
        value = float(entry_var.get())
        if func == "sqrt":
            entry_var.set(str(math.sqrt(value)))
        elif func == "sin":
            entry_var.set(str(math.sin(math.radians(value))))
        elif func == "cos":
            entry_var.set(str(math.cos(math.radians(value))))
        elif func == "tan":
            entry_var.set(str(math.tan(math.radians(value))))
        elif func == "log":
            entry_var.set(str(math.log10(value)))
        elif func == "ln":
            entry_var.set(str(math.log(value)))
    except:
        entry_var.set("Error")

# GUI Window
root = tk.Tk()
root.title("Scientific Calculator")
entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=6)

# Buttons Layout
buttons = [
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),("sqrt",1,4),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),("sin",2,4),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),("cos",3,4),
    ("0",4,0),(".",4,1),("=",4,2),("+",4,3),("tan",4,4),
    ("C",5,0),("DEL",5,1),("log",5,2),("ln",5,3)
]

for (text,r,c) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=8, height=2, command=calculate).grid(row=r, column=c)
    elif text == "C":
        tk.Button(root, text=text, width=8, height=2, command=clear).grid(row=r, column=c)
    elif text == "DEL":
        tk.Button(root, text=text, width=8, height=2, command=delete).grid(row=r, column=c)
    elif text in ["sqrt","sin","cos","tan","log","ln"]:
        tk.Button(root, text=text, width=8, height=2, command=lambda t=text: scientific(t)).grid(row=r, column=c)
    else:
        tk.Button(root, text=text, width=8, height=2, command=lambda t=text: press(t)).grid(row=r, column=c)

root.mainloop()
