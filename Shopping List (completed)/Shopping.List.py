import sqlite3
from tkinter import *
from tkinter import ttk
rw = Tk()

basket = {}

priceLabel = ttk.Label(text="Price: ")
priceLabel.pack()
LocationLabel = ttk.Label(text="Location:")
LocationLabel.pack()

def displayInfo(id):
    #print("displayInfo Called")
    conn = sqlite3.connect('itemDB.db')
    c = conn.cursor()
    c.execute('SELECT * FROM food WHERE id = ?', str(id))
    response = c.fetchone()
    price = response[2]
    Location = response[3]
    priceLabel.configure(text="Price: " + str(price))
    LocationLabel.configure(text="Location: " +str(Location))
    conn.close()

#banana

button1=ttk.Button(rw,text="Banana", command = lambda: displayInfo(1))
button1.pack()
mi1=PhotoImage(file="Banana.GIF")
button1.config(image=mi1, compound=RIGHT)
tmi1 = mi1.subsample(7,7)
button1.config(image=tmi1)


#Apple
button2=ttk.Button(rw,text="Apple", command = lambda: displayInfo(2))
button2.pack()
mi2=PhotoImage(file="apple.GIF")
button2.config(image=mi2, compound=RIGHT)
tmi2 = mi2.subsample(7,7)
button2.config(image=tmi2)


#book
button3=ttk.Button(rw,text="Book", command = lambda: displayInfo(3))
button3.pack()
mi3=PhotoImage(file="Book.GIF")
button3.config(image=mi3, compound=RIGHT)
tmi3 = mi3.subsample(5,5)
button3.config(image=tmi3)


#jeans
button4=ttk.Button(rw,text="Jeans", command = lambda: displayInfo(4))
button4.pack()
mi4=PhotoImage(file="jeans2.GIF")
button4.config(image=mi4, compound=RIGHT)
tmi4 = mi4.subsample(5,5)
button4.config(image=tmi4)


#Hoe
button5=ttk.Button(rw,text="Hoe", command = lambda: displayInfo(5))
button5.pack()
mi5=PhotoImage(file="Hoe.GIF")
button5.config(image=mi5, compound=RIGHT)
tmi5 = mi5.subsample(5,5)
button5.config(image=tmi5)


#sugar
button6=ttk.Button(rw,text="Sugar", command = lambda: displayInfo(6))
button6.pack()
mi6=PhotoImage(file="Sugar.GIF")
button6.config(image=mi6, compound=RIGHT)
tmi6 = mi6.subsample(5,5)
button6.config(image=tmi6)


#leather boots
button7=ttk.Button(rw,text="Leather Boots", command = lambda: displayInfo(7))
button7.pack()
mi7=PhotoImage(file="leather.boots.GIF")
button7.config(image=mi7, compound=RIGHT)
tmi7 = mi7.subsample(6,6)
button7.config(image=tmi7)


#shovel
button8=ttk.Button(rw,text="Shovel", command = lambda: displayInfo(8))
button8.pack()
mi8=PhotoImage(file="shovel.GIF")
button8.config(image=mi8, compound=RIGHT)
tmi8 = mi8.subsample(5,5)
button8.config(image=tmi8)

