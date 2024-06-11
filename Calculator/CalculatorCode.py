import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("230x240")
window.title("Calculator")
window.resizable(False,False)

def equals_f():
    try:

        if entry.get() == "":
            entry.insert("end", "error")
        elif entry.get()[0] == "0":
            entry.delete(0, "end")
            entry.insert("end", "error")
        else:
            func = entry.get()
            func = eval(func)
            entry.insert("end", "=")
            entry.insert("end", func)
    except SyntaxError:
        entry.insert("end", "invalid input")

entry = tk.Entry(window, width=20, borderwidth=3, relief=SUNKEN)
entry.grid(padx=10, pady=10, sticky="w", row=0, column=0)

delete_button = tk.Button(window, text="C", width=6, command=lambda:entry.delete(0,"end"), bg="red", borderwidth=2, relief=RAISED)
delete_button.grid(padx=160, pady=10, sticky="w", row=0)

nine_button = tk.Button(window, text="9", width=6, command=lambda:entry.insert("end","9"), borderwidth=2, relief=RAISED)
nine_button.grid(padx=15, pady=5, sticky="w", row=1)

eight_button = tk.Button(window, text="8", width=6, command=lambda:entry.insert("end","8"), borderwidth=2, relief=RAISED)
eight_button.grid(padx=65, pady=5, sticky="w", row=1)

seven_button = tk.Button(window, text="7", width=6, command=lambda:entry.insert("end","7"), borderwidth=2, relief=RAISED)
seven_button.grid(padx=115, pady=5, sticky="w", row=1)

plus_button = tk.Button(window, text="+", width=6, command=lambda:entry.insert("end","+"), borderwidth=2, relief=RAISED)
plus_button.grid(padx=165, pady=5, sticky="w", row=1)


six_button= tk.Button(window, text="6", width=6, command=lambda:entry.insert("end","6"), borderwidth=2, relief=RAISED)
six_button.grid(padx=15, pady=5, sticky="w", row=2)

five_button = tk.Button(window, text="5", width=6, command=lambda:entry.insert("end","5"), borderwidth=2, relief=RAISED)
five_button.grid(padx=65, pady=5, sticky="w", row=2)

four_button = tk.Button(window, text="4", width=6, command=lambda:entry.insert("end","4"), borderwidth=2, relief=RAISED)
four_button.grid(padx=115, pady=5, sticky="w", row=2)

minus_button = tk.Button(window, text="-", width=6, command=lambda:entry.insert("end","-"), borderwidth=2, relief=RAISED)
minus_button.grid(padx=165, pady=5, sticky="w", row=2)

three_button= tk.Button(window, text="3", width=6, command=lambda:entry.insert("end","3"), borderwidth=2, relief=RAISED)
three_button.grid(padx=15, pady=5, sticky="w", row=3)

two_button = tk.Button(window, text="2", width=6, command=lambda:entry.insert("end","2"), borderwidth=2, relief=RAISED)
two_button.grid(padx=65, pady=5, sticky="w", row=3)

one_button = tk.Button(window, text="1", width=6, command=lambda:entry.insert("end","1"), borderwidth=2, relief=RAISED)
one_button.grid(padx=115, pady=5, sticky="w", row=3)

crash_button = tk.Button(window, text="*", width=6, command=lambda:entry.insert("end","*"), borderwidth=2, relief=RAISED)
crash_button.grid(padx=165, pady=5, sticky="w", row=3)


zero_button = tk.Button(window, text="0", width=6, command=lambda:entry.insert("end","6"), borderwidth=2, relief=RAISED)
zero_button.grid(padx=15, pady=5, sticky="w", row=4)

double_zero_button = tk.Button(window, text="00", width=6, command=lambda:entry.insert("end","5"), borderwidth=2, relief=RAISED)
double_zero_button.grid(padx=65, pady=5, sticky="w", row=4)

comma_button = tk.Button(window, text=",", width=6, command=lambda:entry.insert("end","4"), borderwidth=2, relief=RAISED)
comma_button.grid(padx=115, pady=5, sticky="w", row=4)

division_button = tk.Button(window, text="/", width=6, command=lambda:entry.insert("end","-"), borderwidth=2, relief=RAISED)
division_button.grid(padx=165, pady=5, sticky="w", row=4)

equals_button = tk.Button(window, text="=", width=18, command=equals_f, borderwidth=2, relief=RAISED)
equals_button.grid(padx=15, pady=5, sticky="w", row=5)

percent_button = tk.Button(window, text="%", width=6, command=lambda:entry.insert("end","%"), borderwidth=2, relief=RAISED)
percent_button.grid(padx=165, pady=5, sticky="w", row=5)

window.mainloop()