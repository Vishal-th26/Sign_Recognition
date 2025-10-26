import joblib
import numpy as np
import mediapipe as mp
import cv2

model = joblib.load("signLan_model.pkl")

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands= 1, min_detection_confidence = 0.7)

cap = cv2.VideoCapture(0)

def draw_text(img,text,pos=(50,50), color=(0,255,0)):
    cv2.putText(img,text,pos,cv2.FONT_HERSHEY_COMPLEX,1.2,color,3,cv2.LINE_AA)

while True:
    sucess, frame = cap.read()
    if not sucess:
        break
    frame = cv2.flip(frame,1)
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)
    
    gesture_text = ''
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract landmarks into flat array
            landmarks = np.array([[lm.x, lm.y, lm.z] for lm in hand_landmarks.landmark]).flatten()

            #prediction
            prediction = model.predict([landmarks])[0]
            gesture_text = prediction
    
    if gesture_text != "":
        draw_text(frame, f"Gesture: {gesture_text}", (30, 80), (0, 255, 0))
    else:
        draw_text(frame, "No Hand Detected", (30, 80), (0, 0, 255))

    cv2.imshow("Gesture Translator", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
