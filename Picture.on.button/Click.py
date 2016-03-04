import sqlite3
from tkinter import *
from tkinter import ttk
rw = Tk()

basket = {}

priceLabel = ttk.Label(text="Price: ")
priceLabel.pack()
quantityLabel = ttk.Label(text="Quantity")
quantityLabel.pack()

def displayInfo(id):
    #print("displayInfo Called")
    conn = sqlite3.connect('itemDB.db')
    c = conn.cursor()
    c.execute('SELECT * FROM food WHERE id = ?', str(id))
    response = c.fetchone()
    price = response[2]
    quantity = response[3]
    priceLabel.configure(text="Price: " + str(price))
    quantityLabel.configure(text="Quantity: " +str(quantity))
    conn.close()

#banana

button1=ttk.Button(rw,text="Banana", command = lambda: displayInfo(1))
button1.pack()

mi=PhotoImage(file="Banana.GIF")
button1.config(image=mi, compound=RIGHT)
tmi1 = mi.subsample(6,6)
button1.config(image=tmi1)


#Apple

button2=ttk.Button(rw,text="Apple", command= lambda: displayInfo(2))
button2.pack()
mi1=PhotoImage(file="apple.GIF")
button2.config(image=mi1, compound=RIGHT)
tmi2 = mi1.subsample(7,7)
button2.config(image=tmi2)

#oranges
button3=ttk.Button(rw,text="oranges", command= lambda: displayInfo(3))
button3.pack()
mi1=PhotoImage(file="apple.GIF")
button3.config(image=mi1, compound=RIGHT)
tmi3 = mi1.subsample(7,7)
button3.config(image=tmi3)

