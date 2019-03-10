import tweepy
from textblob import TextBlob
import sys

# Authenticate
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

candidate = sys.argv[1]
def labels(analysis, threshold=0):
    if analysis.sentiment[0] > threshold:
        return 'positive'
    else:
        return 'negative'

tweets = api.search('candidate', count = 100)
with open('%s_tweets.csv'%candidate, 'w') as candidate_csv:
    candidate_csv.write('tweet, sentiment_label \n')
    for tweet in tweets:
        analysis = TextBlob(tweet.text)
        candidate_csv.write('%s %s\n' %(tweet.text, labels(analysis)))
