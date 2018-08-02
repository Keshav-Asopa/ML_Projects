# import libraries
import tweepy
import matplotlib.pyplot as plt
#analysis 
from textblob import TextBlob

#defining consumer key and secret
#making connection with twitter api
c_key = "xxxxxxxxxxxxxxxxxxxxxxxx"
c_sec = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

#token key and secret
#to search and get information you need to use token
t_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
t_sec = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

#connecting twitter API
auth_session = tweepy.OAuthHandler(c_key, c_sec)

#setting, sending token key and secret
auth_session.set_access_token(t_key, t_sec)

#now accessing API
api_connect = tweepy.API(auth_session)

#searching data
topic = api_connect.search('Modi')

for i in topic:
	#tokenized and clean
	blob_data = TextBlob(i.text)
	#applying sentiment output will be polarity
	print(blob_data.sentiment)

