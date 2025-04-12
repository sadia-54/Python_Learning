# pylint: disable=no-member

import os
import cv2

img_path = os.path.join('.', 'data', 'image.png')

img = cv2.imread(img_path)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # there are more and more other color spaces

cv2.imshow('image', img)
cv2.imshow('image rgb', img_rgb)
cv2.waitKey(0) 

