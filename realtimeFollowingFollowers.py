# Import necessary libraries
import tweepy
import time
import random

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

# Retrieve usernames of all the recent followers
# the username of the targeted user
username = "ChirpNews"

# Total count of all followers
c = tweepy.Cursor(api.get_followers, screen_name=username)

count = 0
for follower in c.items():
    count += 1
print(username + " has " + str(count) + " followers.")

# printing the latest 20 followers of the user
# for follower in api.get_followers(screen_name=username):
#     print(follower.screen_name)
num = 20
# print("\n")
for follower in tweepy.Cursor(api.get_followers, screen_name=username).items(num):
    print(follower.screen_name)

# Print the users the bot is following
# Ordered in which they were added
# friends() method is used to get user's friends (users they are following)
# for friend in api.get_friends(screen_name=username):
#     print(friend.screen_name)
num = 30
print("\n")
for friend in tweepy.Cursor(api.get_friends, screen_name=username).items(num):
    print(friend.screen_name)

# Total count of all the friends / following
# getting all the friends
c = tweepy.Cursor(api.get_friends, screen_name=username)

# counting the number of friends
count = 0
for friends in c.items():
    count += 1

print(username + " has " + str(count) + " friends.")
# api.update_status("12-11-2022 12:59PM")
