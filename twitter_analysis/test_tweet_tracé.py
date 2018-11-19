from twitter_public.twitter_analysis.tweet_tracé import *
from twitter_public.twitter_collect.data_tweet import *
from twitter_public.twitter_collect.tweet_collect import *


data = transform_to_dataframe(collect())

def test_tweet_trace_nb_de_likes_fonction_de_len():
    assert trace_nb_likes_fonction_de_len(data) is None
