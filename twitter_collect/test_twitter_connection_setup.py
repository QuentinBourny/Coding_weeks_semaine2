from twitter_public.twitter_collect.twitter_connection_setup import *
from pytest import *

def test_twitter_setup():
          assert twitter_setup() is not None
