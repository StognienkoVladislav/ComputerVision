
import cv2
import numpy as np
import matplotlib.pyplot as plt


blank_img = np.zeros(shape=(512, 512, 3), dtype=np.int16)
plt.imshow(blank_img)
plt.show()

cv2.rectangle(blank_img, pt1=(384, 10), pt2=(500, 150), color=(0, 255, 0),
              thickness=10)

cv2.circle(blank_img, (100, 100), 50, (255, 0, 0), 8)

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(blank_img, text='Hi', org=(10, 500), fontFace=font, fontScale=4, color=(255, 255, 255),
            thickness=3, lineType=cv2.LINE_AA)
plt.imshow(blank_img)
plt.show()
