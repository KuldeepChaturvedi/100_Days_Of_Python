import tweepy
from textblob import TextBlob
import csv

consumer_key = 'kqyT3fp8fTt3JC2dwnVuVze8J'
consumer_secert_key = 'jLzLV2vliLYfqJu29yllG2axSdDaYujeIAMvoBe0heWxhibhsH'

access_token = '404176458-EcOc10GVeQjkyPDW6xHZJG9e1Q9o1cYugBuxH3Mz'
access_token_secret = 'f3ilUWddcQV27Q5NAZ7qSkiGg4Vq8WOvoalVDLYzZmMb7'

auth = tweepy.OAuthHandler(consumer_key,consumer_secert_key)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('RedmiNote7Pro')

csvData = [['Tweet','Polarity','Subjectivity']]

for tweet in public_tweets:
    print('-------------'*4)
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print('------------- Sentiment Polarity -------------')
    print(analysis.sentiment.polarity)
    print('------------- Sentiment Subjectivity -------------')
    print(analysis.sentiment.subjectivity)
    csvData.append([tweet.text,"{:.2f}".format(analysis.sentiment.polarity),"{:.2f}".format(analysis.sentiment.subjectivity)])


with open('twitter.csv', 'w', encoding='utf-8') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()