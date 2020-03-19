import cv2 
import numpy as np  

#สร้างกรอบรูป
img = np.zeros((512,512,3),np.uint8)

#ลองวาดรูปในกรอบที่สร้างไว้
cv2.rectangle(img,(100,100),(200,200),(255,0,0),2,)
cv2.circle(img,(200,150),50,(0,240,0),-1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Noppanut',(10,400),font,1,(100,100,100),2)

#แสดงรูปที่สร้าง 
cv2.imshow('img',img)
cv2.waitKey(0)

