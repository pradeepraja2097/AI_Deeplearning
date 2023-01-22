import mediapipe as mp
import cv2
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


def euclidean_dist(point1, point2):
    return np.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


cap = cv2.VideoCapture(0)
finger_coordinates=[(8,6),(12,10),(16,14),(20,18)]
thumb_coordinate=(4,2)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: 
    while cap.isOpened():
        ret, frame = cap.read()
        
        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Flip on horizontal
        image = cv2.flip(image, 1)
        
        # Set flag
        image.flags.writeable = False
        
        # Detections
        results = hands.process(image)
        
        # Set flag to true
        image.flags.writeable = True
        
        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        font = cv2.FONT_HERSHEY_COMPLEX 
        
        # Rendering results
        if results.multi_hand_landmarks:

            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )
                
                # landmarks = []
                hand_points = []
                for idx,lm in enumerate(hand.landmark):
                    h,w,c=image.shape
                    cx,cy= int(lm.x*w)  ,int(lm.y*h)
                    hand_points.append([cx,cy])

                hand_points = np.array(hand_points)
                # print(hand_points)

                # check the distance for index finger
                dist = euclidean_dist(hand_points[8], hand_points[5])
                if dist > 120 :
                    print("Index finger is opened")
                    cv2.putText(image,'I',(0,100),font,2,(255,255,255),3)
                
                # check the distance for middle finger
                dist = euclidean_dist(hand_points[12], hand_points[9])
                if dist > 120 :
                    print("Middle finger is opened")
                    cv2.putText(image,'M',(0,100),font,2,(255,255,255),3)

                # check the distance for ring finger
                dist = euclidean_dist(hand_points[16], hand_points[13])
                if dist > 120 :
                    print("Ring finger is opened")
                    cv2.putText(image,'R',(0,100),font,2,(255,255,255),3)

                # check the distance for pinky finger
                dist = euclidean_dist(hand_points[20], hand_points[17])
                if dist > 120 :
                    print("Pinky finger is opened")
                    cv2.putText(image,'B',(0,100),font,2,(255,255,255),3)

                # check the distance for thumb finger
                dist = euclidean_dist(hand_points[4], hand_points[2])
                if dist > 71 :
                    print("Thumb finger is opened")
                    cv2.putText(image,'T',(0,100),font,2,(255,255,255),3)
                


        
        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()