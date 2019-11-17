# MÁSTER EN BIG DATA Y BUSINESS ANALYTICS
# MOD 1 - FINAL EVALUATION - EX. 2: dado un archivo que contiene en cada línea
# una palabra o conjunto de palabras seguido de un valor numérico denominado
# “sentimiento” y un conjunto de tweets, se pide calcular el sentimiento de
# aquellas palabras o conjunto de palabras que no tienen un valor asociado en el
# archivo de “sentimientos”. Se pueden seguir distintas estrategias para asignar
# un valor. Por ejemplo, se podría asignar como valor el valor del “sentimiento”
# del tweet en que se encuentra la palabra o conjunto de palabras sin valor, o
# el valor medio del “sentimiento” del tweet.

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
        print("Something went wrong parsing the file  " + filename)

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

# ---- MAIN PROGRAM -------------------------------------------------------------------------------------------------

# ---- Filenames (including path)
file_tweet = 'Tweets.txt'
file_sentimientos = 'Sentimientos.txt'


# -- PROCESS TWEETS FILE WITH PANDAS READ_JSON
list_of_tweets = get_tweets(file_tweet)

# -- PROCESS SENTIMIENTOS FILE TO A DICITIONARY
valores = get_sentiments(file_sentimientos)

# -- PROCESS TWEETS SENTIMENT AND PRINT
for tweet in list_of_tweets:
    tweet_sentimiento = 0
    words_without_sent = []
    number_of_words = 0
    for word in tweet.split(" "):
        tweet_sentimiento += valores.get(word.lower(),0)
        number_of_words += 1
        if valores.get(word.lower(),0)==0:
            words_without_sent.append(word)

    # asignar como valor el valor medio del “sentimiento” del tweet
    for item in words_without_sent:
        print(item + ': ' + str(tweet_sentimiento/number_of_words))
        print("\n")

print("--- THE END ---")
