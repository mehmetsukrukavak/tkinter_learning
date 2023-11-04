import tkinter

window = tkinter.Tk()
window.title("Python Tkinter Example")
window.minsize(450, 300)

window.update()
screen_y = window.winfo_height()
screen_x = window.winfo_width()
#label
myLabel = tkinter.Label(text="This is a Label",font=("Arial", 30, "bold"))
myLabel.config(bg="black",fg="white")
#myLabel.pack()
#myLabel.place(x=0,y=0)
myLabel.grid(row=0,column=0)

#entry
myEntry = tkinter.Entry(width=20)
#myEntry.pack()
#myEntry.place( x=100,y=50)
myEntry.grid(row=0,column=3)
#button
def click_button():
    print("Button clicked")
    userInput = myEntry.get()
    print(userInput)
myButton = tkinter.Button(text="This is a Button",command=click_button)
#myButton.place(x=screen_x / 2 -65,y=screen_y / 2 -14)
#myButton.update()
#print(myButton.winfo_width())
#print(myButton.winfo_height())
myButton.grid(row=1,column=2)

#myButton.pack()

window.mainloop()