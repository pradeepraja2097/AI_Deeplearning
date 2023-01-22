import cv2
import numpy as np


img = cv2.imread("/home/pradeep/Documents/Deeplearning/Tyser/2/Letter.png", cv2.IMREAD_GRAYSCALE)

#  kernel size
kernel = np.ones((5, 5), np.uint8)

#  dilation
dilation = cv2.dilate(img, kernel, iterations=5)
h_concat=cv2.hconcat([img,dilation])
cv2.imwrite("/home/pradeep/Documents/Deeplearning/Tyser/2/Dilation.jpg",h_concat)

#  erosion
erosion = cv2.erode(img, kernel, iterations=1)
h_concat_erosion=cv2.hconcat([img,erosion])
cv2.imwrite("/home/pradeep/Documents/Deeplearning/Tyser/2/Erosion.jpg",h_concat_erosion)

#  opening
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
h_concat_opening=cv2.hconcat([img,opening])
cv2.imwrite("/home/pradeep/Documents/Deeplearning/Tyser/2/Opening.jpg",h_concat_opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
