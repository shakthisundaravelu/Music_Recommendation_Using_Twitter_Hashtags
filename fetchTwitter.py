import re
import sys
from tweepy import OAuthHandler
import tweepy

def text_clean(text):

    remove_space = '\s+'
    find_url = ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
        '[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    find_mention = '@[\w\-]+'
    process_text = re.sub(remove_space, ' ', text)
    process_text = re.sub(find_url, '', process_text)
    process_text = re.sub(find_mention, '', process_text)
    process_text = process_text.encode('ascii','ignore')
    return process_text.decode('utf-8')

con_key = 'PG2atN7eFZIfjqPugmrQ0DTHN'
con_secret = 'BcKjeAsjePUjw5SqOj7DqQy7QgTvNo6fbNXoT6PHoV68CwqWSX'
acc_token = '93137600-fD6r6VCcwx2f4ahKrqTlImxhFicNYcpy17HkL8Ne4'
acc_token_secret = 'lYUwaYoI6j5nHk7pijChJUxzDuY99osg64rs9vjhOejWU'

try:
            auth = OAuthHandler(con_key, con_secret)
            auth.set_access_token(acc_token, acc_token_secret)
            api = tweepy.API(auth)
            
except:
            
            print("Error: Twitter Not Connected")


# if len (sys.argv) != 2 :
#    print ("Usage: python fetchTweet.py  <search text>")
#    sys.exit (1)

def search_tweet(searchTxt):


    query = "#"+searchTxt
    count = 20
    tweets = []
    clean_tweets=[]
    try:
                fetched_tweets = api.search(q = query, count = count)

                for tweet in fetched_tweets:
                    parsed_tweet = {}
                    ss=tweet.text
                    parsed_tweet['text'] = ss#clean_tweet(ss)
                    clean_tweets.append(text_clean(ss))
                    tweets.append(parsed_tweet)

    except tweepy.TweepError as e:
           print("Error : " + str(e))

    print ("*********************************")
    print ("Total tweets read from twitter server ")
    print (len(tweets))
    return clean_tweets

# import pandas as pd
# df = pd.DataFrame(tweets)
# df.to_csv("tweets.csv")
#
# df = pd.DataFrame(clean_tweets)
# df.to_csv("clean_tweets.csv")
