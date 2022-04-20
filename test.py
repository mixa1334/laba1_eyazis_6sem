import vocabulary
import engine
import pprint


def proc_and_save():
    text = engine.read_text_from_file("test.docx")
    voc = engine.preprocess_text(text)
    pprint.pprint(voc.get_entire_vocabulary())
    engine.write_vocabulary_to_file([voc.get_entire_vocabulary(), voc.get_entire_morphological_information()],
                                    "info.pkl")


def from_f():
    l = engine.read_vocabulary_from_file("info.pkl")
    voc = vocabulary.Vocabulary()
    voc.set_vocabulary(l[0])
    voc.set_morphological_information(l[1])
    return voc


pprint.pprint(from_f().get_entire_vocabulary())
