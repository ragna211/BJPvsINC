BATTLE @TWITTER #BJPvsINC

INTRODUCTION:
When the heat of elections is at its peak, what could be better than to see the battle of elections in real time. To see the battle, we’ll be using twitter as our tool. Accessing and judging tweets in real time could be helpful to predict the “KING” of the nation for next 5 years.

STEPS OF WORKING:
Authentication: To access twitter data, we need a twitter developer account. Twitter developer’s account provide us with 4 credentials which are necessary to get twitter data in real time and those credentials are:
	a.)Consumer Key
  b.)Consumer Secret
  c.)Access Token
  d.)Access Token
  Python’s Tweepy library was used for authentication.


Get Tweets: Once authenticated, now fetch the tweets with relevant query(BJP and congress in our case). Also, we mentioned the count of tweets, so that we don't get irrelevant tweets which may add noise to our analysis.

Cleaning: Now we did the cleaning process. These were the points that were kept in mind while cleaning:
Remove @User i.e. name of twitter handle
Remove punctuations
Remove digits
All this was done using regex.


Sentiment Analysis: We made a TextBlob object and passed he cleaned tweet into it. Then we used its sentiment analysis functionality. Textblob is the python library built on top of nltk. Its functionality includes rule based sentiment scores.Polarity ranges from [-1,1] where:
Polarity<0-NEGATIVE
           >0-POSITIVE
           =0-NEUTRAL

RESULTS:
Basis of deciding win:
We checked the percentage of positive tweets for the particular party among some top tweets.Whosoever has a higher share of positive tweets, won the battle. 
Results were so dynamic that even if we run the code after few minutes, we get different results. It was because we were fetching tweets in real time. For instance, we are adding a screenshot.
          
APPLICATIONS:
Not only for election, this model could be used to analyze many other trends. e.g.  ipl, fifa etc.
These trends could be used as a feedback system. e.g. customer feedback, working of government
 Forecast market movement based on news, blogs and social media sentiment

FUTURE USE:
From now, in any upcoming elections, you can track your performance with this project in real time. Extra features like:
Geolocation: To get the tweets from particular area
Until: To get the tweets till a particular date
could be embedded to get a more detailed analysis.



