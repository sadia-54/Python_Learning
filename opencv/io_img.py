# pylint: disable=no-member
import os
import cv2

# read image
image_path = os.path.join('.', 'data', 'me.jpg')

img = cv2.imread(image_path)

# write image
cv2.imwrite(os.path.join('.', 'data', 'me_copy.jpg'), img)

# visualize image
resized_img = cv2.resize(img, (800, 600))  # resize image to 800x600
cv2.imshow('image', resized_img)
cv2.waitKey(0)   # wait for a key press to close the window