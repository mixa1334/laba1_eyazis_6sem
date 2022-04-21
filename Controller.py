import Vocabulary
import engine


class Controller:
    def __init__(self, voc, view):
        self.__voc = voc
        self.__view = view

    def save_vocabulary(self, filename):
        l = [self.__voc.get_entire_vocabulary(), self.__voc.get_entire_morphological_information()]
        engine.write_vocabulary_to_file(l, filename)

    def open_vocabulary(self, filename):
        l = engine.read_vocabulary_from_file(filename)
        self.__voc = Vocabulary.Vocabulary()
        self.__voc.set_vocabulary(l[0])
        self.__voc.set_morphological_information(l[1])
        return self.__voc

    def create_empty(self):
        self.__voc = Vocabulary.Vocabulary()
        return self.__voc

    def create_from_doc(self, filename):
        text = engine.read_text_from_file(filename)
        self.__voc = engine.preprocess_text(text)
        return self.__voc
