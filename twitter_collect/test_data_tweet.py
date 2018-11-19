from twitter_public.twitter_collect.tweet_collect import *
from twitter_public.twitter_collect.data_tweet import *
from pytest import *


def test_collect():
    tweets = collect()
    data =  transform_to_dataframe(tweets)
    assert 'text' in data.columns
