import json
import sys, csv
import pandas as pd
path_tweet = 'D:/GitHub/master-bigdata/mod1-fundamentos_tratamiente-datos-ds/09-FinalEvaluation/Ex1/Tweets.json'
path_sentimientos = 'D:/GitHub/master-bigdata/mod1-fundamentos_tratamiente-datos-ds/09-FinalEvaluation/Ex1/Sentimientos.txt'


tweets = {}
counter= 0

def fetchTweetsFromFile(pathOfTweetFile):
    fields = []
    rows   = []

    with open(path_tweet, 'r') as file:
        csvreader = csv.reader(file, delimiter=',')
        next(csvreader)

        for row in csvreader:
                print('row: ' + str(row))
                rows.append(row)
        print ("Total no. of tweets: {}".format(csvreader.line_num-2))

        return rows

tweet_rows = fetchTweetsFromFile(path_tweet)

tweets = [row[4] for row in tweet_rows]
print(type(tweets))
print(str(tweets))

tweets
