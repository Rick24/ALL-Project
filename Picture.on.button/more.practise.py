#from tkinter import ttk
from tkinter import*
#rw = Tk()
Window = Tk()

canvas = Canvas(Window, width=400, height=300, bg= 'white')
#button 
button1= ttk.Button(rw,text="Banana")
button1.pack()
mi=PhotoImage(master = Window, file="Banana.GIF")
button1.config(image=mi, compound=RIGHT)
tmi1 = mi.subsample(6,6)
button1.config(image=tmi1)

canvas.pack()
Window.mainloop()
