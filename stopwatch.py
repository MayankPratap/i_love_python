# Display the the program's instructions.

print "Press Enter to begin.Afterwards,press ENTER to Click the stopwatch.Press Ctrl-C to quit"
raw_input()
print "Started"
startTime=time.time()   # Get the first lap's start time
lastTime=startTime
lapNum=1

# Start tracking the lap times.

try:
    while True:
       raw_input()
       lapTime=round(time.time()-lastTime,2)
       totalTime=round(time.time()-startTime,2)
       print 'Lap #%s: %s (%s)' % (lapNum,totalTime,lapTime)
       lapNum+=1           # Increase lap counter
       lastTime=time.time()   # reset the last lap time

except KeyboardInterrupt:
    print '\nDone'
