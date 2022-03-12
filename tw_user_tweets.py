import tweepy
import api_token

client = tweepy.Client(bearer_token=api_token.BEARER_TOKEN)

tweets = client.get_users_tweets(id=api_token.atz_tw_id, tweet_fields=['created_at'], max_results=10)

count = 0
for tweet in tweets.data:
    count += 1
    print(tweet.id)
    print("------->>>>>>>>")
    print(tweet.text)
    print("------->>>>>>>>")
    print(tweet.created_at)
    print("---" + str(count) + "--->")

