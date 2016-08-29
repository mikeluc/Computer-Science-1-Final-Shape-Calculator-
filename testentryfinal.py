from tkinter import *

def showEntryField():
    print("Shape: %s\n Data: %s\n Find: %s\n Value: %s " % (e1.get(), e2.get(), e3.get(), e4.get()))
    
master = Tk()
master.title("Shape Calculator")
master.geometry("500x500")
Label(master, text="What shape do you want to find?").grid(row=0)
Label(master, text="What data would you like to input?").grid(row=1)
Label(master, text="What would you like to calculate?").grid(row=2)
Label(master, text="Enter your value").grid(row=3)



e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)


Button(master, text='quit', command=master.quit).grid(row=5,column=0, sticky=W, pady=4)
Button(master, text='show', command=showEntryField).grid(row=5, column=1, sticky=W, pady=4)
mainloop()
