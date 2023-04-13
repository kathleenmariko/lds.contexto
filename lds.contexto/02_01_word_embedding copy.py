import glob
import spacy
from gensim.models import Word2Vec

nlp = spacy.load("en_core_web_sm")

def pre_processing():
  '''this function converts the text of each general conference talk into tokenized and lemmetized sentences'''
  all_sents = []
  for file in glob.glob("/Users/kathleenbrown/Documents/portfolio/lds.contexto/plain_text_files/*.txt"):
    file_name = file
    with open(file_name, "r") as h:
        doc = nlp(h.read())
    sents = [[tok.lemma_ for tok in sent] for sent in doc.sents]
    sents_lower = [[tok.lower() for tok in sent] for sent in sents]
    all_sents.extend(sents_lower)
  return all_sents

def word_embedding(all_sents):
  '''this function processes the word vectors and stores them in 'word2vec.model' which is found in the main directory'''
  model = Word2Vec(sentences=all_sents, vector_size=100, window=5, min_count=1, workers=4)
  model.save("word2vec.model")
  return model 

all_sents = pre_processing()
model = word_embedding(all_sents)