import tweepy
import api_token

client = tweepy.Client(bearer_token=api_token.BEARER_TOKEN)

query = 'ukraine victory  -is:retweet -#eximbank -btc -eth -nft -crypto -donation -donating -donate lang:en '
#case sensitive word check
repeated_word_check = "Putin"


count = 0
word_alert_count = 0
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=1000):
    count+=1
    print(count)
    #enter the word you wish to count occurence of in each tweet !
    word_alert = tweet.text.count(repeated_word_check)
    print(f" '{repeated_word_check}' repeated {word_alert} times")
    word_alert_count += word_alert
    print(tweet.text)
    print("\n")
    print("\n")

print(word_alert_count)