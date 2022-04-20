import tkinter as tk


def fun():
    global myEntyr1
    text = "hello -> " + myEntyr1.get()
    myEntyr1.delete(0, tk.END)
    tk.Label(root, text=text).grid(row=4, column=1)
    # myEntyr1.grid_forget()

# main window
root = tk.Tk()

myLabel1 = tk.Label(root, text="Hello dude")
myLabel2 = tk.Label(root, text="wtf dude iam not dude")

# place on the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=2)

myButton = tk.Button(root, text="Click me!!!!", padx=50, pady=50, command=lambda: fun(), fg="blue", bg="gray")
myButton.grid(row=3, column=0, columnspan=3)
myButton2 = tk.Button(root, text="Exit but", command=root.quit, bg="gray", fg="red")
myButton2.grid(row=5, column=0, columnspan=3)

myEntyr1 = tk.Entry(root, width=50, fg="blue", bg="gray", borderwidth=10, state=tk.DISABLED)
myEntyr1.insert(0, "type u name")
myEntyr1.grid(row=2, column=1)

# event loop
root.mainloop()
