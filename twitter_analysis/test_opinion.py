from public.twitter_analysis.opinion import *


def test_sentiments():
    sentiment=sentiments(['Un joueur partant chasser est vraiment très doué','Tu es nul', 'Tu es bon','rien','Ca devrait suffire'])
    assert sentiment[0]+sentiment[1]+sentiment[2]==1
