#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import time
import numpy as np


# In[2]:


'''vidStream = cv2.VideoCapture(0)

frame = 0
while True:

    ret, frame = vidStream.read()
    cv2.imshow("Test Window", frame)
    #print(frame)
    #abc = np.flip(frame, axis=1)
    #print (abc)

    if cv2.waitKey(10)==ord('q'):
        break
        
frame = np.flip(frame, 1)'''


# In[5]:


cap = cv2.VideoCapture(0)

background = 0

for i in range(60):
    ret , frame = cap.read()
    
frame = np.flip(frame, 1)


# In[ ]:


while(cap.isOpened()):
    ret, img = cap.read()
    
    if not ret:
        break
    
    img = np.flip(img,axis=1)
    
    #cv2.imshow("Original",img)
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    
    #cv2.imshow("HSV", hsv)
    
    '''blurImg1 = cv2.blur(img,(5,5))
    cv2.imshow("blur1", blurImg1)

    avging = cv2.blur(img,(10,10))
    cv2.imshow('Average', avging)

    Gaus = cv2.GaussianBlur(img,(5,5),0)
    cv2.imshow("Gaus", Gaus)

    Med = cv2.medianBlur(img,5)
    cv2.imshow("Median", Med)

    BiFi = cv2.bilateralFilter(img,9,75,75)
    cv2.imshow("Bilateral", BiFi)'''
    
    
    red1 = np.array([0,120,70],np.uint8)
    red2 = np.array([10,255,255],np.uint8)
    mask1 = cv2.inRange(hsv,red1,red2)
    #cv2.imshow("mask1",mask1)
    

    red1 = np.array([170,120,70],np.uint8)
    red2 = np.array([180,255,255],np.uint8)
    mask2 = cv2.inRange(hsv,red1,red2)
    #cv2.imshow("mask2",mask2)
    
    
    mask = mask1+mask2
    kernel = np.ones((15,15),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    #cv2.imshow("mask",mask)
    #cv2.imshow("Background",frame)
    
    
    img[np.where(mask==255)] = frame[np.where(mask==255)]
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Display',img)
    k = cv2.waitKey(10)
    if k == 27:
        break
        
cap.release()
cv2.destroyAllWindows()


# In[ ]:




