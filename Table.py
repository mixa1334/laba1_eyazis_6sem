import tkinter as tk


class Table(tk.Frame):
    def __init__(self, voc, parent):
        super().__init__(parent)
        i = 1
        for lemma in voc.get_all_lemmas():
            self.__insert(i, 0, lemma)
            i += 1
            for word in voc.get_all_words_according_to_lemma():
                self.__insert(i, 0, word)
                self.__insert(i, 1, voc.get_count_of_word(lemma, word))
                self.__insert(i, 2, voc.get_morphological_info_according_to_word(word))
                i += 1

    def __insert(self, i, j, item):
        entry = tk.Entry(self, width=20, fg='gray', font=('Arial', 16, ''))
        entry.grid(row=i, column=j)
        entry.insert(tk.END, item)

    def __header(self):
        header_words = ["Слово", "Кол-во вхождения", "Морфологическая информация"]
        for j in range(3):
            entry = tk.Entry(self, width=20, bg='Black', fg='Black', font=('Arial', 16, 'bold'))
            entry.grid(row=0, column=j)
            entry.insert(tk.END, header_words[j])
