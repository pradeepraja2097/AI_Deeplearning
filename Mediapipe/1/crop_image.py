import cv2


img = cv2.imread("/home/pradeep/Documents/Deeplearning/Tyser/Task_1.jpg")


cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)

#crop coordinates Initialization
start_x, start_y, end_x, end_y = 0, 0, 0, 0


def mouse_event(event, x, y, flags, param):
    global start_x, start_y, end_x, end_y
    if event == cv2.EVENT_LBUTTONDOWN:
        start_x, start_y = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        end_x, end_y = x, y
        # Draw the rectangle for cropping
        cv2.rectangle(img, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
        cv2.imshow("Image", img)
cv2.setMouseCallback("Image", mouse_event)
cv2.waitKey(0)
cropped_img = img[start_y:end_y, start_x:end_x]
cv2.imwrite("/home/pradeep/Documents/Deeplearning/Tyser/1/Task_1_cropped.jpg", cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
