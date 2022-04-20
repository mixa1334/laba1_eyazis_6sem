from nltk.tokenize import word_tokenize
from pymystem3 import Mystem
from string import punctuation
import docx
import pickle

import vocabulary


def read_text_from_file(filename):
    doc = docx.Document(filename)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return "\n".join(text)


def write_vocabulary_to_file(voc, filename):
    with open(filename, "wb") as file:
        pickle.dump(voc, file)


def read_vocabulary_from_file(filename):
    with open(filename, "rb") as file:
        voc = pickle.load(file)
    return list(voc)


def preprocess_text(text):
    mystem = Mystem()
    text = text.lower()
    result = vocabulary.Vocabulary()
    words = list(filter(lambda val: val not in punctuation, word_tokenize(text)))
    lemmas = list(filter(lambda val: val != " " and val != "\n", mystem.lemmatize(" ".join(words))))

    for i in range(len(words)):
        result.add_word_according_to_lemma(words[i], lemmas[i])

    return result
