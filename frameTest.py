import tkinter as tk
from tkinter import messagebox

root = tk.Tk()


def popupmsg():
    response = messagebox.askyesno("Oops", "smth went wrong, do u want to exit?")
    if response:
        global root
        root.quit()


root.title("Hello")

frame = tk.LabelFrame(root, text="frame", padx=50, pady=50)
frame.grid(padx=100, pady=10)

b = tk.Button(frame, text="Click me")
b2 = tk.Button(frame, text="Dont click me))))", padx=100, command=popupmsg)
b.grid(row=0, column=0, padx=100)
b2.grid(row=1, column=1)

root.mainloop()
