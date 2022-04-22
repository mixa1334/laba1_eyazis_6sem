import tkinter as tk
from tkinter import ttk


class Table:
    def __init__(self, parent, voc):
        header_words = ["Слово", "Кол-во вхождения", "Морфологическая информация"]
        table = ttk.Treeview(parent, show="headings")
        table['columns'] = header_words

        for head in header_words:
            table.heading(head, text=head, anchor='center')
            if head != header_words[0]:
                table.column(head, anchor='center')

        for lemma in voc.get_all_lemmas():
            l_row = (lemma, "", "")
            table.insert('', tk.END, values=l_row)
            for word in voc.get_all_words_according_to_lemma(lemma):
                morph_info = voc.get_morphological_info_according_to_word(word)
                w_row = (
                    word, voc.get_count_of_word(word, lemma), str(morph_info[0]) + " " + str(morph_info[1]) + " " +
                    str(morph_info[2]) + " " + str(morph_info[3]) + " ")
                table.insert('', tk.END, values=w_row)

        scroll_pane = ttk.Scrollbar(parent, command=table.yview)
        table.configure(yscrollcommand=scroll_pane.set)
        scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)
        self.__table = table
