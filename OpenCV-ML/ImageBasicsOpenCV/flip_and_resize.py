
import numpy as np
import matplotlib.pyplot as plt
import cv2


# MATPLOTLIB --> RGB (Red Green Blue)
# OpenCV --> BGR (Blue Green Red)

img = cv2.imread('../data/00-puppy.jpg')

fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_gray = cv2.imread('../data/00-puppy.jpg', cv2.IMREAD_GRAYSCALE)

plt.imshow(img)
plt.show()

plt.imshow(fix_img)
plt.show()

plt.imshow(img_gray, cmap='gray')
plt.show()

# 0.5 == 50%
resize_img = cv2.resize(fix_img, (0, 0), fix_img, 0.5, 0.5)
plt.imshow(resize_img)
plt.show()


flip_img = cv2.flip(fix_img, 1)
plt.imshow(flip_img)
plt.show()


# Save Image
cv2.imwrite('name_of_image.jpg', fix_img)
