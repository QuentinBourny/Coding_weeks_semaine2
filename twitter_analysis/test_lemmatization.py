from public.twitter_analysis.lemmatization import *

def test_lemmatisation():
    assert lemmatisation('I am the flights')=={'i','am','the','flight'}

def test_lem():
    assert lem(['I am the flights','you will be queries'])=={'flight','query'}
