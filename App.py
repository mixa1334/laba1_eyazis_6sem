import tkinter as tk
import Vocabulary
import Controller
import View


class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()

        self.title("Laba 1")
        voc = Vocabulary.Vocabulary()
