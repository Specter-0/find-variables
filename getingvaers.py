import tkinter as tk
import math
win = tk.Tk()
win.title("variables")

def Blacklist(*args):
    for arg in args:
        blacklist.append(arg)
        
row = 0
column = 0

def get_var(vars):
    Slist = []
    Make.column = 0
    Make.row = 0
    for var in vars:
        if var not in blacklist and not var.startswith("__"):
            Slist.append(var)
    print(Slist)
    for var in Slist:
        if Make.column == round(math.sqrt(len(Slist))):
            Make.column = 0
            Make.row += 1
            win.columnconfigure(Make.column, weight=1, minsize=75)
            win.rowconfigure(Make.row, weight=1, minsize=50)
        square = Make(var)
        Make.column += 1


class Make():
    def update(self, event):
        v = self.entry.get()
        self.result["text"] = f"{self.var} = {eval(v)}"
        #self.content["text"] = f"{v} is {type(eval(v))} \n equals = '{eval(v)}'"

    def __init__(self, var):
        self.var = var
        self.frame = tk.Frame(
            master = win,
            relief = tk.RAISED,
            borderwidth = 0.3,
            background = "gray"
        )
        self.frame.grid(row=self.row, column=self.column, padx=5, pady=5)
        self.content = tk.Label(
            master = self.frame, 
            text = f"{self.var} is {type(eval(self.var))} \n equals = '{eval(self.var)}'"
        ).grid(padx=5, pady=5)

        if type(eval(self.var)) in [float, int]:
            self.result = tk.Label(
                master = self.frame,
                text = f"{self.var} = {eval(self.var)}",
                background = "gray"
            )
            self.result.grid(padx=5, pady=5)
            self.entry = tk.Entry(
                master = self.frame,
                width = 10
            )
            self.entry.grid(padx=5, pady=5)
            self.entry.bind("<Return>", self.update)

blacklist = ["var"]
for dont_use_this_variable in dir():
    blacklist.append(dont_use_this_variable)

del(dont_use_this_variable)

vad = 2
dar = "streee"
cat = 56
clam = 42.5
camberage = ["university", "failed"]
iamdead = True
lukas = "kinda gay"
alvar = (25, 69)
virgin = "yes"

get_var(dir())


#get_var(dir())

#get_var(dir())

win.mainloop()
