from time import strftime
import tkinter as tk
from tkinter import Label

window = tk.Tk()
window.title("Digital Clock")
window.geometry("200x80")
window.resizable(False, False)

clock_label = Label(
    window, bg= "black", fg= "white", font= ("Arial", 30, "bold"), relief = "flat"
)
clock_label.place(x= 20, y= 20)

def label_update():

    time = strftime("%H: %M: %S\n %d-%m-%Y ")
    clock_label.configure(text= time)
    clock_label.after(80, label_update)
    clock_label.pack(anchor= "center")

label_update()
window.mainloop()