import cv2
import numpy as np
import time


cam = cv2.VideoCapture(-1)
time.sleep(1)

while True:
    ret,frame = cam.read()

    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()