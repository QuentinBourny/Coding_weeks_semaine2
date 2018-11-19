from twitter_public.twitter_collect.stockage_tweet import *
from twitter_public.twitter_collect.tweet_collect import *
from pytest import *
tweets = collect()
store_tweet(tweets,"Emmanuel_Macron")

def test_store_tweet():
    with open("Emmanuel_Macron.json", 'r') as readfile :
        assert readfile is not None
