import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#C1C1FF")

def spellCheck():
    word = text.get()
    txt = TextBlob(word)
    RightText = str(txt.correct())

    CorrectText = Label(root, text = "Correct Spelling: ", font=("poppins", 20, "bold"), bg="#C1C1FF", fg="#000000")
    CorrectText.place(x=80, y=250)
    spell.config(text=RightText)

heading =Label(root, text ="Check Spelling", font=("Helvetica", 30, "bold"), bg="#C1C1FF", fg="#2F2F4F") 
heading.pack (pady=(50,0))

text = Entry(root, justify="center", width = 15, font=("poppins", 25), bg="#FFF0F5", border=3)
text.pack(pady=10)
text.focus()

button = Button(root, text="CHECK", width=15, font=("arial", 20, "bold"), fg="#FAEBD7", bg="#000000", command=spellCheck)
button.pack()

spell = Label(root, font=("poppins", 20, "bold"), bg="#FFF0F5", fg="#2F2F4F", border=2)
spell.place(x=350, y=250)

root.mainloop()
