import numpy as np
import cv2
from imutils import contours
import imutils

img = cv2.imread('/Users/noppanutwapee/Desktop/Python_Deep-Learning/Project_pimc+/Pic Test/coler detect.jpg')
#resize

img = imutils.resize(img,500,500)


# HSV color model เป็นการพิจารณาสีโดยใช้ Hue, Saturation, Value
# Hue คือ ค่าสีของสีหลัก, Saturation คือ ความบริสุทธิ์ของสี , Value คือ ความสว่างของสี
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([20,180,180])
upper_blue = np.array([40,255,255])
# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
'''
for c in contours:
   rect = cv2.boundingRect(c)
   print(rect)
   x,y,w,h = rect
   area = w * h

   epsilon = 0.08 * cv2.arcLength(c, True)
   approx = cv2.approxPolyDP(c, epsilon, True)
 

   if area > 200000:
      cv2.drawContours(img, [approx], -1, (0, 0, 255), 5)
      cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)
      print('approx', approx)
      for x in range(0, len(approx)):
         cv2.circle(img, (approx[x][0][0], approx[x][0][1]), 30, (0,0,255), -1)
'''

# cv2.imwrite('/Users/noppanutwapee/Desktop/Python_Deep-Learning/Project_pimc+/Pic Test/output master.png',img)
cv2.imshow('coler',img)
cv2.waitKey(0)
cv2.drawContours(img, contours, -1, (0,255,0), 2)

#cv2.imshow('test',img2)
#cv2.waitKey(0)
cv2.imshow('coler',img)
cv2.waitKey(0)
cv2.imshow('coler',mask)
cv2.waitKey(0)

