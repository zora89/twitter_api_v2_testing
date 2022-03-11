import tweepy
import api_token

client = tweepy.Client(bearer_token=api_token.BEARER_TOKEN)

query = 'india election  -is:retweet -#eximbank -btc -eth -nft -crypto -donation -donating -donate lang:en '
#case sensitive word check
repeated_word_check = "FOR"
versus_word = "SAYS"

count = 0
word_counter_1 = 0
word_counter_2 = 0
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=1000):
    count+=1
    print(count)
    unified_lowercase_tweet = tweet.text.lower()
    #enter the word you wish to count occurence of in each tweet !
    word_alert = unified_lowercase_tweet.count(repeated_word_check.lower())
    versus_word_alert = unified_lowercase_tweet.count(versus_word.lower())
    print(f" '--->>>{repeated_word_check}' repeated {word_alert} times")
    print(f" '--->>>{versus_word}' repeated {versus_word_alert} times")
    word_counter_1 += word_alert
    word_counter_2 += versus_word_alert
    print(tweet.text)
    print("\n")
    print("\n")

print(f"'{repeated_word_check.lower()}' count is {word_counter_1} \n'{versus_word.lower()}' count is {word_counter_2}")