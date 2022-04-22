import engine


class Vocabulary:
    def __init__(self):
        self.__vocabulary = {}
        self.__morphological_information = {}
        self.__do_filter = False
        self.__filter_settings = []

    def __del__(self):
        del self.__vocabulary
        del self.__morphological_information

    def add_lemma(self, lemma):
        self.__vocabulary[lemma] = {}

    def delete_lemma(self, lemma):
        del self.__vocabulary[lemma]

    def add_word_according_to_lemma(self, word, lemma):
        if lemma in self.__vocabulary:
            if word in self.__vocabulary[lemma]:
                self.__vocabulary[lemma][word] += 1
            else:
                self.__vocabulary[lemma][word] = 1
        else:
            self.__vocabulary[lemma] = {word: 1}
        self.add_morphological_information(word, ["", "", "", ""])

    def delete_word_according_to_lemma(self, word, lemma):
        if lemma in self.__vocabulary:
            del self.__vocabulary[lemma][word]

    def get_all_lemmas(self):
        lemmas = []
        for lem in sorted(self.__vocabulary.keys()):
            if len(self.get_all_words_according_to_lemma(lem)) > 0:
                lemmas.append(lem)
        return lemmas

    def get_all_words(self):
        words = []
        for value in self.__vocabulary.values():
            for word in value.keys():
                words.append(word)
        return words

    def get_all_words_according_to_lemma(self, lemma):
        words = []
        for value in self.__vocabulary[lemma].keys():
            if bool(self.__filter_word(value, lemma)):
                words.append(value)
        return words

    def __filter_word(self, word, lemma):
        if bool(self.__do_filter):
            info = self.get_morphological_info_according_to_word(word)
            count = int(self.get_count_of_word(word, lemma))
            f_count = self.__filter_settings[0]
            if f_count != "":
                f_count = int(f_count)
                if f_count != count:
                    return False
            if len(info) > 1:
                f_part_of_lang = self.__filter_settings[1]
                f_gen = self.__filter_settings[2]
                f_number = self.__filter_settings[3]
                f_padej = self.__filter_settings[4]
                if f_part_of_lang != "":
                    if f_part_of_lang != info[0]:
                        return False
                if f_gen != "":
                    if f_gen != info[1]:
                        return False
                if f_number != "":
                    if f_number != info[2]:
                        return False
                if f_padej != "":
                    if f_padej != info[3]:
                        return False
            else:
                if not bool(self.__filter_settings[5]):
                    return False
        else:
            return True
        return True

    def get_count_of_word(self, word, lemma):
        return self.__vocabulary[lemma][word]

    def set_count_of_word(self, word, count, lemma):
        self.__vocabulary[lemma][word] = count

    def add_morphological_information(self, word, information):
        self.__morphological_information[word] = list(information)

    def get_entire_vocabulary(self):
        return self.__vocabulary

    def get_entire_morphological_information(self):
        return self.__morphological_information

    def set_vocabulary(self, vocabulary):
        self.__vocabulary = dict(vocabulary)

    def set_morphological_information(self, information):
        self.__morphological_information = dict(information)

    def get_morphological_info_according_to_word(self, word):
        return self.__morphological_information.get(word, ["", "", "", ""])

    def size_of_vocabulary(self):
        return len(self.__vocabulary.items())

    def set_filter_settings(self, settings):
        self.__filter_settings = list(settings)

    def set_enable_filter(self, enable):
        self.__do_filter = bool(enable)
