import  tweepy
import api_token

client = tweepy.Client(bearer_token=api_token.BEARER_TOKEN)

query = 'covid -is:retweet'

response = client.search_recent_tweets(query=query, max_results=10)

print(response)