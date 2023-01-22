import cv2


img = cv2.imread("/home/pradeep/Documents/Deeplearning/Tyser/Task_1.jpg")

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)


start_x, start_y, end_x, end_y = 0, 0, 0, 0 #coordinates initialization

# Function to mousecalback
def mouse_event(event, x, y, flags, param):
    global start_x, start_y, end_x, end_y
    if event == cv2.EVENT_LBUTTONDOWN:
        start_x, start_y = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        end_x, end_y = x, y
        # Draw the rectangle for cropping
        cv2.rectangle(img, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
        # Display the top-left and bottom-right coordinates of the rectangle
        cv2.putText(img, f'Top Left: ({start_x}, {start_y})', (start_x, start_y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.putText(img, f'Bottom Right: ({end_x}, {end_y})', (end_x, end_y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.imshow("Image", img)
        cv2.imwrite("/home/pradeep/Documents/Deeplearning/Tyser/1/Task_1_insights.jpg",img)


cv2.setMouseCallback("Image", mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()