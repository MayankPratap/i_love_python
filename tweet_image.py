import tweepy
from subprocess import call
from datetime import datetime

datetimeobj = datetime.now()               #take time and date for filename  
now = datetimeobj.strftime('%Y%m%d-%H%M%S')
photo_name = now + '.jpg'
cmd = 'raspistill -t 500 -w 500 -h 500 -o ' + photo_name
call ([cmd], shell=True)         #shoot the photo  

# Consumer keys and access tokens, used for OAuth  
consumer_key = '11ACG54PRfljrKDnqunLovhCt'
consumer_secret = 'sV5UVCUuRTnHDKJe2V6tF1qUAXVXH89CbAK8yEuvqS1N6iTI08'
access_token = '730706573132238848-g4cwsL6lSkQyKHzqBDoRQuTmz64j9z3'
access_token_secret = 'SPRRD0dPkyclY8QAxTRVIldHmLeDb2ZnkuQ4VrrutcpdY'

# OAuth process, using the keys and tokens  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication  
api = tweepy.API(auth)

# Send the tweet with photo  
photo_path = photo_name
status = 'I love Raspberry Pi : ' + datetimeobj.strftime('%Y/%m/%d %H:%M:%S')
api.update_with_media(photo_path, status=status)

