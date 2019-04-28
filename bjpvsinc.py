# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 11:23:32 2019

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 07:46:24 2019

@author: HP
"""

import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 

class TwitterClient(object): 
  
   def __init__(self): 
      
      consumer_key = 'qFr4nEXlDN6Hb7FrVfcwSBkrU'
      consumer_secret = 'Tdt8Uej3pgUTbwVS74KyzDz54uzwS3NiiH0qv3xcl2WBPnPO07'
      access_token = '1120505850466988032-aDgEl2bTl6DkEG1gMa8LaqbyHJnA0k'
      access_token_secret = 'mF9IeMrAQwL1vtnZOrgzbYpImfj8hn7P2Nv6PFISMoT9g'

      try: 
         self.auth = OAuthHandler(consumer_key, consumer_secret) 
         self.auth.set_access_token(access_token, access_token_secret) 
         self.api = tweepy.API(self.auth) 
      except: 
         print("Error: Authentication Failed") 

   def clean_tweet(self, tweet): 
      a=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 
      #print("a",a)
      return a
  
    
   def get_tweet_sentiment(self, tweet): 
      analysis = TextBlob(self.clean_tweet(tweet)) 
      if analysis.sentiment.polarity > 0: 
         return 'positive'
      elif analysis.sentiment.polarity == 0: 
         return 'neutral'
      else: 
         return 'negative'

   def get_tweets(self, query, count = 10): 
      tweets = [] 

      try: 
         fetched_tweets = self.api.search(q = query, count = count) 
         for tweet in fetched_tweets: 
            parsed_tweet = {} 
            parsed_tweet['text'] = tweet.text 
            parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 
            if tweet.retweet_count > 0: 
               if parsed_tweet not in tweets: 
                  tweets.append(parsed_tweet) 
            else: 
               tweets.append(parsed_tweet) 

         return tweets 

      except tweepy.TweepError as e: 
         print("Error : " + str(e)) 

def main(): 
   api = TwitterClient() 
   btweets = api.get_tweets(query = 'BJP OR Bhartiya Janta Party', count = 200) 
   bptweets = [tweet for tweet in btweets if tweet['sentiment'] == 'positive'] 
   print(btweets)
   bp=100*len(bptweets)/len(btweets)
   print("BJP's Positive tweets percentage: {} %".format(100*len(bptweets)/len(btweets))) 
   bntweets = [tweet for tweet in btweets if tweet['sentiment'] == 'negative'] 
   ctweets = api.get_tweets(query = 'Congress OR INC OR Indian National Congress', count = 200) 
   cptweets = [tweet for tweet in btweets if tweet['sentiment'] == 'positive'] 
   cp=100*len(cptweets)/len(ctweets)
   print("Congress's Positive tweets percentage: {} %".format(100*len(cptweets)/len(ctweets))) 
   cntweets = [tweet for tweet in ctweets if tweet['sentiment'] == 'negative']
   
   print("BATTLE RESULTS")
   print("BJP's favor",bp/(bp+cp))
   
   print("Congress's favor",cp/(cp+bp))
      
if __name__ == "__main__": 
   # calling main function 
   main()