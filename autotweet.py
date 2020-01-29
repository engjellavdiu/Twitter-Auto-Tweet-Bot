import tweepy
import time
from datetime import datetime

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    auth = tweepy.OAuthHandler("pCJIZm0jEKyIFPRRLTSz2jfy7","7ZQONhZ3CNG1Msy99jbVEQSuQWETR8aY94TsvunLX95osPRQYk")
    auth.set_access_token("1354422482-RKb4j1j8alMJ2yBee5B4ZDG2kt0FupL2Z7NmTEN", "1TtxQ6NAh5DPTG9Hns5xwrWsHPQ52KIV6vb0W7rh1WvZ2")
    api = tweepy.API(auth)
    tweet = ("Qa bone ti "+current_time)
    api.update_status(status =(tweet))
    print ("Done!")
    time.sleep(10800)