import tkinter as tk
from tkinter import ttk
from tkinter import font

window = tk.Tk()
window.title("Creating A Font")

frame = tk.Frame(window)

def update(self):
    SampleFont.configure(family=ChooseAFontStyle_combobox.get())
    SampleFont.configure(size=ChooseAFontSize_combobox.get())
    SampleFont.configure(weight=isBold())
    SampleFont.configure(slant=isItalic())
    SampleFont.configure(underline=isUnderline())
    SampleFont.configure(overstrike=isOverstrike())
    window.update()

def result():
    SampleFont.configure(weight=isBold())
    SampleFont.configure(slant=isItalic())
    SampleFont.configure(underline=isUnderline())
    SampleFont.configure(overstrike=isOverstrike())

def isBold():
    if(Bold.get()):
        return "bold"
    else:
        return "normal"
def isItalic():
    if(Italic.get()):
        return 'italic'
    else:
        return 'roman'
def isUnderline():
    if(Underline.get()):
        return True
    else:
        return False
def isOverstrike():
    if(Overstrike.get()):
        return True
    else:
        return False

frame1 = tk.Frame(frame)
frame1.grid(column=0, row=0)

FontStyleLabel = ttk.Label(frame1, text="Choose a font style:")
FontStyleLabel.grid(column=0, row=0)
ChooseAFontStyle = tk.StringVar()
ChooseAFontStyle_combobox = ttk.Combobox(FontStyleLabel, width=30, textvariable= ChooseAFontStyle, state="readonly")
ChooseAFontStyle_combobox["values"] = font.families()
ChooseAFontStyle_combobox.grid(column=0, row=1)
ChooseAFontStyle_combobox.current(0)

FontSizeLabel = ttk.Label(frame, text = "Choose a font size:")
FontSizeLabel.grid(column=1, row=0)
ChooseAFontSize = tk.StringVar()
ChooseAFontSize_combobox = ttk.Combobox(frame, width=10, textvariable=ChooseAFontSize, state="readonly")
ChooseAFontSize_combobox["values"] = list(range(2,50))
ChooseAFontSize_combobox.grid(column=1, row=1)
ChooseAFontSize_combobox.current(0)

textLabel = ttk.Label(frame, text="Text to be displayed")
textLabel.grid(column=0,row=2)

frame2 = tk.Frame(frame)
frame2.grid(column=0,row=1)

SampleText = tk.StringVar()
SampleText.set("Sample Text")
SampleText_entry = ttk.Entry(frame, width=30, textvariable=SampleText)
SampleText_entry.grid(column=0, row=3)

Bold = tk.IntVar()
Italic = tk.IntVar()
Underline = tk.IntVar()
Overstrike = tk.IntVar()
text = ["Bold", "Italic", "Underline", "Overstrike"]

checkbutton1 = tk.Checkbutton(frame2, text=text[0], variable=Bold, command=result)
checkbutton1.grid(column=0,row=0, sticky=tk.W)
checkbutton2 = tk.Checkbutton(frame2, text=text[1], variable=Italic, command=result)
checkbutton2.grid(column=1,row=0, sticky=tk.W)
checkbutton3 = tk.Checkbutton(frame2, text=text[2], variable=Underline, command=result)
checkbutton3.grid(column=2,row=0, sticky=tk.W)
checkbutton4 = tk.Checkbutton(frame2, text=text[3], variable=Overstrike, command=result)
checkbutton4.grid(column=3,row=0, sticky=tk.W)

LabelFrame = ttk.LabelFrame(frame, text='Sample Text')
LabelFrame.grid(column=0, row=4)

SampleFont = font.Font(family=ChooseAFontStyle_combobox.get(),size=ChooseAFontSize_combobox.get())

SampleLabel = ttk.Label(LabelFrame)
SampleLabel["textvariable"] = SampleText
SampleLabel["font"] = SampleFont
SampleLabel.grid(column=0,row=0)

ChooseAFontStyle_combobox.bind("<<ComboboxSelected>>", update)
ChooseAFontSize_combobox.bind("<<ComboboxSelected>>", update)

frame.pack()
window.mainloop()