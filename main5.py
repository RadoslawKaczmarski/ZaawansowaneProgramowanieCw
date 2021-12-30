import cv2

import numpy as np
from imutils.object_detection import  non_max_suppression

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def Detect (frame):
    rects, weights = HOGCV.detectMultiScale(frame,winStride=(4,4),padding=(8,8),scale=1.03)
    rects = np.array([[x,y,x+w,y+h] for (x,y,w,h) in rects])
    pick = non_max_suppression(rects,probs=None,overlapThresh=0.65)
    c=1
    for x,y,w,h in pick:
        cv2.rectangle(frame, (x,y), (w,h), (0,0,255),2)
        #cv2.rectangle(frame, (x,y - 20), (w,y), (0,0,255), -1)
        c +=1

    cv2.imshow("zdj", frame)
    return frame

