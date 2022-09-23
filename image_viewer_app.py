# import packages/Modules
from tkinter import *
from PIL import ImageTk, Image

# Creating tkinter widget window
root = Tk()

# MAKING THE SIZE FIXED
root.resizable(False, False)

# creating a title for the app
root.title('Image viewer App')

# defining the pictures to the program
my_img1 = ImageTk.PhotoImage(Image.open("Images/animals.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("Images/jungle.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Images/animals.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("Images/jungle.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("Images/zebra.jpg"))

# making a list for the different images
_my_img_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# inserting the image into a label function
my_label = Label(image=my_img1)

# displaying the image on the program widow
my_label.grid(row=0, column=0, columnspan=3)


# Creating the functions for the forward buttons
def forward_btn(image_number):
    global my_label
    global button_forward
    global button_backward
    global status
    my_label.grid_forget()
    my_label = Label(image=_my_img_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward_btn(image_number + 1))
    button_backward = Button(root, text="<<", command=lambda: backward_btn(image_number - 1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_backward.grid(row=1, column=0)

    # Update the Image_counter
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(_my_img_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


# Creating the functions for the backward buttons
def backward_btn(image_number):
    global my_label
    global button_forward
    global button_backward
    global status
    my_label.grid_forget()
    my_label = Label(image=_my_img_list[image_number - 1])

    button_forward = Button(root, text=">>", command=lambda: forward_btn(image_number + 1))
    button_backward = Button(root, text="<<", command=lambda: backward_btn(image_number - 1))

    if image_number == 1:
        button_backward = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_backward.grid(row=1, column=0)

    # Update the Image_counter
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(_my_img_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


# defining the buttons
button_backward = Button(root, text="<<", command=backward_btn)
quit_button = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward_btn(2))

# displaying the buttons
button_backward.grid(row=1, column=0)
quit_button.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

#  updated the Image_counter
# I updated the Image_counter here again to make the Image_counter display on the app even without clicking the
# forward and backwards buttons

status = Label(root, text="Image 1 of " + str(len(_my_img_list)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

# making the tkinter program run
root.mainloop()
