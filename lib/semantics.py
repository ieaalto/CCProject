from gensim.models.word2vec import *
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
    else:
        from nltk.corpus import reuters, brown, gutenberg
        sents = reuters.sents() + brown.sents()
        for gsents in [gutenberg.sents(fid) for fid in gutenberg.fileids()]:
            sents += gsents

        return create_model(sentences=sents, savename=filepath)


