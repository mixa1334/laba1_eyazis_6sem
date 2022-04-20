class Vocabulary:
    def __init__(self):
        self.__vocabulary = {}
        self.__morphological_information = {}

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

    def delete_word_according_to_lemma(self, word, lemma):
        if lemma in self.__vocabulary:
            del self.__vocabulary[lemma][word]

    def get_all_lemmas(self):
        return self.__vocabulary.keys()

    def get_all_words(self):
        words = []
        for value in self.__vocabulary.values():
            for word in value.keys():
                words.append(word)
        return words

    def get_all_words_according_to_lemma(self, lemma):
        words = []
        for value in self.__vocabulary[lemma]:
            for word in value:
                words.append(word)
        return words

    def get_count_of_word(self, word, lemma):
        return self.__vocabulary[lemma][word]

    def add_morphological_information(self, word, information):
        self.__morphological_information[word] = list(information)

    def edit_morphological_information(self, word, information):
        self.add_morphological_information(word, information)

    def get_entire_vocabulary(self):
        return self.__vocabulary

    def get_entire_morphological_information(self):
        return self.__morphological_information

    def set_vocabulary(self, vocabulary):
        self.__vocabulary = dict(vocabulary)

    def set_morphological_information(self, information):
        self.__morphological_information = dict(information)
