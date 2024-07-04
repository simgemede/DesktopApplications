import tkinter as tk
from tkinter import *
from tkinter.filedialog import *

def open_func():
    file = askopenfile(mode="r", filetypes=[("text files", ".txt")])
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)

def save_func():
    new_file = asksaveasfile(mode="w", filetypes=[("text files", ".txt")])
    if new_file is None:
        return
    text = str(entry.get())
    new_file.write(text)
    new_file.close()

def new_func():
    entry.delete(1.0,END)

window = tk.Tk()
window.geometry("400x500")
window.resizable(False, False)
window.title("Notepad")
window.config(bg="white")
frame_top = tk.Frame(window)
frame_top.pack(padx=10, pady=5, anchor="nw")

open_button = tk.Button(window, text="Open", bg="white", command=open_func)
open_button.place(x=5, y=10)

save_button = tk.Button(window, text="Save", bg="white", command=save_func)
save_button.place(x=45, y=10)

delete_button = tk.Button(window, text="New", bg="white", command=new_func)
delete_button.place(x=80, y=10)

exit_button = tk.Button(window, text="Exit", bg="white", command=exit)
exit_button.place(x=115, y=10)

entry = tk.Text(window, wrap="word", bg="#efe5f6", font=("arial",15))
entry.pack(padx=5, pady=25, expand=True, fill="both")

window.mainloop()