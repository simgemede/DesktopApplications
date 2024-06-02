import tkinter
import tkinter.messagebox

def add():
    add_from_entry = entry.get()
    if add_from_entry != " ":
        listbox.insert(tkinter.END,add_from_entry)
        entry.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showinfo(title=" ", message="You didn't write anything.")

def delete():
    try:
        listbox_selection = listbox.curselection()[0]
        listbox.delete(listbox_selection)
    except IndexError as Error:
        tkinter.messagebox.showinfo(title=" ", message="You have to choose something.")


window = tkinter.Tk()
window.title("To-Do List")
window.geometry("350x320")
window.resizable(width="FALSE",height="FALSE")

frame = tkinter.Frame(window)
frame.pack()

listbox = tkinter.Listbox(frame,height=15,width=40,bg="black",fg="white")
listbox.pack()

entry = tkinter.Entry(window,width=50,bg="white",fg="black")
entry.pack()

buton = tkinter.Button(window,text="Add",width=20,bg="black",fg="white",command=add)
buton.pack(anchor=tkinter.CENTER)
buton1 = tkinter.Button(window,text="Delete",width=20,bg="black",fg="white",command=delete)
buton1.pack(anchor=tkinter.CENTER)

window.mainloop()