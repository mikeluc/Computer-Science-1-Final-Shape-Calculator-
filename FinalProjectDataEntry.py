from tkinter import *




    
root = Tk()

root.title("Shape Calculator")
root.geometry("500x500")

app = Frame(root)
app.grid()

e = Entry(root)
e.pack()




label = Label(app, text = "What shape do you want to find?")
label.grid()
e.delete(0, END)
e.insert(0, "hiu")

button1 = Button(app, text = "Enter")
button1.grid()



root.mainloop()

