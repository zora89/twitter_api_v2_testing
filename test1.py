import  tweepy
import api_token

client = tweepy.Client(bearer_token=api_token.BEARER_TOKEN)

query = 'paytm "and" india -is:retweet'

response = client.search_recent_tweets(query=query, max_results=10, tweet_fields=['created_at', 'lang'], user_fields=['profile_image_url'], expansions=['author_id'] )


users = {u['id']: u for u in response.includes['users']}

count = 0
for tweet in response.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id ]
        count += 1
        print("--")
        print(str(count))
        print (str(tweet.id))
        print("------->>>>>>>>")
        print(tweet.text)
        print("------->>>>>>>>")
        print(tweet.lang)
        print(str(tweet.created_at))
        print(user.username)
        print(user.profile_image_url)