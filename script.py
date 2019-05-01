import tweepy
from textblob import TextBlob
import sys

# Authenticate
consumer_key= 'consumer_key'
consumer_secret= 'consumer_secret'

access_token= 'access_token'
access_token_secret= 'access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

candidate = sys.argv[1]
def labels(analysis, threshold=0):
    if analysis.sentiment[0] > threshold:
        return 'positive'
    else:
        return 'negative'

neg_count = 0
pos_count = 0

tweets = api.search('candidate',count=100)

for tweet in tweets:
    analysis = TextBlob(tweet.text)
    if labels(analysis) == 'positive':
        pos_count += 1
    elif labels(analysis) == 'negative':
        neg_count += 1

total = pos_count + neg_count
pos_per = (pos_count/total)*100
neg_per = (neg_count/total)*100

print('percentage of positive tweets: %.2f' %pos_per)
print('percentage of negative tweets: %.2f' %neg_per)
