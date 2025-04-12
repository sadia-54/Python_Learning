# pylint: disable=no-member

import os
import cv2

img_path = os.path.join('.', 'data', 'image.png')

img = cv2.imread(img_path)

k_size = 10  # kernel size for blurring, the neighbourhood size of the pixel to be blurred
img_blur = cv2.blur(img, (k_size, k_size))  
# mediun blur is better for removing noise

cv2.imshow('image', img)
cv2.imshow('img_blurred', img_blur)
cv2.waitKey(0)
