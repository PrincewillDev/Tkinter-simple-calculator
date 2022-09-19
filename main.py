from tkinter import *

root = Tk()

input_field = Entry(root, width=50)
input_field.pack()


def my_click():
    my_label = Label(root, text=input_field.get())
    my_label.pack()


my_button = Button(root, text="Enter your name", command=my_click, fg="red")
my_button.pack()

root.mainloop()
