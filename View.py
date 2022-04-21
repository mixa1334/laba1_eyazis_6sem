import tkinter as tk
import Table
import Vocabulary
from tkinter import filedialog
import re
from tkinter import messagebox


class View(tk.Tk):
    def __init__(self):
        super(View, self).__init__()
        self.title("Laba 1")
        self.geometry("800x400")
        self.maxsize(1920, 1080)
        self.minsize(800, 400)
        self.__controller = None

        menu_frame = tk.Frame(self)
        open_button = tk.Button(menu_frame, text="open", command=self.__command_open)
        open_button.grid(row=0, column=0)
        save_button = tk.Button(menu_frame, text="save", command=self.__command_save)
        save_button.grid(row=0, column=1)
        create_empty_voc = tk.Button(menu_frame, text="create empty", command=self.__command_create_empty)
        create_empty_voc.grid(row=0, column=2)
        create_from_doc = tk.Button(menu_frame, text="create from doc", command=self.__command_create_from_doc)
        create_from_doc.grid(row=0, column=3)
        menu_frame.place(relx=0, rely=0, relwidth=1, relheight=0.5)
        self.__menu_frame = menu_frame
        self.__content_frame = None
        self.__set_content_table(Vocabulary.Vocabulary())

    def __set_content_table(self, voc):
        if self.__content_frame:
            del self.__content_frame
        content_frame = tk.Frame(self)
        self.__table = Table.Table(content_frame, voc)
        content_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)
        self.__content_frame = content_frame

    def __command_open(self):
        filename = filedialog.askopenfilename(title="select a file to open", filetypes=[("pkl files", ".pkl")])
        if filename and self.__controller:
            voc = self.__controller.open_vocabulary(filename)
            self.__set_content_table(voc)

    def __command_save(self):
        top = tk.Toplevel()
        top.title("Save as file")
        label = tk.Label(top, text="Type file name")
        entry = tk.Entry(top)
        button = tk.Button(top, text="Save", command=lambda: self.__prosecc_save_button(top, entry))
        label.grid(row=0, column=0, padx=10, pady=10)
        entry.grid(row=0, column=1, padx=10, pady=10)
        button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def __prosecc_save_button(self, window, entry):
        fname = entry.get()
        window.destroy()
        regex = re.compile('[a-zA-Z]+', re.I)
        match = regex.match(str(fname))
        if bool(match):
            self.__controller.save_vocabulary(fname)
            messagebox.showinfo("Save to file", "Success!")
        else:
            messagebox.showerror("Save to file", "Incorrect filename")

    def __command_create_empty(self):
        if self.__controller:
            voc = self.__controller.create_empty()
            self.__set_content_table(voc)

    def __command_create_from_doc(self):
        filename = filedialog.askopenfilename(title="select a file to open",
                                              filetypes=[("docx files", ".docx"), ("doc files", ".doc")])
        if filename and self.__controller:
            voc = self.__controller.create_from_doc(filename)
            self.__set_content_table(voc)

    def set_controller(self, controller):
        self.__controller = controller
