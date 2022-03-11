import tweepy
import api_token

client = tweepy.Client(bearer_token=api_token.BEARER_TOKEN)

query = 'andaman  -is:retweet -#eximbank -btc -eth -nft -crypto -donation -donating -donate lang:en '
#case sensitive word check
word_check_1 = "airpoRT"
word_check_2 = "TOURISM"

count = 0
word_count_1 = 0
word_count_2 = 0
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=1000):
    count+=1
    print(count)
    unified_lowercase_tweet = tweet.text.lower()
    #enter the word you wish to count occurence of in each tweet !
    word_alert = unified_lowercase_tweet.count(word_check_1.lower())
    versus_word_alert = unified_lowercase_tweet.count(word_check_2.lower())
    print(f" '--->>>{word_check_1}' repeated {word_alert} times")
    print(f" '--->>>{word_check_2}' repeated {versus_word_alert} times")
    word_count_1 += word_alert
    word_count_2 += versus_word_alert
    print(tweet.text)
    print("\n")
    print("\n")

print(f"'{word_check_1.lower()}' count is {word_count_1} \n'{word_check_2.lower()}' count is {word_count_2}")