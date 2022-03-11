import tweepy
import api_token

client = tweepy.Client(bearer_token=api_token.BEARER_TOKEN)

#put userid @ here ->
users = client.get_users(usernames=['zorawarpurohit'])

for user in users:
    print(user)


