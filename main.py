import cv2
import mediapipe as mp
import pyautogui #move our curser
#open camera
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ =frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                #print(x, y)
                if id == 8:   # id for the index finger tip from the hand landmarks
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x      #to cover the hole screen in x direction
                    index_y = screen_height/frame_height*y             #to cover the y direction
                    pyautogui.moveTo(index_x, index_y)
                if id == 12:  # id for the thumb tip
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    middle_finger_x = screen_width / frame_width * x
                    middle_finger_y = screen_height / frame_height * y
                    print('outside' , abs(index_y - middle_finger_y))
                    if abs(index_y - middle_finger_y) < 30:
                        pyautogui.click()
                        pyautogui.sleep(1)
                        pyautogui.click(clicks=2)
                        pyautogui.click(clicks=2, interval=0.25)
                        pyautogui.click(button = 'right', clicks=3, interval=0.25)
                        print('Click')
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
