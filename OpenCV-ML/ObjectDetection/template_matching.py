
import cv2
import numpy as np
import matplotlib.pyplot as plt


full_img = cv2.imread('../data/sammy.jpg')
full_img = cv2.cvtColor(full_img, cv2.COLOR_BGR2RGB)
plt.imshow(full_img)
plt.show()

face = cv2.imread('../data/sammy_face.jpg')
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
plt.imshow(face)
plt.show()


# All the 6 methods for comparison in a List

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED',
           'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']


for method in methods:
    full_copy = full_img.copy()

    new_method = eval(method)

    res = cv2.matchTemplate(full_copy, face, new_method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if new_method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc  # (x, y)
    else:
        top_left = max_loc

    height, width, channels = face.shape
    bottom_right = (top_left[0] + width, top_left[1] + height)

    cv2.rectangle(full_copy, top_left, bottom_right, (255, 0, 0), thickness=10)

    # Plot and show the images
    plt.subplot(121)
    plt.imshow(res)
    plt.title('HeatMap of template matching')

    plt.subplot(122)
    plt.imshow(full_copy)
    plt.title('Detection of template')

    # Title with the method used
    plt.suptitle(method)

    plt.show()
