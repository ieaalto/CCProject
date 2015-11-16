from gensim.models.word2vec import *
from nltk.corpus import brown
from os.path import isfile

def create_model(sentences = None, filepath=None, save=True, savename="model.txt"):
    if sentences:
        model = Word2Vec(sentences)
    elif filepath:
        model = Word2Vec.load(filepath)
    else:
        raise ValueError("No corpus defined!")

    if save:
        model.save(savename)

    model.init_sims(replace=True)
    return model

def create_model_from_NLTK():
    filepath = "nltkcorpus.txt"
    if isfile(filepath):
        return create_model(filepath= filepath, save=False)

    return create_model(sentences=brown.sents(), savename=filepath)

