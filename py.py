import tkinter as tk
win = tk.Tk()

def Blacklist(var):
    blacklist.append(var)

def get_var(vars):
    print(vars)
    for var in vars:
        if var not in blacklist:
            tk.Label(text=f"{var} is {type(eval(var))} and has the value {eval(var)}").pack()
            # print(f"{var} is {type(eval(var))} and has the value {eval(var)}")

blacklist = ["var"]
for var in dir():
    blacklist.append(var)

vad = 2
dar = "streee"

get_var(dir())

win.mainloop()
