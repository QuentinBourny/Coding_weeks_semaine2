import matplotlib.pyplot as plt
import pandas as pd

def trace_nb_likes_fonction_de_len(data):
    long_likes=pd.Series(data=data['likes'].values, index=data['len'])
    plt.plot(long_likes)
    #plt.show()
