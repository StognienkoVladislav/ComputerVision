
import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('../data/rainbow.jpg', 0)
plt.imshow(img, cmap='gray')
plt.show()


ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

plt.imshow(thresh1, cmap='gray')
plt.show()


img2 = cv2.imread('../data/crossword.jpg', 0)
plt.imshow(img2, cmap='gray')
plt.show()


ret2, th1 = cv2.threshold(img2, 180, 255, cv2.THRESH_BINARY)

plt.imshow(th1, cmap='gray')
plt.show()


th2 = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
plt.imshow(th2, cmap='gray')
plt.show()


blended = cv2.addWeighted(src1=th1, alpha=0.6, src2=th2, beta=0.4, gamma=0)
plt.imshow(blended, cmap='gray')
plt.show()
