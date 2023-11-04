from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(600,800)
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
button.config(padx=10,pady=10)
button.pack()


entry = Entry(width=20)
entry.focus()
entry.pack()

text = Text(width=20, height=10)
text.pack()

#scale
def scale_selected(value):
    print(value)
scale = Scale(from_=0, to=50,command=scale_selected)
scale.pack()

#spinbox
def spinbox_selected():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=50,command=spinbox_selected)
spinbox.pack()

#checkButton
def checkButton_selected():
    print(checkState.get())

checkState = IntVar()
checkButton = Checkbutton(text="Check",variable=checkState,command=checkButton_selected)
checkButton.pack()

#radioButton
def radioButton_selected():
    print(radioButtonCheckState.get())

radioButtonCheckState = IntVar()
radioButton1 = Radiobutton(text="1. Option",value=10,variable=radioButtonCheckState,command=radioButton_selected)
radioButton2 = Radiobutton(text="2. Option",value=20,variable=radioButtonCheckState,command=radioButton_selected)
radioButton1.pack()
radioButton2.pack()

#listbox
def listbox_selected(event):
    print(listbox.get(listbox.curselection()))
listbox = Listbox()
cityList = ["Ankara","İstanbul", "Ankara", "Muğla", "İzmir"]
for cityIdx in range(len(cityList)):
    listbox.insert(cityIdx,cityList[cityIdx])
listbox.bind("<<ListboxSelect>>",listbox_selected)
listbox.pack()





window.mainloop()