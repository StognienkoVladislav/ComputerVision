
import cv2
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm


def create_rgb(color):
    return tuple(np.array(cm.tab10(color)[:3])*255)


road = cv2.imread('../data/road_image.jpg')
road_copy = np.copy(road)

plt.imshow(road_copy)
plt.show()

segments = np.zeros(road.shape, dtype=np.uint8)
marker_image = np.zeros(road.shape[:2], dtype=np.int32)

colors = []
for i in range(10):
    colors.append(create_rgb(i))

##############################################################

# Global variables
n_markers = 10

# Color choice
current_marker = 1

# Markers updated by watershed
marks_updated = False


# Callback function
def mouse_callback(event, x, y, flags, param):
    global marks_updated
    if event is cv2.EVENT_LBUTTONDOWN:
        # Markers passed to the watershed algo
        cv2.circle(marker_image, (x, y), 10, (current_marker), -1)

        # User sees on the road image
        cv2.circle(road_copy, (x, y), 10, colors[current_marker], -1)

        marks_updated = True


# While true
cv2.namedWindow('Road Image')
cv2.setMouseCallback('Road Image', mouse_callback)

while True:

    cv2.imshow('Watershed Segments', segments)
    cv2.imshow('Road Image', road_copy)

    key = cv2.waitKey(1)
    # Close all windows
    if key == 27:
        break

    # Clearing all the olors press C key
    elif key == ord('c'):
        road_copy = road.copy()
        segments = np.zeros(road.shape, dtype=np.uint8)
        marker_image = np.zeros(road.shape[:2], dtype=np.int32)

    # Update color choice
    elif key > 0 and chr(key).isdigit():
        current_marker = int(chr(key))

    # Update the markings
    if marks_updated:
        marker_image_copy = marker_image.copy()
        cv2.watershed(road, marker_image_copy)

        segments = np.zeros(road.shape, dtype=np.uint8)

        for color_ind in range(n_markers):
            # Coloring segments, numpy call
            segments[marker_image_copy == (color_ind)] = colors[color_ind]

cv2.destroyAllWindows()
