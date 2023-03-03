import tkinter as tk
import math
win = tk.Tk()
win.title("variables")

def Blacklist(*args):
    for arg in args:
        blacklist.append(arg)

def update():
    pass

i = 2
j = 0
def get_var(vars):
    global i, j
    Slist = []
    for var in vars:
        if var not in blacklist:
            Slist.append(var)

    for var in Slist:
        if j == round(math.sqrt(len(Slist))):
            j = 0
            i += 1
            win.columnconfigure(i, weight=1, minsize=75)
            win.rowconfigure(i, weight=1, minsize=50)

        frame = tk.Frame(
            master = win,
            relief = tk.RAISED,
            borderwidth = 0.3,
            background = "gray"
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        tk.Label(
            master = frame, 
            text = f"{var} is {type(eval(var))} \n equals = '{eval(var)}'"
        ).grid(padx=5, pady=5)

        if type(eval(var) == int):
            entry = tk.Entry(
                master = frame,
                width = 10,
            ).grid(padx=5, pady=5)
            result = tk.Label(
                master = frame,
                text = f"{var} = {eval(var)}",
                background = "gray"
            ).grid(padx=5, pady=5)

        j += 1

blacklist = ["var"]
for var in dir():
    blacklist.append(var)

vad = 2
dar = "streee"
cat = 56
clam = 42.5
camberage = ["university", "failed"]
iamdead = "dead"
lukas = "kinda gay"
alvar = (25, 69)
anal = "no"

get_var(dir())

win.mainloop()
