# MÁSTER EN BIG DATA Y BUSINESS ANALYTICS
# MOD 1 - FINAL EVALUATION - EX. 1: dado un archivo que contiene en cada línea
# una palabra o conjunto de palabras seguido de un valor numérico, denominado
# “sentimiento”, y un conjunto de tweets, se pide calcular para cada tweet un
# valor denominado “sentimiento del tweet”, que se obtiene como la suma de los
# “sentimientos” de los términos que aparecen en el tweet.

import json
import pandas as pd

# ---- FUNCTIONS ---------------------------------------------------------------
def get_tweets(filename):
    """ Process a json formatted file with tweets using pandas read_json """
    try:
        tweets = []
        pd_tweets = pd.read_json(filename, lines=True)    # use parameter lines=True to read the file as a json object per line
        pd_tweets = pd_tweets[pd_tweets.text.notnull()]['text']
        tweets = pd_tweets.to_list()
        return tweets
    except:
        print("Something went wrong parsing the file " + filename)

def get_sentiments(filename):
    """ Process a file that contains in each line a word or
        set of words followed by a numerical value, called "feeling
        - returns a dictionary with pairs of words and sentiments
    """
    valores = {}
    for linea in open(filename, 'r'):
         termino, valor = linea.split('\t')
         valores[termino] = int(valor)
    return valores


# -- FILES & VARIABLES
file_tweet = 'Tweets.txt'
file_sentimientos = 'Sentimientos.txt'


# -- MAIN PROGRAM -------------------------------------------------------------

# -- process tweets file using pandas read_json
list_of_tweets = get_tweets(file_tweet)

# -- process sentimientos file
valores = get_sentiments(file_sentimientos)

# ---- process tweets sentiments
for tweet in list_of_tweets:
    tweet_sentimiento = 0
    for word in tweet.split(" "):
        tweet_sentimiento += valores.get(word.lower(),0)
    print("EL SIGUIENTE TWEET: '" + tweet + "' TIENE UN SENTIMIENTO ASOCIADO DE: " + str(tweet_sentimiento))
    print("\n")
