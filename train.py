import mediapipe as mp
import cv2
import numpy as np
import os
import csv

gesture_name = input("Enter the guesture name:- ").strip()
os.makedirs('Dataset', exist_ok=True)
csv_path = os.path.join("Dataset",f"{gesture_name}.csv")

mp_hands = mp.solutions.hands 
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands= 1,min_detection_confidence= 0.7)

cap = cv2.VideoCapture(0)

with open(csv_path, "a", newline='') as f:
    writer = csv.writer(f)

    while True:
        sucess , frame = cap.read()
        if not sucess:
            break
        
        frame = cv2.flip(frame,1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks , mp_hands.HAND_CONNECTIONS)
                landmarks = []
                for lm in hand_landmarks.landmark:
                    landmarks.extend([lm.x,lm.y,lm.z])
                
                key = cv2.waitKey(1)
                if key == ord('s'):
                    writer.writerow(landmarks + [gesture_name])
                    print(f"[DATA] Saved sample for {gesture_name}")
    
        cv2.imshow("data collector",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
          break
        

cap.release()
cv2.destroyAllWindows()





