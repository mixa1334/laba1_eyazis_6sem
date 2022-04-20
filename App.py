import tkinter as tk
import Vocabulary
import Controller
import View


class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("Laba 1")
        voc = Vocabulary.Vocabulary()
        view = View.View(self)
        view.pack()
        controller = Controller.Controller(voc, view)
        view.set_controller(controller)


if __name__ == "__main__":
    app = App()
    app.resizable(False, False)
    app.minsize(1350, 900)
    app.mainloop()
