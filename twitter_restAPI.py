import tweepy 
import codecs # have to encode text before writing to file 
import re # regular expressions 
import string 
from collections import Counter

# tonny's credentials
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# finding time zone
# print tweet._json['user']['time_zone']

def tweet_data(keywords):
	f = codecs.open("tweet.txt",'w','utf-8')
	for word in keywords:
		public_tweets = api.search(q = word,count = 1500)
		for tweet in public_tweets:
			# get rid of urls
			tweet.text = re.sub('\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet.text, flags=re.MULTILINE)
			#f.write("user: " + tweet.user.screen_name + " text: " + tweet.text + " time: " + str(tweet.created_at) + ",\n" )
			f.write(tweet.text + ",\n")
	f.close()

# to be called after tweet_data
def countFrequency():
	table = string.maketrans("","")
	f = open("tweet.txt","r")
	c = Counter()
	for line in f:
		line.translate(table, string.punctuation)
		c = Counter(line.split())
		print c['NDP']

