import tweepy
import api_token

client = tweepy.Client(bearer_token=api_token.BEARER_TOKEN)

users = client.get_users(usernames=['astratechz'])

for user in users:
    print(user)
