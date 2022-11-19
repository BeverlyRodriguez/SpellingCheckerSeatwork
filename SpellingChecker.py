import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Spelling Checker")
root.geometry("1000x700")
root.config(background="black")


heading =Label(root, text ="Check Spelling", font=("Helvetica", 30, "bold"), bg="#white", fg="#gray") 
heading.pack (pady=(50,0))

text = Entry(root, justify="center", width = 15, font=("poppins", 25), bg="blue", border=2)
text.pack(pady=10)
text.focus()
root.mainloop()
