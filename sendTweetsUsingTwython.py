from twython import Twython

APP_KEY='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
APP_SECRET='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCESS_TOKEN='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCESS_TOKEN_SECRET='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Creating twittter object using Twython

twitter = Twython(APP_KEY,APP_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

# Updating status using update_status attribute of twitter object

twitter.update_status(status='Now I will undergo Beta testing')
