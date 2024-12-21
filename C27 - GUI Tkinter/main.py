import tkinter

from regex import W

# Create the main window
window = tkinter.Tk()
window.geometry("800x600")

window.title("My First GUI Program")
window.minsize(400, 200)

#Components
mylabel = tkinter.Label(window, text="Welcome to my first GUI program", font=("Courier New", 20), justify="left")
mylabel.grid(row=0, column=0)
#mylabel.place(x=0,y=0)

#button
button = tkinter.Button(window, text="Click me!", font=("Courier New", 20), command=lambda: print("Button clicked"))
button.grid(row=1, column=0)
#button.pack()

def button_click():
    print("Button 2 clicked")
    mylabel.config(text=input.get())

button2 = tkinter.Button(window, text="Click me2!", font=("Courier New", 20), command=button_click)
button2.grid(row=1, column=1)
#button2.pack()

#Entry
input = tkinter.Entry(window, width=10, font=("Courier New", 20))
input.grid(row=2, column=0)
#input.pack()

window.mainloop()