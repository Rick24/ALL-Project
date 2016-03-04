from tkinter import *
from tkinter import ttk
rw = Tk()

#Hat
button4=ttk.Button(rw,text="Hat")
button4.pack()
mi3=PhotoImage(file="Hat.GIF")
button4.config(image=mi3, compound=RIGHT)
tmi4 = mi3.subsample(7,7)
button4.config(image=tmi4)


#Oranges
button5=ttk.Button(rw,text="Orange")
button5.pack()
mi4=PhotoImage(file="orange.GIF")
button5.config(image=mi4, compound=RIGHT)
tmi5 = mi4.subsample(7,7)
button5.config(image=tmi5)


#Jeans
button6=ttk.Button(rw,text="Jeans")
button6.pack()
mi5=PhotoImage(file="jeans.GIF")
button6.config(image=mi5, compound=RIGHT)
tmi6 = mi5.subsample(7,7)
button6.config(image=tmi6)


#Shirt
button7=ttk.Button(rw,text="Shirt")
button7.pack()
mi6=PhotoImage(file="shirt.GIF")
button7.config(image=mi6, compound=RIGHT)
tmi7 = mi6.subsample(7,7)
button7.config(image=tmi7)

