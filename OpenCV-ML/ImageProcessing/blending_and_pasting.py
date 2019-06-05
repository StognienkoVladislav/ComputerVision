
import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.cvtColor(cv2.imread('../data/dog_backpack.png'), cv2.COLOR_BGR2RGB)

img2 = cv2.cvtColor(cv2.imread('../data/watermark_no_copy.png'), cv2.COLOR_BGR2RGB)

plt.imshow(img1)
plt.show()

plt.imshow(img2)
plt.show()


# BLENDING IMAGES OF THE SAME SIZE

img1_1 = cv2.resize(img1, (1200, 1200))
img2_1 = cv2.resize(img2, (1200, 1200))

blended = cv2.addWeighted(img1_1, 0.8, img2_1, 0.1, 0)
plt.imshow(blended)
plt.show()


# OVERLAY SMALL IMAGE ON TOP OF A LARGER IMAGE (NO BLENDING)
# Numpy reassignment

large_img = img1
small_img = cv2.resize(img2, (600, 600))

x_offset = 0
y_offset = 0

x_end = x_offset + small_img.shape[1]
y_end = y_offset + small_img.shape[0]

large_img[y_offset:y_end, x_offset:x_end] = small_img
plt.imshow(large_img)
plt.show()

# BLEND TOGETHER IMAGES OF DIFFERENT SIZES

img1 = cv2.cvtColor(cv2.imread('../data/dog_backpack.png'), cv2.COLOR_BGR2RGB)

img2 = cv2.cvtColor(cv2.imread('../data/watermark_no_copy.png'), cv2.COLOR_BGR2RGB)

img2 = cv2.resize(img2, (600, 600))

# img1_x - img2_x
# img1_y - img2_y
x_offset = 934 - 600
y_offset = 1401 - 600

row, col, channels = img2.shape

roi = img1[y_offset:1401, x_offset:943]

img2gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
plt.imshow(img2gray, cmap='gray')

mask_inv = cv2.bitwise_not(img2gray)
plt.imshow(mask_inv, cmap='gray')
plt.show()


white_background = np.full(img2.shape, 255, dtype=np.uint8)

bk = cv2.bitwise_or(white_background, white_background, mask=mask_inv)

fg = cv2.bitwise_or(img2, img2, mask=mask_inv)

final_roi = cv2.bitwise_or(roi, fg)
plt.imshow(final_roi)
plt.show()


# Add mask on Large image
large_img = img1
small_img = final_roi

large_img[y_offset:y_offset + small_img.shape[0], x_offset:x_offset + small_img.shape[1]] = small_img
plt.imshow(large_img)
plt.show()
