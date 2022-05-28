from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Collection')
root.configure(bd=6)
root.iconbitmap('../icon_png/computer.ico')

# images
image1 = Image.open('../../icon_png/a1.png')
image2 = Image.open('../../icon_png/a2.png')
image3 = Image.open('../../icon_png/a3.png')
image4 = Image.open('../../icon_png/n1.png')
image5 = Image.open('../../icon_png/n2.png')
image6 = Image.open('../../icon_png/n3.png')

# resizing images
image1 = image1.resize((320, 500))
image2 = image2.resize((320, 500))
image3 = image3.resize((320, 500))
image4 = image4.resize((320, 500))
image5 = image5.resize((320, 500))
image6 = image6.resize((320, 500))

# using the ImageTk.PhotoImage library
img1 = ImageTk.PhotoImage(image1)
img2 = ImageTk.PhotoImage(image2)
img3 = ImageTk.PhotoImage(image3)
img4 = ImageTk.PhotoImage(image4)
img5 = ImageTk.PhotoImage(image5)
img6 = ImageTk.PhotoImage(image6)


# listing images
img_list = [img1, img2, img3, img4, img5, img6]


# putting images into label widget
lbl = Label(image=img1)
lbl.grid(row=0, column=0, columnspan=3)

# status menu
status = Label(root, text='Image 1 of ' + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)

# functions
def forward(image_number):
   global lbl
   global button_forward
   global button_back
   lbl.grid_forget()    # image should disappear when we click the forward button 1st time.
   lbl = Label(image=img_list[image_number - 1])    # then, this prints the next image.
   button_forward = Button(root, text='>>', width=6, bd=5, command=lambda: forward(image_number + 1))
   button_back = Button(root, text='<<', width=6, bd=5, command=lambda: back(image_number - 1))

   if image_number == 6:
       button_forward = Button(root, text='>>', width=6, bd=5, state=DISABLED)

   lbl.grid(row=0, column=0, columnspan=3)  # puts lbl on the screen
   button_back.grid(row=1, column=0)
   button_forward.grid(row=1, column=2)

   # setting the status to dynamic change
   status = Label(root, text='Image ' + str(image_number) + ' of ' + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
   status.grid(row=2, column=0, columnspan=3, pady=7, sticky=W + E)

def back(image_number):
    global lbl
    global button_forward
    global button_back
    #lbl.grid_forget()  # image should disappear when we click the forward button 1st time.
    lbl = Label(image=img_list[image_number - 1])  # then, this prints the next image.
    button_back = Button(root, text='<<', width=6, bd=5, command=lambda: back(image_number - 1))
    button_forward = Button(root, text='>>', width=6, bd=5, command=lambda: forward(image_number + 1))

    if image_number == 1:
        button_back = Button(root, text='<<', width=6, bd=5, state=DISABLED)

    lbl.grid(row=0, column=0, columnspan=3)  # puts lbl on the screen
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # setting the status to dynamic change
    status = Label(root, text='Image ' + str(image_number) + ' of ' + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, pady=7, sticky=W + E)

# buttons
button_forward = Button(root, text='>>', width=6, bd=5, command=lambda: forward(2)).grid(row=1, column=2)
button_exit = Button(root, text='Exit', command=root.quit, bd=5).grid(row=1, column=1)
button_back = Button(root, text='<<', width=6, bd=5, state=DISABLED, command=back).grid(row=1, column=0)
status.grid(row=2, column=0, columnspan=3, pady=7, sticky=W+E)

root.mainloop()