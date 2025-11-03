from tkinter import *


window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)

my_label = Label(text="I AM A LABEL", font=("Arial",24, "bold"))
my_label.pack()

my_label["text"] = "New Text"

my_label.config(text="New Text")
input = Entry(width=10)
input.pack()
# Button

def button_click():
    print("I got clicked!")
    my_label.config(text=input.get())




button = Button(text="Click Me1", command=button_click)
button.pack()


window.mainloop()

# def asf(*args):
#     for _ in args:
#         print(_)
#
# def calculate(**kwargs):
#     # print(type(kwargs))
#     for key, value in kwargs.items():
#         print(key, value)


# asf(3,4,5,6)

# calculate(add=3, multiply=5)

# def test(*args):
#     print(args)
#
# print(type(test(1,2,3,4)))

# def all_aboard(a, *args, **kw):
#     print(a, args, kw)
#
#
# all_aboard(4, 7, 3, 0, x=10, y=64)