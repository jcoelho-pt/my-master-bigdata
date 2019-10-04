import json

path_tweet = 'D:/GitHub/master-bigdata/mod1-fundamentos_tratamiente-datos-ds/09-FinalEvaluation/Ex1/Tweets.txt'
path_sentimientos = 'D:/GitHub/master-bigdata/mod1-fundamentos_tratamiente-datos-ds/09-FinalEvaluation/Ex1/Sentimientos.txt'


valores = {}
for linea in open(path_sentimientos, 'r'):
    termino, valor = linea.split('\t')
    valores[termino] = int(valor)
print(valores.items())
