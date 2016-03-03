from tkinter import *
from tkinter import ttk
rw = Tk()
#banana
button1=ttk.Button(rw,text="Banana")
button1.pack()
mi=PhotoImage(file="Banana.GIF")
button1.config(image=mi, compound=RIGHT)
tmi1 = mi.subsample(7,7)
button1.config(image=tmi1)


#Apple
button2=ttk.Button(rw,text="Apple")
button2.pack()
mi1=PhotoImage(file="apple.GIF")
button2.config(image=mi1, compound=RIGHT)
tmi2 = mi1.subsample(7,7)
button2.config(image=tmi2)


#Strong_poison
button3=ttk.Button(rw,text="Strong poison")
button3.pack()
mi2=PhotoImage(file="Book.gif")
button3.config(image=mi2, compound=RIGHT)
tmi3 = mi2.subsample(7,7)
button3.config(image=tmi3)


