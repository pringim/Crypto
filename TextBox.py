from tkinter import *
import requests
import json
import os
import matplotlib.pyplot as plt

os.system('cls')
root = Tk()
root.iconbitmap("Python.ico")
root.title('Text Boxes')
root.geometry("600x500+345+100")

def clear():
    my_text.delete(1.0, END)
    my_label.config(text="")

def get_text():
    my_label.config(text=my_text.get(1.0, END))


my_text = Text(root, width=40, height=10, font=("Helvetica", 12))
my_text.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text="Clear Text", command=clear)
clear_button.grid(row=0, column=0)

get_text_button = Button(button_frame, text="Get Text", command=get_text)
get_text_button.grid(row=0, column=1, padx=10)

my_label = Label(root, text="")
my_label.pack(pady=20)

mainloop()