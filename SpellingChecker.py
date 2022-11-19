import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#E6E6FA")

def spellCheck():
    word = text.get()
    txt = TextBlob(word)
    RightText = str(txt.correct())

    CorrectText = Label(root, text = "CORRECT SPELLING: ", font=("poppins", 20, "bold"), bg="#CDC1C5", fg="black")
    CorrectText.place(x=100, y=250)
    spell.config(text=RightText)

heading =Label(root, text ="Check Spelling", font=("Helvetica", 30, "bold"), fg="#333333") 
heading.pack (pady=(50,0))

text = Entry(root, justify="center", width = 15, font=("poppins", 25), bg="#FFF0F5", border=2)
text.pack(pady=10)
text.focus()

button = Button(root, text="CHECK", width=15, font=("arial", 20, "bold"), fg="#FAEBD7", bg="#8B8386", command=spellCheck)
button.pack()

spell = Label(root, font=("poppins", 20), bg="#FFF0F5", fg="#CDC9A5")
spell.place(x=350, y=250)

root.mainloop()
