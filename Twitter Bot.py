import tweepy
import time
from datetime import datetime
#from pytz import timezone (an option)

while True:
    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    auth = tweepy.OAuthHandler("OAuthHandler","OAuthHandler") #Info from Twitter API
    auth.set_access_token("AccessToken", "AccessToken") #Info from Twitter API
    api = tweepy.API(auth)
    tweet = (" Text "+currentTime)
    api.update_status(status =(tweet))
    print ("Done!")
    time.sleep(30) #Time for next Tweet (in seconds)