from twitter_public.twitter_collect.data_tweet import *
from twitter_public.twitter_collect.tweet_collect import *
from twitter_public.twitter_analysis.tweet_analysis import *

data = transform_to_dataframe(collect())

def test_max_de_likes():
    assert max_de_likes(data)==np.max(data['likes'])
