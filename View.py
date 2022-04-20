import tkinter as tk
import Table
import Vocabulary


class View(tk.Frame):
    def __init__(self, parent):
        super(View, self).__init__(parent)
        self.__controller = None
        self.__table = Table.Table(self, Vocabulary.Vocabulary())
        self.__table.pack()

    def set_controller(self, controller):
        self.__controller = controller
