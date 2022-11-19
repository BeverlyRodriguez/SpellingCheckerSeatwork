import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Spelling Checker")
root.geometry("1000x700")
root.config(background="black")


heading =Label(root, text ="Check Spelling", font=("Helvetica", 30, "bold"), bg="#white", fg="#gray") 

root.mainloop()
