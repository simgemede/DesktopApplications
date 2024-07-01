import tkinter as tk
import random

colors = ["Red","Blue","Green","Black","White",
           "Yellow","Pink","Brown","Purple","Gray","Orange"]

score = 0

remaining_time = 90

def start_game(event):
    if remaining_time == 90:
        countdown()
    enter_color()

def enter_color():
    global score
    global remaining_time
    if remaining_time > 0:
        entry.focus_set()
        if entry.get().lower() == colors[1].lower():
            score += 1
        entry.delete(0,tk.END)
        random.shuffle(colors)
        color_label.config(fg = str(colors[1]), text= str(colors[0]))
        score_label.config(text= "Score:" + str(score))

def countdown():
    global remaining_time
    if remaining_time > 0:
        remaining_time -= 1
        time_label.config(text="Remaining Time:" + str(remaining_time))
        time_label.after(1000, countdown)

window = tk.Tk()
window.title("Color Game")
window.geometry("300x200")
window.resizable(False,False)

enter_color_label = tk.Label(window, text="Enter the color.",
                            font=("Arial",12,"bold"))
enter_color_label.pack()

score_label = tk.Label(window, text="Press the enter key to get started.")
score_label.pack()

time_label = tk.Label(window, text="Remaining Time:" + str(remaining_time), font=("Arial",12))
time_label.pack()

color_label = tk.Label(window, font=("Arial",60))
color_label.pack()

entry = tk.Entry(window)
window.bind("<Return>", start_game)
entry.pack()
entry.focus_set()

window.mainloop()