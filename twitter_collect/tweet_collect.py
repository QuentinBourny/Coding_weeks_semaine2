from twitter_public.twitter_collect.twitter_connection_setup import *
connexion = twitter_setup()

def collect():
    tweets = connexion.search("Emmanuel Macron",language="french",rpp=10)
    return tweets


def collect_by_user(user_id):
    statuses = connexion.user_timeline(id = user_id, count = 200)
    for status in statuses:
        print(status.text)
    return statuses

#collect_by_user(3350900693)

# from tweepy.streaming import StreamListener
# class StdOutListener(StreamListener):
#
#     def on_data(self, data):
#         print(data)
#         return True
#
#     def on_error(self, status):
#         if  str(status) == "420":
#             print(status)
#             print("You exceed a limited number of attempts to connect to the streaming API")
#             return False
#         else:
#             return True
#
#
#
#
# def collect_by_streaming( filtre ):
#
#     listener = StdOutListener()
#     stream=tweepy.Stream(auth = connexion.auth, listener=listener)
#     stream.filter(track=[ filtre ])

#collect_by_streaming('Donald Trump')
