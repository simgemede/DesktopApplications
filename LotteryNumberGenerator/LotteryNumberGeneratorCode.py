import random
from tkinter import *
import tkinter as tk

def func():
    x = random.randint(1, 90)
    q = random.randint(1, 90)
    w = random.randint(1, 90)
    e = random.randint(1, 90)
    r = random.randint(1, 90)
    t = random.randint(1, 90)
    no1.set(x)
    no2.set(q)
    no3.set(w)
    no4.set(e)
    no5.set(r)
    no6.set(t)
    return

window = tk.Tk()
window.geometry("800x180")
window.title("Lottery Number Generator")

no1 = StringVar()
no2 = StringVar()
no3 = StringVar()
no4 = StringVar()
no5 = StringVar()
no6 = StringVar()

frame1 = Frame(window)
frame1.pack(side=TOP)

label1 = Label(frame1, text= "Lottery Number Generator", font= ("Calibri,46"), fg= "blue")
label1.pack(side=TOP)

frame2 = Frame(window)
frame2.pack(side=TOP)

entry = Entry(frame1, textvariable= no1, bd=20, insertwidth= 1, font=("Arial",30), justify= "center", width= 4)
entry.pack(side=LEFT)
entry.config(state= "readonly")
entry2 = Entry(frame1, textvariable= no2, bd=20, insertwidth= 1, font=("Arial",30), justify= "center", width= 4)
entry2.pack(side=LEFT)
entry2.config(state= "readonly")
entry3 = Entry(frame1, textvariable= no3, bd=20, insertwidth= 1, font=("Arial",30), justify= "center", width= 4)
entry3.pack(side=LEFT)
entry3.config(state= "readonly")
entry4 = Entry(frame1, textvariable= no4, bd=20, insertwidth= 1, font=("Arial",30), justify= "center", width= 4)
entry4.pack(side=LEFT)
entry4.config(state= "readonly")
entry5 = Entry(frame1, textvariable= no5, bd=20, insertwidth= 1, font=("Arial",30), justify= "center", width= 4)
entry5.pack(side=LEFT)
entry5.config(state= "readonly")
entry6 = Entry(frame1, textvariable= no6, bd=20, insertwidth= 1, font=("Arial",30), justify= "center", width= 4)
entry6.pack(side=LEFT)
entry6.config(state= "readonly")

frame3 = Frame(window)
frame3.pack(side=TOP)
buton1 = Button(frame3, padx=8, width=20, pady=8, bd=8, font=("Arial",12), text="Generate random numbers.", bg="black", fg="white", command=func)
buton1.pack(side=TOP)

window.mainloop()