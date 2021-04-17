# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 20:23:52 2021

@author: snakk
"""
import cv2
import numpy as np

image= cv2.VideoCapture(0)


def empty(x):
    pass

MyColors= np.array([96, 129, 88, 241, 129, 180])

for color in MyColors:
    cv2.namedWindow('TrackBars')
    cv2.resizeWindow("TrackBars", 640, 240)
    cv2.createTrackbar("Hue Min", "TrackBars", MyColors[0], 179, empty)
    cv2.createTrackbar("Hue Max", "TrackBars", MyColors[1], 179, empty)
    cv2.createTrackbar("Sat Min", "TrackBars", MyColors[2], 255, empty)
    cv2.createTrackbar("Sat Max", "TrackBars", MyColors[3], 255, empty)
    cv2.createTrackbar("Val Min", "TrackBars", MyColors[4], 255, empty)
    cv2.createTrackbar("Val Max", "TrackBars", MyColors[5], 255, empty)

    
    
def getContours(img):
    contours, hierarchy= cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #xset, yset, wset, hset=   [], [], [], []
    count=0
    x=y=w=h=0
    for i in contours:
        peri= cv2.arcLength(i, True)
        corner_points= cv2.approxPolyDP(i, 0.02*peri, True) #0.02*Peri is the resolution
        x,y,w,h= cv2.boundingRect(corner_points)  #this actually gives one corner point by (x,y) and the width and height (w,h)
        #cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        #xset.append(x), yset.append(y), wset.append(w), hset.append(h)                               
        count= count+1                                                                      
        
    return x+w/2,y 

        
newPoints=[]

while True:
    _,frame= image.read()
    frame=cv2.flip(frame, 1)
    imageHSV= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    Hue_Min= cv2.getTrackbarPos('Hue Min', "TrackBars")
    Hue_Max= cv2.getTrackbarPos('Hue Max', "TrackBars")
    Sat_Min= cv2.getTrackbarPos('Sat Min', "TrackBars")
    Sat_Max= cv2.getTrackbarPos('Sat Max', "TrackBars")
    Val_Min= cv2.getTrackbarPos('Val Min', "TrackBars")
    Val_Max= cv2.getTrackbarPos('Val Max', "TrackBars")
    #print(Hue_Min,Hue_Max, Sat_Min, Sat_Max, Val_Min, Val_Max)
    lower= np.array([Hue_Min, Sat_Min, Val_Min])
    upper= np.array([Hue_Max, Sat_Max, Val_Max])
    mask= cv2.inRange(imageHSV, lower, upper)
    result= cv2.bitwise_and(frame, frame, mask= mask)
    result_gray= cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    result_blur= cv2.GaussianBlur(result_gray, (5, 5), 1)
    result_canny= cv2.Canny(result_blur, 50, 50)
    getContours(result_canny)
    
    x,y= getContours(result_canny)
    
    cv2.circle(frame, (int(x),int(y)), 3, (255,0,0),-1)
    newPoints.append([x,y])

    for newPoint in newPoints:
        cv2.circle(frame, (int(newPoint[0]),int(newPoint[1])), 3, (255,0,0),-1)
                
    cv2.imshow("Final output",frame)
    cv2.imshow("edges",result_canny)
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break

cv2.destroyAllWindows()
image.release()