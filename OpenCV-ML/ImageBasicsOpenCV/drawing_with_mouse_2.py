
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Variables
# True while mouse button down
drawing = False
ix, iy = -1, -1


# Function for drawing
def draw_rectangle(event, x, y, flags, param):

    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)


cv2.namedWindow(winname='Drawing')
cv2.setMouseCallback('Drawing', draw_rectangle)


# Showing Image
img = np.zeros((512, 512, 3), np.int8)


while True:

    cv2.imshow('Drawing', img)

    # If we`ve waited at least 1 ms AND we`ve pressed the Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
