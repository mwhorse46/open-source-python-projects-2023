from os import access
from pydoc import describe
import tweepy
import requests
import json

api_key = "your api key"
api_key_secret = "your secret key"
access_token ="your access key"
access_token_secret ="your token secret"

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

data = requests.get('https://zenquotes.io/api/quotes/')
data = json.loads(data.text)
quote = data[0].get('q')
author = data[0].get('a')
description = quote + "\n" + " - " + author
print(description)
print("Bio Updated")
api.update_profile(description=description)