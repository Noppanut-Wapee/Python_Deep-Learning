import cv2 
import numpy as np  

img = cv2.imread('/Users/noppanutwapee/Desktop/Python_Deep-Learning/Project_pimc+/Pic Test/meter.jpg',cv2.IMREAD_COLOR)
#roi = img [213:434,255:505]
cv2.rectangle(img,(255,434),(505,213),(0,0,255),4)
#roi = img[213-213:434-213,255-255:505-255]
print(img.shape)
cv2.imshow('Test',img)
cv2.waitKey(0)

#โหลดรูปมา กำหนดค่า 1 เริ่มต้่น 0 grayscale -1 alpha
img1 = cv2.imread('/Users/noppanutwapee/Desktop/Python_Deep-Learning/Project_pimc+/Pic Test/meter.jpg',0)
cv2.imshow('TEXT',img1)
cv2.waitKey(0)

cv2.imwrite('pun.png',img1)


cv2.destroyAllWindows


