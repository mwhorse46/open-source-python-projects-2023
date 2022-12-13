import cv2 as cv
import random
img = cv.imread('opencv/assets/soccer_practice.jpg')
# tag = img[500:700, 600:900]
# img[100:300, 650:950] = tag
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
