
from tkinter import *


def addNumbers():
    res = str(e1.get()) + str(e2.get()) + str(e3.get())
    myText.set(res)


master = Tk()
myText = StringVar();
Label(master, text="Firstname").grid(row=0, sticky=W)
Label(master, text="Secondname ").grid(row=1, sticky=W)
Label(master, text="salary ").grid(row=2, sticky=W)

Label(master, text="bio:").grid(row=3, sticky=W)
result = Label(master, text="", textvariable=myText).grid(row=3, column=1, sticky=W)

e1 = Entry(master)
e2 = Entry(master)
e3=Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2,column=1)

b = Button(master, text="submit", command=addNumbers)
b.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)

mainloop()