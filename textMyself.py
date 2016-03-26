""""
    
    This script uses twilio Module of Python to send myself text messages.
    
    I can use this script to send me a message if a download has finished or an automated process has finished a boring task.
    
    To use this script you have to register on twilio.com and select Programmable Messaging as option.
    
    Then you will get a Authentication SID,Token and a Twilio Phone Number which will send you text messages on number you select.
 
    If you want to use this code in any of your other scripts , you must place this script in same folder as your python executable.
    
    To find out where your python executable is :-
    
          import sys
          print sys.executable

    After placing this script in executable folder, you can use it in any other script as :-
    
     import textMyself
     
     textMyself.textmyself(message)
  


"""

#!python

# textMyself.py - Contains textmyself() function that texts a message

# passed to it as a string

sid="XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
token="XXXXXXXXXXXXXXXXXXXXXXXXXXXX"

myNumber="+XXXXXXXXXXXXX"
twilioNumber="+XXXXXXXXXXXX"

from twilio.rest import TwilioRestClient

def textmyself(message):
    twilioClient=TwilioRestClient(sid,token)
    twilioClient.messages.create(body=message,from_=twilioNumber,to=myNumber)
    
# textmyself("Hello There")  will send "Hello There" message on my mobile number     
