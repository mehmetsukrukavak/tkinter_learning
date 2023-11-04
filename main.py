import tkinter

window = tkinter.Tk()
window.title("Python Tkinter Example")
window.minsize(450, 300)


#label
myLabel = tkinter.Label(text="This is a Label",font=("Arial", 30, "bold"))
myLabel.config(bg="black",fg="white")
myLabel.pack()

#entry
myEntry = tkinter.Entry(width=20)
myEntry.pack()

#button
def click_button():
    print("Button clicked")
    userInput = myEntry.get()
    print(userInput)
myButton = tkinter.Button(text="This is a Button",command=click_button)
myButton.pack()

window.mainloop()