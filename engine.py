from pprint import pprint
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation
import docx
import pickle


def read_text_from_file(filename):
    doc = docx.Document(filename)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return "\n".join(text)


def write_vocabulary_to_file(voc, filename):
    with open(filename, "w") as file:
        pickle.dump(voc, file)


def read_vocabulary_from_file(filename):
    with open(filename, "r") as file:
        voc = pickle.load(file)
    return voc


def preprocess_text(text):
    mystem = Mystem()
    # russian_stopwords = stopwords.words("russian")
    text = text.lower()
    result = {}
    words = list(filter(lambda val: val not in punctuation, word_tokenize(text)))
    lemmas = list(filter(lambda val: val != " " and val != "\n", mystem.lemmatize(" ".join(words))))
    
    # for i in range(len(words)):
    #     # if word != " " and word.strip() not in punctuation:
    #     word = words[i]
    #     lemma = lemmas[i]
    #     if lemma in result:
    #         if word in result[lemma]:
    #             result[lemma][word] += 1
    #         else:
    #             result[lemma][word] = 1
    #     else:
    #         new_forms = {word: 1}
    #         result[lemma] = new_forms

    return result
