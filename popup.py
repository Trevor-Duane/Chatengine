from tkinter import *
from tkinter import ttk
gui = Tk()
gui.geometry("400x400")
#make sure first is capital and second is not
gui.title("Please Login To Acess This Application")
a = Label(gui ,text="User Name").grid(row=0,column = 0)

b = Label(gui ,text="Password").grid(row=1,column = 0)

e = Entry(gui).grid(row=0,column=1)
f = Entry(gui).grid(row_=1,column=1)
c = ttk.Button(gui ,text="Cancel").grid(row=2,column=0)
d = ttk.Button(gui ,text="Login").grid(row=2,column=1)

g = Label(gui ,text="Sign Up", bg="#87CEEB").grid(row=2,column = 2)

gui.mainloop()