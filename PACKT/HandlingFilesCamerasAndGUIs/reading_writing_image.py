
import numpy as np
import cv2

img = np.zeros((3, 3), dtype=np.uint8)

# convert into BGR
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
