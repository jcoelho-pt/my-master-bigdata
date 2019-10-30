import json
import pandas as pd
path_tweet = 'D:/GitHub/master-bigdata/mod1-fundamentos_tratamiente-datos-ds/09-FinalEvaluation/Ex1/Tweets.json'
path_sentimientos = 'D:/GitHub/master-bigdata/mod1-fundamentos_tratamiente-datos-ds/09-FinalEvaluation/Ex1/Sentimientos.txt'


# ---- PROCESS TWEETS FILE TO PANDAS -------------------------------------------
tweets = {}

pd_tweets = pd.read_json(path_tweet, lines=True)    # use parameter lines=True to not
pd_tweets['text']

pd_tweets_filtered = pd_tweets[pd_tweets.text.notnull()]['text']
pd_tweets_filtered


# ---- PROCESS SENTIMIENTOS FILE TO A DICITIONARY ------------------------------
valores = {}
for linea in open(path_sentimientos, 'r'):
     termino, valor = linea.split('\t')
     valores[termino] = int(valor)
print(valores.items())

pd_valores = pd.DataFrame.from_dict(valores, orient='index', columns=['Valores'])
pd_valores
