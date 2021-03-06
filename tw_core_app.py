import tweepy
import api_token

#setting the client, query and response always first.
client = tweepy.Client(bearer_token=api_token.BEARER_TOKEN)
query = 'agnipath -is:retweet -#eximbank -btc -eth -nft -crypto -donation -donating -donate lang:en '
response = tweepy.Paginator(
        client.search_recent_tweets, query=query, max_results=100, 
        tweet_fields=['created_at', 'lang'], 
        user_fields=['profile_image_url'], 
        expansions=['author_id']).flatten(limit=100
        )

counts = client.get_recent_tweets_count(query=query, granularity = 'day')

#case sensitive word check
word_check_1 = "support"
word_check_2 = "against"

#setting counters for ease of data relay
count = 0
word_count_1 = 0
word_count_2 = 0

for tweet in response:        
    count+=1
    print(count)
    lowercase_tweet = tweet.text.lower()
    #enter the word you wish to count occurence of in each tweet !
    word_1_alert = lowercase_tweet.count(word_check_1.lower())
    word_2_alert = lowercase_tweet.count(word_check_2.lower())
    print(f" '--->>>{word_check_1}' repeated {word_1_alert} times")
    print(f" '--->>>{word_check_2}' repeated {word_2_alert} times")
    word_count_1 += word_1_alert
    word_count_2 += word_2_alert
    print(tweet.text)
    print(tweet.author_id)
    print("\n")
    print("\n")

print(f"Tweet Research Query: {query}")
print("")
print(f"Total Tweets Scanned {count}")
print("")
print(f"Scanner 1 Detected'{word_check_1.lower()}' count is {word_count_1} \nScanner 2 Detected'{word_check_2.lower()}' count is {word_count_2}")
print("")
print("<<<<<<<<------------ TWEET VOLUME IN PAST 7 DAYS")
for tweet in counts.data:
    print("Tweet Volume", tweet['tweet_count'])