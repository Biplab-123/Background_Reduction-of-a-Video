##code inspired by SENTDEX

import numpy as np
import cv2

cap = cv2.VideoCapture('people-walking.mp4')#read the video
fgbg = cv2.createBackgroundSubtractorMOG2()#to subtract the background by mog algorithm

while(1):
    ret, frame = cap.read()#if while true then ret will work

    fgmask = fgbg.apply(frame)
 
    cv2.imshow('fgmask',frame)#to show the real video
    cv2.imshow('frame',fgmask)#to show the video after reduction of the background

    
    if cv2.waitKey(1) & 0xFF == ord('f'):  #wait for s key to press and break the infinite loop
        break
    

cap.release()
cv2.destroyAllWindows()
