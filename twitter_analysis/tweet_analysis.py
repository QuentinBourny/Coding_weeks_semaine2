import numpy as np

def max_de_likes(df):
    '''database en entrée, tweet avec le plus de like en sortie'''
    return np.max(df['likes'])


#print("The tweet with more likes is: \n{}".format(data['text'][likes]))
#print("Number of s: {}".format(likes))
#print("{} characters.\n".format(data['len'][likes]))

