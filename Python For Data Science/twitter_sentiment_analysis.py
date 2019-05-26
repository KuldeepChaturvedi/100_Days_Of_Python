# Python script to generate csv file which contains tweet and its polartiy with subjectivity and objectivity of tweet.
import tweepy
from textblob import TextBlob
import csv
import datetime

consumer_key = None
consumer_secert_key = None
access_token = None
access_token_secret = None
topic = None
while(consumer_key == None or consumer_key == ''):
    consumer_key = input('Enter the consumer Key = ')
while(consumer_secert_key == None or consumer_secert_key == ''):
    consumer_secert_key = input('Enter the consumer secert Key = ')
while(access_token == None or access_token == ''):
    access_token = input('Enter access token = ')
while(access_token_secret == None or access_token_secret == ''):
    access_token_secret = input('Enter access token secret = ')

print('--------------------'*4)
print('Please wait Authenticating....')
auth = tweepy.OAuthHandler(consumer_key,consumer_secert_key)
print('--------------------'*4)
print('Please wait setting access token....')
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

while(topic == None or topic == ''):
    topic = input('Please enter keyword to search = ')
print('--------------------'*4)
print('Fetching twittes......')
public_tweets = api.search(q=topic,count=100)

csvData = [['Tweet','Polarity','Subjectivity','Subective / Objective']]
for tweet in public_tweets:
    tweet_text = tweet.text
    analysis = TextBlob(tweet.text)
    polarity_score = analysis.sentiment.polarity
    subjectivity_score = analysis.sentiment.subjectivity
    subjective_or_objective = None
    if subjectivity_score > 0.5:
        if subjectivity_score == 1.0:
            subjective_or_objective = 'Very Subjective'
        else:
            subjective_or_objective = 'Subjective'
    if subjectivity_score < 0.5:
        if subjectivity_score == 0.0:
            subjective_or_objective = 'Very Objective'
        else:
            subjective_or_objective = 'Objective'
    csvData.append([tweet.text,polarity_score,subjectivity_score,subjective_or_objective])

current_date_time  = datetime.datetime.now().strftime('%d%m%y_%H%M%S')

filename = topic + '_' + str(current_date_time) + '.csv'
print('--------------------'*4)
print('Creating File ' + filename)
print('Writing in file ' + filename)
with open(filename, 'w', encoding='utf-8') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
print(filename + ' created successfully.')

csvFile.close()