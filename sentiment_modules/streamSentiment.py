'''
streamSentiment.py
21 Sep 2015 | Tonny and Vicki

Streams tweets according to filter labels and determines their sentiment value
'''

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

atoken = ""
asecret = ""
ckey = ""
csecret = ""


class listener(StreamListener):

	def on_data(self, data):
		try:
			all_data = json.loads(data)

			tweet = all_data["text"].lower()
			count = all_data["retweet_count"] + all_data["favorite_count"]
			sentiment_value, confidence = s.sentiment(tweet)
			print(tweet, sentiment_value, confidence)

			if confidence*100 >= 80 and ('ndp' in tweet or 'mulcair' in tweet):
				output = open("twitter-NDP.txt", "a")
				if count == 0:
					output.write(sentiment_value)
					output.write('\n')
				else:
					for x in xrange(count):
						output.write(sentiment_value)
						output.write('\n')
				output.close()

			if confidence*100 >= 80 and ('liberal' in tweet or 'trudeau' in tweet):
				output = open("twitter-liberal.txt", "a")
				if count == 0:
					output.write(sentiment_value)
					output.write('\n')
				else:
					for x in xrange(count):
						output.write(sentiment_value)
						output.write('\n')
				output.close()

			if confidence*100 >= 80 and ('conservative' in tweet or 'harper' in tweet):
				output = open("twitter-conservative.txt", "a")
				if count == 0:
					output.write(sentiment_value)
					output.write('\n')
				else:
					for x in xrange(count):
						output.write(sentiment_value)
						output.write('\n')
				output.close()

			return True

		except:
			return True


	def on_error(self, status):
		print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
while True:
	try:
		twitterStream.filter(track=['elxn42', 'cdnpoli', 'pledgetovote', 'harper', 'mulcair', 'trudeau'])
	except:
		continue