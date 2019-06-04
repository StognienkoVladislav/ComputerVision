
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Function for drawing
def draw_circle(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 255, 0), -1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 0, 255), -1)


cv2.namedWindow(winname='Drawing')
cv2.setMouseCallback('Drawing', draw_circle)


# Showing Image
img = np.zeros((512, 512, 3), np.int8)


while True:

    cv2.imshow('Drawing', img)

    # If we`ve waited at least 1 ms AND we`ve pressed the Esc
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
