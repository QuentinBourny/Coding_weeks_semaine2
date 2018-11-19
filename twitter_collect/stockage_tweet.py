import json

def store_tweet(tweets,filename):
    '''écrit les tweets dans le dossier twitter_collector avec le nom filename.json'''
    liste=[]
    for tweet in tweets:
        liste.append({'id':tweet.id,'text':tweet.text,'user_id':tweet.user.id,'date':str(tweet.created_at)})
        #[{id du tweet,texte du tweet,date du tweet}], nous n'arrivons pas à récupérer les hashtags
    with open(filename+".json", "w") as write_file: #écrit la liste de dico dans un json : filename.json
        json.dump(liste, write_file)



