import cv2
img = cv2.imread("/home/pradeep/Documents/Deeplearning/Tyser/3/Task_3.jpg", cv2.IMREAD_GRAYSCALE)

# Simple_thresholding
ret, simple_threshold = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
h_concat_simple=cv2.hconcat([img,simple_threshold])
cv2.imwrite("/home/pradeep/Documents/Deeplearning/Tyser/3/Simple_thresholding.jpg",h_concat_simple)

# Adaptive_thresholding
adaptive_threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
h_concat_adaptive=cv2.hconcat([img,adaptive_threshold])
cv2.imwrite("/home/pradeep/Documents/Deeplearning/Tyser/3/Adaptive_thresholding.jpg", h_concat_adaptive)
cv2.waitKey(0)
cv2.destroyAllWindows()