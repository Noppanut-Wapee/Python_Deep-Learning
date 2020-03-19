import cv2 
import numpy as np  
from matplotlib import pyplot as plt  

img = cv2.imread('/Users/noppanutwapee/Desktop/Python_Deep-Learning/Project_pimc+/Pic Test/meter.jpg',cv2.IMREAD_COLOR)

plt.imshow(img, cmap='gray',interpolation='bicubic')
plt.xticks([1]),plt.yticks([1])
#plt.show()
#cv2.waitKey(0)

#cv2.imwrite('pun.png',img1)


#cv2.destroyAllWindows


