# Import necessary libraries
import tweepy
import pandas as pd
import csv
import time
import random
from datetime import date, timedelta, datetime
import datetime
from pandas import DataFrame
pd.options.mode.chained_assignment = None  # default='warn' # to disable SettingWithCopyWarning

# Access the credentials file and store all keys and tokens in different variables
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

# getting the authenticated user's information
user = api.verify_credentials()

# printing the name of the user
print("The authenticated user's name is : " + user.name)
print("The authenticated user's location is : " + str(user.location))
print("\n")

# the username of the targeted user
# username = "ChirpNews"

# store tweets in csv files
# 3 different csv files for 3 different accounts

# for i in range(1, 10):
#     api.update_status(i)

presentDay = date.today()
print("Today's date is : " + str(presentDay))

tomorrow = presentDay + timedelta(1)
print("Tomorrow's date is : " + str(tomorrow))
yesterday = presentDay + timedelta(0)
print("Yesterday's date is : " + str(yesterday))

# the username of the targeted account whose tweets are to be retrieved
username = "ANI"
user = api.get_user(screen_name=username)
followerCount = user.followers_count
print(username + " has " + str(followerCount) + " followers on Twitter \n")

# Open/create a file to append data to
csvFile = open('ani.csv', 'a')

# Use csv writer
csvWriter = csv.writer(csvFile)
# To delete previous contents of the file
csvFile.truncate(0)

start_date = datetime.datetime(2022, 11, 27, 00, 00, 00)
end_date = datetime.datetime(2022, 11, 26, 00, 00, 00)

for tweet in tweepy.Cursor(api.user_timeline,
                           screen_name=username,
                           # since=start_date,
                           # until=end_date,
                           # lang="en",
                           ).items(750):
    # print("ID TWEET: " + str(tweet.text))
    # Write a row to the CSV file. Use UTF=8 encoding
    engagementRate = (tweet.retweet_count + tweet.favorite_count) / 100

    csvWriter.writerow([tweet.created_at.date(), tweet.text.encode('utf-8'),
                        "https://twitter.com/" + username + "/status/" + str(tweet.id),
                        tweet.retweet_count, tweet.favorite_count, engagementRate])
    print(tweet.created_at.date(), tweet.text, "https://twitter.com/" + username + "/status/" + str(tweet.id),
          tweet.retweet_count, tweet.favorite_count, engagementRate)
csvFile.close()

# assign header columns
# also add tweet link
headerList = ["Created At", "Tweet", "TweetLink", "RetweetCount", "LikeCount", "EngagementRate"]
colNames = ["Created At", "Tweet", "TweetLink", "RetweetCount", "LikeCount", "EngagementRate"]

# read contents of csv file
# file = pd.read_csv("ani.csv")
# Assigning Column names to CSV file
file = pd.read_csv("ani.csv", names=colNames, header=None)
# print(file)

# converting data frame to csv
# Assigning header names to be visible in the CSV file
file.to_csv("ani.csv", header=headerList, index=False)

print("\n")
for col in file.columns:
    print(col)

# Getting Tweets of 1 day window
dateDf = file.groupby("Created At")
todayDf = dateDf.get_group("2022-12-19")

# Sorting the CSV for highest engagement rates
# sort data frame
todayDf.sort_values(by='EngagementRate',
                    ascending=False,
                    inplace=True)
# file.sort_values('EngagementRate',
#                  axis=0,
#                  ascending=False,
#                  inplace=True,
#                  na_position='first')
# file.sort_values(file.columns[5])
# file.sort_values(by='EngagementRate',
#                  # axis=1,
#                  ascending=False,
#                  inplace=True)
# kind="mergesort")
# print(file)

# for items in file:
#     for i in range(5):
#         # api.update_status(file['TweetLink'])
#         print(file['TweetLink'])
# print(file.head(5))
# print(file['TweetLink'].head(5))
# api.update_status(file['TweetLink'].head(5))

# Creating a list of the top 5 tweets of the CSV file
tweetLinks = todayDf['TweetLink'].tolist()
# print(tweetLinks)
for i in range(5):
    print(tweetLinks[i])
    api.update_status(tweetLinks[i])
