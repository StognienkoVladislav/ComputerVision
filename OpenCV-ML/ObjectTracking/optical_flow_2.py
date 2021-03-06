
import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()

prvs_img = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

hsv_mask = np.zeros_like(frame1)
hsv_mask[:, :, 1] = 255


while True:

    ret_2, frame_2 = cap.read()

    next_img = cv2.cvtColor(frame_2, cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(prvs_img, next_img, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    mag, ang = cv2.cartToPolar(flow[:, :, 0], flow[:, :, 1], angleInDegrees=True)

    hsv_mask[:, :, 0] = ang/2
    hsv_mask[:, :, 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)

    bgr = cv2.cvtColor(hsv_mask, cv2.COLOR_HSV2BGR)
    cv2.imshow('frame', bgr)

    k = cv2.waitKey(10) & 0xFF

    if k is 27:
        break

    prvs_img = next_img


cap.release()
cv2.destroyAllWindows()
