from tkinter import *

window = Tk() # this is how we can create a window but it wont show up
window.title("My First GUI Program")
window.minsize(width=300, height=100)
window.config(padx=50, pady=20)
window.title("Miles to Km Converter")

# grid should be a 3 x 3

def convert():
    miles = float(input.get())
    km = 1.60934 * miles
    number.config(text="{}".format(km))


text1 = Label(text="is equal to")
text1.grid(column=0,row=1)

miles = Label(text="Miles")
miles.grid(column=2,row=0)

input = Entry(width=10)
input.grid(column=1,row=0)


km = Label(text="Km")
km.grid(column=2,row=1)

number = Label(text="0")
number.grid(column=1,row=1)

button = Button(text="Calculate", command= convert)
button.grid(column=1, row=2)



window.mainloop()