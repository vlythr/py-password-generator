from poplib import LF
from tkinter import *
from random import randint

root = Tk()
root.title('Password Generator')
root.geometry("500x300")

my_password = chr(randint(33,126))

def new_rand():
    pass

def clipper():
    pass

# Label Frame
lf = LabelFrame(root, text="How many characters?")
lf.pack(pady=20)

# Entry box to designate Number of Characters
my_entry =  Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

# Entry box for Returned Password
pw_entry = Entry(root, text="", font=("Helvetica", 24))
pw_entry.pack(pady=20)

# Frame for the buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# Buttons
my_button = Button(my_frame, text="Generate Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy to Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)




root.mainloop()