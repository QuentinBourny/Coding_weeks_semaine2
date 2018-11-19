from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

def sentiments(liste_tweets):
    '''d'une liste de tweets EN FRANCAIS(str) renvoie une liste de sentiments pour les différents tweets'''
    nb_positive_tweets=0
    nb_negative_tweets=0
    nb_neutral_tweets=0
    for tweet in liste_tweets :
        blob=tb(tweet)
        sentiment=blob.sentiment[0]
        if sentiment>0:
            nb_positive_tweets+=1
        elif sentiment==0:
            nb_neutral_tweets+=1
        else :
            nb_negative_tweets+=1
    n=len(liste_tweets)
    return nb_positive_tweets/n,nb_neutral_tweets/n,nb_negative_tweets/n
