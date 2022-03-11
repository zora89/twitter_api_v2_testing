import  tweepy
import api_token 

client = tweepy.Client(bearer_token=api_token.BEARER_TOKEN)

query = 'andaman "and" bjp -is:retweet'

#checks for recent tweets
response = client.search_recent_tweets(query=query, max_results=10, tweet_fields=['created_at', 'lang'], user_fields=['profile_image_url'], expansions=['author_id'] )
#checks for count on of tweets in past week on said query
counts = client.get_recent_tweets_count(query=query, granularity = 'day')
#needs to be UNDERSTOOD
users = {u['id']: u for u in response.includes['users']}


#returns information on recent tweets
count = 0
for tweet in response.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id ]
        count += 1
        print("--")
        print(str(count))
        #print (str(tweet.id))
        print("------->>>>>>>>")
        print("BODY: " + tweet.text)
        print("------->>>>>>>>")
        print("LANG: " + tweet.lang)
        print("CREATED AT: " + str(tweet.created_at))
        print("USERNAME: " + user.username)
        print(user.profile_image_url)
print("<<<<<<<<------------ TWEET VOLUME IN PAST 7 DAYS")
#print(counts.data)

#returns count data on recent query search
for tweet in counts.data:
    print(tweet['tweet_count'])