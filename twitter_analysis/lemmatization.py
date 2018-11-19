from textblob import TextBlob
from textblob import Word
import pandas as pd
import nltk
from nltk.corpus import stopwords


stop_words = set(stopwords.words('english'))

def lemmatisation(text):
    '''d'un texte en string renvoie l'ensmeble des mots lemmatisés en minuscules'''
    sentence=TextBlob(text).lower()
    return set([sentence.words[k].lemmatize() for k in range(len(sentence.words))])

def lem(liste_tweets):
    '''d'une liste de tweets qui sont des str, on renvoie l'ensemble des mots utilisés, privé de l'ensemble des stop-words'''
    nv_set=set()
    for tweet in liste_tweets:
        nv_set=nv_set.union(lemmatisation(tweet))
    return nv_set.difference(stop_words)
