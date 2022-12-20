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
print("\n")

# Retrieve usernames of all the recent followers
# the username of the targeted user
username = "ChirpNews"

# toFollow = "varsha98rathore"
# api.create_friendship(screen_name=toFollow)
# api.update_status("Hello, World! - Test")

# Follow back all the followers
print("\n")
print(" ~ Starting follow back process ~ ")
following = tweepy.Cursor(api.get_friends, screen_name=username)
followers = tweepy.Cursor(api.get_followers, screen_name=username)
for follower in followers.items():
    if follower in following.items():
        print("Already followed: " + follower.screen_name)
    else:
        # follower.follow()
        api.create_friendship(screen_name=follower)
        print("Followed Back: " + follower.screen_name)

# Unfollow those who don't follow back anymore
print("\n")
print(" ~ Starting unfollow process ~ ")
for friend in following.items():
    if friend not in followers.items():
        # friend.destroy_friendship()
        api.destroy_friendship(screen_name=friend)
        print("Destroyed friendship with: " + friend.screen_name)
    else:
        print("Still a friend with: " + friend.screen_name)
        # pass

# for follower in tweepy.Cursor(api.get_followers).items():
#     follower.follow()
#     print("Followed Back " + follower.screen_name)
