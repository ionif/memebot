from collections import deque
import tweepy, time, sys, os
 
CONSUMER_KEY = '####'
CONSUMER_SECRET = '####'
ACCESS_KEY = '####'
ACCESS_SECRET = '###'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

queue = deque([])
directory = "filepath/memes/"

for filename in os.listdir(directory):
	if filename.endswith(".PNG") or filename.endswith(".JPG") or filename.endswith(".GIF"): 
		print(os.path.join(directory, filename))
		queue.append(os.path.join(directory, filename))
        	continue

def update():
	meme = queue.popleft()
	api.update_with_media(meme, status="")

start_time = time.time()
while True:
	print "tick"
	update()
	#posts every 2 hours
	time.sleep(43200.0 - ((time.time() - start_time) % 43200.0))

