# python ghraphical user interfaces

# Tkinter
from tkinter import *

window = Tk() # this is how we can create a window but it wont show up
window.title("My First GUI Program")
window.minsize(width=500, height=300)
#===================================================================
# label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack() # what allows the label to show up on the screen
#===================================================================
# ho we can update labels
my_label["text"] = "New Text"
my_label.config(text="New Texts")
#===================================================================
# Buttons
def button_clicked():
    my_label["text"] = input.get()
button = Button(text="Click Me", command=button_clicked)
# button.pack()
#===================================================================
# Entry
input = Entry(width=10)
# input.pack()
input.get() # returns the input as string
#===================================================================
# See other py file for examples of other widgets and how they are used
#===================================================================

# we have Pack, Place and Grid
# pack just adds them one after the other

# Place is for precise positioning, inciate the x and the y value
input = Entry(width=10)
input.place(x=0,y=0) # gets very speficic

# Grid cn divide into any number of rows and columns
input = Entry(width=10)
input.grid(column=0,row=1)
# wont show until you place the rest
input = Entry(width=10)
input.grid(column=1,row=1)


# can add padding to things by saying .config(padx = , pady = )

window.mainloop() # this is what keeps our window on the screen, this will be at the bttom of the code





#============================================================================================================================
# # How to make a funciton take multiple argumetns

# def add(*args): # args is a tuple 
#     # print(sum(args)) # this works as well but wanted to show you can iterate thorugh the arguments
#     # nums[0] wopuld be the order they are presented
#     count = 0
#     for n in args:
#         count += n
#     print(count)

# add(1,2,3,4,5,6,7,8,9)
# add(1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17)
# add(1,2,3)

# # how to pass multiple key word arguments 
# def calculate(**kwargs): # kwargs is a dictionary
#     print(kwargs["multiply"] , kwargs["adds"])

# calculate(adds = 3, multiply = 5)

# class Car:
#     def __init__(self, **kw):
#         self.make = kw["make"] # doing it this way means you must incklude it or else this will cause a key error as it is a dictionary
#         self.model = kw.get("model") # useing kw get, we can return none if upon object creation a kw isnt passed 