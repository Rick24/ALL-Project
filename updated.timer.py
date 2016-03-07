from tkinter import *
import time
import math

root = Tk()
var = StringVar()
label = Label(root, textvariable=var, relief=RAISED)
var.set ("0:00")
label.pack()
#root.mainloop()


for t in range(300,-1,-1):
    minutes = t / 60
    seconds = t % 60
    (str(math.floor(minutes)) + ":" + str(seconds))
    var.set(str(math.floor(minutes)) + ":" + str(seconds))
    root.update_idletasks()
    time.sleep(1.0)

root.mainloop()

    




          
