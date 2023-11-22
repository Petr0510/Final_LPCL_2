import cv2
import mediapipe as mp
import numpy as np
from math import acos, degrees

def palm_centroid(coordinates_list):
     coordinates = np.array(coordinates_list)
     centroid = np.mean(coordinates, axis=0)
     centroid = int(centroid[0]), int(centroid[1])
     return centroid


mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

# Pulgar
thumb_points = [1, 2, 4]

# Índice, medio, anular y meñique
palm_points = [0, 1, 2, 5, 9, 13, 17]
fingertips_points = [8, 12, 16, 20]
finger_base_points =[6, 10, 14, 18]

# Colores
GREEN = (48, 255, 48)
BLUE = (192, 101, 21)
YELLOW = (0, 204, 255)
PURPLE = (128, 64, 128)
PEACH = (180, 229, 255)

with mp_hands.Hands(
     model_complexity=1,
     max_num_hands=1,
     min_detection_confidence=0.5,
     min_tracking_confidence=0.5) as hands:

     while True:
          ret, frame = cap.read()
          if ret == False:
               break
          frame = cv2.flip(frame, 1)
          height, width, _ = frame.shape
          frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
          results2 = hands.process(frame_rgb)
          fingers_counter = "_"
          thickness = [2, 2, 2, 2, 2]

          if results2.multi_hand_landmarks:
               coordinates_thumb = []
               coordinates_palm = []
               coordinates_ft = []
               coordinates_fb = []
               for hand_landmarks in results2.multi_hand_landmarks:
                    for index in thumb_points:
                         x = int(hand_landmarks.landmark[index].x * width)
                         y = int(hand_landmarks.landmark[index].y * height)
                         coordinates_thumb.append([x, y])
                    
                    for index in palm_points:
                         x = int(hand_landmarks.landmark[index].x * width)
                         y = int(hand_landmarks.landmark[index].y * height)
                         coordinates_palm.append([x, y])
                    
                    for index in fingertips_points:
                         x = int(hand_landmarks.landmark[index].x * width)
                         y = int(hand_landmarks.landmark[index].y * height)
                         coordinates_ft.append([x, y])
                    
                    for index in finger_base_points:
                         x = int(hand_landmarks.landmark[index].x * width)
                         y = int(hand_landmarks.landmark[index].y * height)
                         coordinates_fb.append([x, y])
                    ##########################
                    # Pulgar
                    p1 = np.array(coordinates_thumb[0])
                    p2 = np.array(coordinates_thumb[1])
                    p3 = np.array(coordinates_thumb[2])

                    l1 = np.linalg.norm(p2 - p3)
                    l2 = np.linalg.norm(p1 - p3)
                    l3 = np.linalg.norm(p1 - p2)

                    # Calcular el ángulo
                    angle = degrees(acos((l1**2 + l3**2 - l2**2) / (2 * l1 * l3)))
                    thumb_finger = np.array(False)
                    if angle > 150:
                         thumb_finger = np.array(True)
                    
                    ################################
                    # Índice, medio, anular y meñique
                    nx, ny = palm_centroid(coordinates_palm)
                   
                    coordinates_centroid = np.array([nx, ny])
                    coordinates_ft = np.array(coordinates_ft)
                    coordinates_fb = np.array(coordinates_fb)

                    # Distancias
                    d_centrid_ft = np.linalg.norm(coordinates_centroid - coordinates_ft, axis=1)
                    d_centrid_fb = np.linalg.norm(coordinates_centroid - coordinates_fb, axis=1)
                    dif = d_centrid_ft - d_centrid_fb
                    fingers = dif > 0
                    fingers = np.append(thumb_finger, fingers)
                    fingers_counter = str(np.count_nonzero(fingers==True))
                    for (i, finger) in enumerate(fingers):
                         if finger == True:
                              thickness[i] = -1

                   
          ################################
          print(fingers_counter)

          cv2.imshow("Frame", frame)
          if cv2.waitKey(1) & 0xFF == 27:
               break
cap.release()
cv2.destroyAllWindows()