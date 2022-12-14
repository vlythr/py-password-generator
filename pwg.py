from poplib import LF
from tkinter import *
from random import randint

root = Tk()
root.title('Password Generator')
root.geometry("600x400")

my_password = chr(randint(33,126))

# Generate password Function

def new_rand():
    pw_entry.delete(0, END)
    pw_length = int(my_entry.get())

    my_password = ''

    for x in range(pw_length):
        my_password += chr(randint(33,126))

    pw_entry.insert(0, my_password)

# Copy to clipboard fuction

def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

# Label Frame
lf = LabelFrame(root, text="How many characters?", font=("Helvetica", 24), bd=0)
lf.pack(pady=20)

# Entry box to designate Number of Characters
my_entry =  Entry(lf, font=("Helvetica", 24), bd=0)
my_entry.pack(pady=20, padx=20)

# Entry box for Returned Password
pw_entry = Entry(root, text="", font=("Helvetica", 24), bd=0)
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