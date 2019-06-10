
import cv2
import time
import numpy as np

cap = cv2.VideoCapture('../data/hand_move.mp4')

if cap.isOpened() is False:
    print('Error file not found or wrong codec used!')


while cap.isOpened():

    ret, frame = cap.read()

    if ret is True:

        # Writer 20 FPS
        time.sleep(1/20)

        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    else:
        break


cap.release()
cv2.destroyAllWindows()
