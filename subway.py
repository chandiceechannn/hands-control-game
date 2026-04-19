import cv2
import mediapipe as mp
import pyautogui
import time
import math

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

prev_action_time = 0


def calc_distance(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm = hand_landmarks.landmark

            
            thumb_tip = lm[4]
            index_tip = lm[8]
            middle_tip = lm[12]
            ring_tip = lm[16]
            pinky_tip = lm[20]

            # Jari tangan terbuka?
            fingers = []
            fingers.append(index_tip.y < lm[6].y)   # Telunjuk
            fingers.append(middle_tip.y < lm[10].y) # Tengah
            fingers.append(ring_tip.y < lm[14].y)   # Manis
            fingers.append(pinky_tip.y < lm[18].y)  # Kelingking
            
            current_time = time.time()
            if current_time - prev_action_time > 0.25:
                # Gesture ke kanan (✌🏻 = telunjuk + tengah)
                if fingers[0] and fingers[1] and not fingers[2] and not fingers[3]:
                    pyautogui.press('right')
                    print("Ke kanan")

                # Gesture ke kiri (👆🏼 = telunjuk saja)
                elif fingers[0] and not any(fingers[1:]):
                    pyautogui.press('left')
                    print("Ke kiri")

                # Gesture slide (✊🏻 = semua jari tertutup) 
                elif not any(fingers):
                    pyautogui.press('down')
                    print("Slide ke bawah")

                # Gesture lompat (✋🏻 = semua jari terbuka)
                elif all(fingers):
                    pyautogui.press('up')
                    print("Lompat")

                prev_action_time = current_time

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()