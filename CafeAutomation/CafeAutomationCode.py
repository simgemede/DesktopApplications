import tkinter as tk

window = tk.Tk()
window.geometry("1000x500")
window.resizable(width="FALSE",height="FALSE")
window.title("Cafe Automation")

total = tk.StringVar()

def Reset():
    entry_drink1.delete(0,tk.END)
    entry_drink2.delete(0,tk.END)
    entry_drink3.delete(0,tk.END)
    entry_drink4.delete(0,tk.END)
    entry_drink5.delete(0,tk.END)
    entry_drink6.delete(0,tk.END)
    entry_drink7.delete(0,tk.END)

def Collect():

    try: d1 = int(turkish_coffee.get())
    except: d1 = 0

    try: d2 = int(milk_coffee.get())
    except: d2 = 0

    try: d3 = int(filter_coffee.get())
    except: d3 = 0

    try: d4 = int(lemonade.get())
    except: d4 = 0

    try: d5 = int(cola.get())
    except: d5 = 0

    try: d6 = int(soda.get())
    except: d6 = 0

    try: d7 = int(water.get())
    except: d7 = 0

    drink1 = 50 * d1
    drink2 = 60 * d2
    drink3 = 70 * d3
    drink4 = 70 * d4
    drink5 = 40 * d5
    drink6 = 30 * d6
    drink7 = 15 * d7

    total_money = drink1 + drink2 + drink3 + drink4 + drink5 + drink6 + drink7
    total.set(total_money)

label = tk.Label(window,text="Cafe Automation",bg="gray",fg="white",font=("arial,30"),width="300",height="2")
label.pack()

frame = tk.Frame(window,bg="light gray",width=300,height=350)
frame.place(x=10,y=120)

label1 = tk.Label(frame,text="Menu",font=("Gabriola",30,"bold"),bg="light gray")
label1.place(x=100,y=0)

label_drink1 = tk.Label(frame,text="Turkish Coffee .... 50 TL",fg="black",bg="light gray",font=("Lucida Calligraphy",13,"bold"))
label_drink1.place(x=25,y=80)
label_drink2 = tk.Label(frame,text="Milk Coffee ......... 60 TL",fg="black",bg="light gray",font=("Lucida Calligraphy",13,"bold"))
label_drink2.place(x=25,y=110)
label_drink3 = tk.Label(frame,text="Filter Coffee ....... 70 TL",fg="black",bg="light gray",font=("Lucida Calligraphy",13,"bold"))
label_drink3.place(x=25,y=140)
labelpoint = tk.Label(frame,text="......................................",fg="black",bg="light gray",font=("Lucida Calligraphy",13,"bold"))
labelpoint.place(x=25,y=170)
label_drink4 = tk.Label(frame,text="Lemonade ........... 70 TL",fg="black",bg="light gray",font=("Lucida Calligraphy",13,"bold"))
label_drink4.place(x=25,y=200)
label_drink5 = tk.Label(frame,text="Cola .................... 40 TL",fg="black",bg="light gray",font=("Lucida Calligraphy",13,"bold"))
label_drink5.place(x=25,y=230)
label_drink6 = tk.Label(frame,text="Soda .................... 30 TL",fg="black",bg="light gray",font=("Lucida Calligraphy",13,"bold"))
label_drink6.place(x=25,y=260)
label_drink7 = tk.Label(frame,text="Water ................. 15 TL",fg="black",bg="light gray",font=("Lucida Calligraphy",13,"bold"))
label_drink7.place(x=25,y=290)

frame2 = tk.Frame(window,height=370,width=300)
frame2.pack()

turkish_coffee = tk.StringVar()
milk_coffee = tk.StringVar()
filter_coffee = tk.StringVar()
lemonade = tk.StringVar()
cola = tk.StringVar()
soda = tk.StringVar()
water = tk.StringVar()
total = tk.StringVar()

label_drinkk1 = tk.Label(frame2,font=("arial",15,"bold"),text="Turkish Coffee",fg="black",bg="light gray")
label_drinkk1.place(x=20,y=50)
label_drinkk2 = tk.Label(frame2,font=("arial",15,"bold"),text="Milk Coffee",fg="black",bg="light gray")
label_drinkk2.place(x=20,y=90)
label_drinkk3 = tk.Label(frame2,font=("arial",15,"bold"),text="Filter Coffee",fg="black",bg="light gray")
label_drinkk3.place(x=20,y=130)
label_drinkk4 = tk.Label(frame2,font=("arial",15,"bold"),text="Lemonade",fg="black",bg="light gray")
label_drinkk4.place(x=20,y=170)
label_drinkk5 = tk.Label(frame2,font=("arial",15,"bold"),text="Cola",fg="black",bg="light gray")
label_drinkk5.place(x=20,y=210)
label_drinkk6 = tk.Label(frame2,font=("arial",15,"bold"),text="Soda",fg="black",bg="light gray")
label_drinkk6.place(x=20,y=250)
label_drinkk7 = tk.Label(frame2,font=("arial",15,"bold"),text="Water",fg="black",bg="light gray")
label_drinkk7.place(x=20,y=290)

entry_drink1 = tk.Entry(frame2,font=("arial",15,"bold"),textvariable=turkish_coffee,width=5)
entry_drink1.place(x=170,y=50)
entry_drink2 = tk.Entry(frame2,font=("arial",15,"bold"),textvariable=milk_coffee,width=5)
entry_drink2.place(x=170,y=90)
entry_drink3 = tk.Entry(frame2,font=("arial",15,"bold"),textvariable=filter_coffee,width=5)
entry_drink3.place(x=170,y=130)
entry_drink4 = tk.Entry(frame2,font=("arial",15,"bold"),textvariable=lemonade,width=5)
entry_drink4.place(x=170,y=170)
entry_drink5 = tk.Entry(frame2,font=("arial",15,"bold"),textvariable=cola,width=5)
entry_drink5.place(x=170,y=210)
entry_drink6 = tk.Entry(frame2,font=("arial",15,"bold"),textvariable=soda,width=5)
entry_drink6.place(x=170,y=250)
entry_drink7 = tk.Entry(frame2,font=("arial",15,"bold"),textvariable=water,width=5)
entry_drink7.place(x=170,y=290)

buton_reset = tk.Button(frame2,fg="black",bg="light gray",font=("arial",15,"bold"),width=6,text="Reset",command=Reset)
buton_reset.place(x=30,y=330)

buton_collect = tk.Button(frame2,fg="black",bg="light gray",font=("arial",15,"bold"),width=6,text="Collect",command=Collect)
buton_collect.place(x=125,y=330)

frame3 = tk.Frame(window,width=300,height=400)
frame3.place(x=700, y=120)

label_total = tk.Label(frame3,text="Total",font=("calibri",20),bg="light gray")
label_total.place(x=70, y=10)

entry_total = tk.Entry(frame3,font=("arial",15,"bold"),textvariable=total,width=15,bg="light gray")
entry_total.place(x=20, y=70)

window.mainloop()