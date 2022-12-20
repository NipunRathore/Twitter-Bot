# import necessary libraries
import tweepy
import time
import random
import datetime
from datetime import date

# Access the credentials file and store all keys and tokens in different variables
# Assign the values correctly
all_keys = open('credentials', 'r').read().splitlines()
api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# Testing credentials authentication
try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")

# WOEID of Ghaziabad
# woeid = 44418
woeid = 23424848
# Worldwide trends
# woeid = 1
# fetching the trends
trends = api.get_place_trends(id=woeid)

# printing the information
print("The top trends for India are :")
tweetTrend = "The top trends for India today are : \n "
for value in trends:
    for trend in value['trends']:
        print(trend['name'])
        # api.update_status(trend['name'])
        tweetTrend += "\n"
        tweetTrend += str(trend['name'])

print("\n")
print(tweetTrend)

# Finding total length of string of trends created
tweetLength = len(tweetTrend)
print("Length is : " + str(tweetLength))

# Reducing tweet length to 280 characters because Twitter allows to post only 280 characters at once
# Limit tweet length by removing excess trailing characters
final = tweetTrend[:280]
print("Final length of the tweet is " + str(len(final)))
# Removing 280 leading characters
final2 = tweetTrend[280:]
# print(len(final2))

final3 = final2[:280]
# print(len(final3))

today = date.today()
api.update_status("Today's date is : " + str(today))
tweet1 = api.update_status(status=final)
# tweet2 = api.update_status(status=final3, in_reply_to_status_id=tweet1.id)
