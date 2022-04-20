import tkinter as tk


class View(tk.Frame):
    def __init__(self, parent):
        super(View, self).__init__(parent)
        self.__controller = None

    def set_controller(self, controller):
        self.__controller = controller
