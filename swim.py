from twython import Twython
import random
import time

APP_KEY = 'xKsStA4iezw65YaUvJxn4H55t'
APP_SECRET = 'yz3KVPnkV6PxudWDihhyEZbr3MT7Z6cffmpLwkF711cHKrwtBp'
ACCESS_TOKEN = '3399074332-Td7cuxbP70aiMZvSOOAIwiXjy94vwYwOTC3LRYj'
TOKEN_SECRET = 'XwxAq6yXAYAu3tzav1ea0dK0jRiG6R3fiIsIjpkecLsBj'

twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, TOKEN_SECRET)
last_count = 0

while(True):

	count = int(random.random() * 28) + 1
	
	if(count == last_count):
		count = count + 1
		
	last_count = count
	
	print(count)

	tweet = ""
	wing = "blub "
	wang = "swimmy "
	wong = "swim "
	
	while(count >= 0):
		rand = random.random()
		
		if(rand < 0.01):
			tweet += "nigga "
			count = count + 1
		
		elif(rand < 0.25):
			tweet += wing
			count = count - 1
			
		elif((rand > 0.25) and (rand < 0.75)):
			tweet += wong
			count = count - 1
			
		else:
			tweet += wang
			count = count - 2
			
		
	
	print(tweet)

	twitter.update_status(status=tweet)
	
	delay = int((random.random() * 3600) + 1800)
	
	print("Tweeting in:: " + str(delay/120))
	
	time.sleep(delay)
	



