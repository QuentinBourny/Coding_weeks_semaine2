from twitter_public.twitter_collect.tweet_collect import *
from pytest import *

def test_collect():
    assert collect() is not None

def test_coleect_by_user():
    assert collect_by_user(3350900693) is not None

