import tweepy
import api_token

client = tweepy.Client(bearer_token=api_token.BEARER_TOKEN)

#put userid @ here ->
users = client.get_users(usernames=['elonmusk'])

tweets = client.get_users_tweets(id=api_token.runa_tw_id, tweet_fields=['created_at'], max_results=100)

for user in users:
    print(user)

for tweet in tweets.data:
    print(tweet.id)
    print("------->>>>>>>>")
    #print(tweet.text)
    print("------->>>>>>>>")
    print(tweet.created_at)

