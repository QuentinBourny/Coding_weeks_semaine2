import pandas as pd

def transform_to_dataframe(tweets):
    '''à partir d'un fichier tweets renvoie la dataframe avec : id,texte,date, longueur de texte, likes, nombre de RT'''
    df=pd.DataFrame({'id':[tweet.id for tweet in tweets],'text':[tweet.text for tweet in tweets],'date':[str(tweet.created_at) for tweet in tweets],'len':[len(tweet.text) for tweet in tweets],'likes':[tweet.favorite_count for tweet in tweets],'RTs':[tweet.retweet_count for tweet in tweets]})
    return df

