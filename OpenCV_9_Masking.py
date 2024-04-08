import cv2 as cv
import numpy as np
img =  cv.imread('C:/Users/User 2/Desktop/cats.jpg')
cv.imshow('Meow', img)


blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', circle)

masked = cv.bitwise_and(img, img, mask=circle)
cv.imshow("Masked", masked)
cv.waitKey(0)