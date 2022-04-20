import tkinter as tk
import Table
import Vocabulary


class View(tk.Frame):
    def __init__(self, parent):
        super(View, self).__init__(parent)
        self.__controller = None
        self.__table = Table.Table(Vocabulary.Vocabulary(), self)
        

    def set_controller(self, controller):
        self.__controller = controller
