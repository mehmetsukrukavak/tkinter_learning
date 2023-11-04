from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(600,600)
window.config(padx=10,pady=10)

label = Label(text="Widget Label")
label.config(bg="black")
label.config(bg="white")
label.config(padx=15,pady=20)
label.pack()

def button_clicked():
    print(text.get("1.0",END))
    #1.0 -> 1: line, 0: character
    print("clicked")

button = Button(text= "Press", command=button_clicked)
button.config(padx=30,pady=30)
button.pack()


entry = Entry(width=20)
entry.focus()
entry.pack()

text = Text(width=30, height=20)
text.pack()





window.mainloop()