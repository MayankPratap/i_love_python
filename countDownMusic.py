#!python3
# countdown.py - A simple countdown script.

import time,subprocess

timeLeft=10

print("Hello")

while timeLeft>0:
   # print("Hello")
    print(timeLeft,end=' ')
    time.sleep(1)
    timeLeft=timeLeft-1


# At the end of the countdown,play a sound file

# 'see' in linux acts as double clicking a file
# In windows use 'start'
# In OSX use 'open'

subprocess.Popen(['see','jiya.mp3'])
