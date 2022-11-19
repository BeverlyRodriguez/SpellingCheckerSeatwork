import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Spelling Checker")
root.geometry("1000x700")
root.config(background="black")


def check():
    b = TextBlob(e.get())
    corrected_text = Label(root, text = str(b.correct()))
    corrected_text.pack()
    
root.mainloop()