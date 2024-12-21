import tkinter

from regex import W

# Create the main window
window = tkinter.Tk()
window.geometry("800x600")

window.title("My First GUI Program")
window.minsize(400, 200)

#Components
mylabel = tkinter.Label(window, text="Welcome to my first GUI program", font=("Courier New", 20), justify="left")
mylabel.pack()

window.mainloop()