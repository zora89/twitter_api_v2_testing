import  tweepy
import api_token 

client = tweepy.Client(bearer_token=api_token.BEARER_TOKEN)

query = 'unicorn -is:retweet -#eximbank -btc -eth -nft -crypto -donation -donating -donate lang:en '

#checks for recent tweets
response = client.search_recent_tweets(query=query, 
            max_results=100, 
            tweet_fields=['created_at', 'lang'], 
            user_fields=['profile_image_url'], 
            expansions=['author_id'])


#checks for tweet count in 7 days on said query
counts = client.get_recent_tweets_count(query=query, granularity = 'day')
#needs to be UNDERSTOOD
users = {u['id']: u for u in response.includes['users']}

#case sensitive word check
word_check_1 = "india"
word_check_2 = "investor"


#returns information on recent tweets
count = 0
word_count_1 = 0
word_count_2 = 0


for tweet in response.data:
    if users[tweet.author_id]:
        lowercase_tweet = tweet.text.lower()
        word_1_alert = lowercase_tweet.count(word_check_1.lower())
        word_2_alert = lowercase_tweet.count(word_check_2.lower())
        #print(f" '--->>>{word_check_1}' repeated {word_1_alert} times")
        #print(f" '--->>>{word_check_2}' repeated {word_2_alert} times")
        word_count_1 += word_1_alert
        word_count_2 += word_2_alert
    
        user = users[tweet.author_id ]
        count += 1
        print("--")
        print(">>> INDEX: " + str(count))
        print (">>> TWEET ID: " + str(tweet.id))
        print(">>> USERNAME: " + user.username) 
        print(">>> TWEET: " + tweet.text)
        print(">>>LANG: " + tweet.lang)
        print(">>>CREATED_AT " + str(tweet.created_at))
        print(">>>PROFILE_IMAGE " + str(user.profile_image_url))
        print('--')
        print('\n')

print("<<<<<<<<------------ TWEET VOLUME IN PAST 7 DAYS")

#print(counts.data)

#returns count data on recent query search
for tweet in counts.data:
    print(tweet['tweet_count'])

print('\n')
print(f"'{word_check_1.lower()}' count is {word_count_1} \n'{word_check_2.lower()}' count is {word_count_2}")