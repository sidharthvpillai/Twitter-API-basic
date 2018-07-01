
# This is how to use  twitter API in collecting data from twitter 
#You have to first create developer account and thus you will get CONSUMER KEY,CONSUMER SECRET ,TOKEN AND OKEN SECRET 
import oauth2
import datetime
import json

CONSUMER_KEY = "Enter your consumer key here "
CONSUMER_SECRET = " Enter consumer secret here "
TOKEN = "Enter your token here"
TOKEN_SECRET = "enter your token secret here"
consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
token = oauth2.Token(key=TOKEN, secret=TOKEN_SECRET)
client = oauth2.Client(consumer, token)
query = "indian terrorism"   #there is a format for querying is given in query.txt
since = datetime.datetime.now() - datetime.timedelta(days=7) #last 7 days data are taken
d= since.date()
url = 'https://api.twitter.com/1.1/search/tweets.json?q=' + query+ '&since='+ str(d)
resp,content = client.request(url, method="GET", body="", headers= None)
data_set= json.loads(content)
for data in data_set["statuses"]:
	print "USER    : ", data["user"]["screen_name"]
	print "Retweet count    : ", data ["retweet_count"]
	print "favourite count    : ", data["favorite_count"]
	print "Message : ", data["text"]
#these are some of the fields in JSON produced by API 
#you can extend getting data by giving particuar fields .
#sample data from twitter API is given in sample.json