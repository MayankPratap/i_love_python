"""
A python script to change automatically desktop background 
You must have install feh in system ("sudo apt-get install feh")
this script is just for fun . If anyone have issue ping me

last work is to set is a cron job 

"""

import requests
import bs4
import subprocess
import os
import time
base_url = "http://apod.nasa.gov/apod/astropix.html"
res = requests.get(base_url,stream=True)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
img = soup.select('img')
#image_link = img.split('src')
img = " ".join(str(elm) for elm in img)

l = img.split("src=")
l=l[len(l)-1]

l = l.split("/>")
l = l[0]
l = l.split('"')
link = "http://apod.nasa.gov/"+l[1]
response = requests.get(link)

x = time.strftime("%d%m%Y")

name = "img"+x+".jpg"
os.system("touch "+name)
with open(name, 'wb') as f:
    f.write(response.content)


os.system("feh --bg-scale "+name)
