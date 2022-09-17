from tkinter import *

root = Tk()
root.title("Simple Calculator")

input_area = Entry(root, width=40, borderwidth=3)
input_area.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# function for getting the clicks of each button
def button_click(number):
    current_number = input_area.get()
    input_area.delete(0, END)
    input_area.insert(0, str(current_number) + str(number))


# function for addition

def button_add():
    first_number = input_area.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    input_area.delete(0, END)


def button_subtract():
    first_number = input_area.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    input_area.delete(0, END)


def button_multiply():
    first_number = input_area.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    input_area.delete(0, END)


def button_divide():
    first_number = input_area.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    input_area.delete(0, END)


# function for equals
def button_equals():
    second_number = int(input_area.get())
    input_area.delete(0, END)
    if math == "addition":
        input_area.insert(0, f_num + second_number)
    elif math == "subtraction":
        input_area.insert(0, f_num - second_number)
    elif math == "multiplication":
        input_area.insert(0, f_num * second_number)
    elif math == "division":
        input_area.insert(0, f_num / second_number)


# function for clear
def button_clear():
    input_area.delete(0, END)


# creating buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_equals = Button(root, text="=", padx=91, pady=20, command=button_equals)

button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=41, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)

# displaying the buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equals.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
