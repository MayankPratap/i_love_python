# This Python script captures video from webcam , flips the video and saves it in a file
# On Pressing key 'q' video recording stops and file is saved.
import numpy as np
import cv2

# Creating VideoCapture Object

cap=cv2.VideoCapture(0)  

# Define the codec and create VideoWriter Object

# I am using XVID Video Codec on my Ubuntu , for Windows use DVIX Codec

fourcc=cv2.VideoWriter_fourcc('X','V','I','D')

# Four things are passed to VideoWriter Object  :- output file name,video codec, frames per sec, frame width and height

out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

# isOpened makes sure that capture is going on

while(cap.isOpened()):

    ret,frame=cap.read()

    if ret==True:     
        frame=cv2.flip(frame,0)
     
        # Write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break


# Release everything if job is finished

cap.release()
out.release()
cv2.destroyAllWindows()
