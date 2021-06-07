import tweepy
import sys
import json


#Sab se pehle ham authentication ke liye keys ko define krengy
#ye keys hamen twitter ne provide ki hen wo yahan insert krengy neechy
# ye keys secret hoti hen so ksi ke sath sahre na kijieyga

api_key= "api key yahan insert kren"
api_secret_key = ""
access_key =""
access_secret =""

# ab ham authenticate krengy apna connection with twitter developer platform  with the help of the keys

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#jo keyword ki tweet chahye wo ham user ke through lengy ya define krengy variable mein
#mene yahan "python" keyword ki tweets search krne k liye kiya h

query = 'python'
max_tweets = 1
searched_tweets = [status for status in tweepy.Cursor(api.user_timeline, q=query).items(max_tweets)]
print(searched_tweets)