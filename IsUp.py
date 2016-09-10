import requests
import os
import sys
from time import sleep
#import commands
from subprocess import call

    
if len(sys.argv)==2:

    url=sys.argv[1]
    while(1):
        res=requests.get(url)
        if res.status_code==requests.codes.ok:
            speech="Site is up"
            print(speech)
            call(["espeak",speech])
        else:
            print("Nope")
        sleep(5)
          
else:
    print("Enter correct number of arguments")
       
