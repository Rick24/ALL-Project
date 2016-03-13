import sqlite3
from tkinter import *
import time
import math
from tkinter import ttk


class Gui:
    def __init__(self, root):
        self.root = root
        
        self.priceLabel = ttk.Label(text="Price: ")
        self.priceLabel.pack()
        
        self.LocationLabel = ttk.Label(text="Location:")
        self.LocationLabel.pack()


        #banana

        self.button1=ttk.Button(rw,text="Banana", command = lambda: self.displayInfo(1))
        self.button1.pack()
        self.mi1=PhotoImage(file="Banana.GIF")
        self.button1.config(image=self.mi1, compound=RIGHT)
        self.tmi1 = self.mi1.subsample(7,7)
        self.button1.config(image=self.tmi1)


        #Apple
        self.button2=ttk.Button(rw,text="Apple", command = lambda: self.displayInfo(2))
        self.button2.pack()
        self.mi2=PhotoImage(file="apple.GIF")
        self.button2.config(image=self.mi2, compound=RIGHT)
        self.tmi2 = self.mi2.subsample(7,7)
        self.button2.config(image=self.tmi2)


        #book
        self.button3=ttk.Button(rw,text="Book", command = lambda: self.displayInfo(3))
        self.button3.pack()
        self.mi3=PhotoImage(file="book.GIF")
        self.button3.config(image=self.mi3, compound=RIGHT)
        self.tmi3 = self.mi3.subsample(5,5)
        self.button3.config(image=self.tmi3)


        #jeans
        self.button4=ttk.Button(rw,text="Jeans", command = lambda: self.displayInfo(4))
        self.button4.pack()
        self.mi4=PhotoImage(file="jeans2.GIF")
        self.button4.config(image=self.mi4, compound=RIGHT)
        self.tmi4 = self.mi4.subsample(5,5)
        self.button4.config(image=self.tmi4)


        #Hoe
        self.button5=ttk.Button(rw,text="Hoe", command = lambda: self.displayInfo(5))
        self.button5.pack()
        self.mi5=PhotoImage(file="Hoe.GIF")
        self.button5.config(image=self.mi5, compound=RIGHT)
        self.tmi5 = self.mi5.subsample(5,5)
        self.button5.config(image=self.tmi5)


        #sugar
        self.button6=ttk.Button(rw,text="Sugar", command = lambda: self.displayInfo(6))
        self.button6.pack()
        self.mi6=PhotoImage(file="Sugar.GIF")
        self.button6.config(image=self.mi6, compound=RIGHT)
        self.tmi6 = self.mi6.subsample(5,5)
        self.button6.config(image=self.tmi6)


        #leather boots
        self.button7=ttk.Button(rw,text="Leather Boots", command = lambda: self.displayInfo(7))
        self.button7.pack()
        self.mi7=PhotoImage(file="leather.boots.GIF")
        self.button7.config(image=self.mi7, compound=RIGHT)
        self.tmi7 = self.mi7.subsample(6,6)
        self.button7.config(image=self.tmi7)


        #shovel
        self.button8=ttk.Button(rw,text="Shovel", command = lambda: self.displayInfo(8))
        self.button8.pack()
        self.mi8=PhotoImage(file="shovel.GIF")
        self.button8.config(image=self.mi8, compound=RIGHT)
        self.tmi8 = self.mi8.subsample(5,5)
        self.button8.config(image=self.tmi8)

        #timer
        self.var = StringVar()
        self.label = Label(rw, textvariable=self.var, relief=RAISED)
        self.var.set ("0:00")
        self.label.pack()

        self.count = 10
        self.timer()
        
    def displayInfo(self,id):
        #print("displayInfo Called")
        conn = sqlite3.connect('itemDB.db')
        c = conn.cursor()
        c.execute('SELECT * FROM food WHERE id = ?', str(id))
        response = c.fetchone()
        price = response[2]
        Location = response[3]
        self.priceLabel.configure(text="Price: " + str(price))
        self.LocationLabel.configure(text="Location: " +str(Location))
        conn.close()
    
    def timer(self):
       #while self.count != 0:
            self.var.set(self.count)
            if self.count >0:
                self.count -= 1
                
            #time.sleep(1.0)
                self.root.after(1000,self.timer)
        

#for t in range(120,-1,-1):
#    minutes = t / 60
#    seconds = t % 60
#    (str(math.floor(minutes)) + ":" + str(seconds))
#    var.set(str(math.floor(minutes)) + ":" + str(seconds))
#    rw.update_idletasks()
#    time.sleep(1.0)


if __name__ == '__main__':
    rw = Tk()
    g = Gui(rw)
    rw.mainloop()

