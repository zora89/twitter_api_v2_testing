import tweepy
import api_token

client = tweepy.Client(consumer_key=api_token.CONSUMER_KEY,
                       consumer_secret=api_token.CONSUMER_SECRET,
                       access_token=api_token.ACCESS_KEY,
                       access_token_secret=api_token.ACCESS_SECRET)

# Replace the text with whatever you want to Tweet about
response = client.create_tweet(text='hello world')

print(response)