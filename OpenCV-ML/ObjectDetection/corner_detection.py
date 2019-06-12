
import cv2
import numpy as np
import matplotlib.pyplot as plt


flat_chess = cv2.imread('../data/flat_chessboard.png')
flat_chess = cv2.cvtColor(flat_chess, cv2.COLOR_BGR2RGB)
plt.imshow(flat_chess)
plt.show()


gray_flat = cv2.cvtColor(flat_chess, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_flat, cmap='gray')
plt.show()


real_chess = cv2.imread('../data/real_chessboard.jpg')
real_chess = cv2.cvtColor(real_chess, cv2.COLOR_BGR2RGB)
plt.imshow(real_chess)
plt.show()


gray_real_chess = cv2.cvtColor(real_chess, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_real_chess, cmap='gray')
plt.show()

# Corner Harris
gray = np.float32(gray_flat)
dst = cv2.cornerHarris(src=gray, blockSize=2, ksize=3, k=0.04)
dst = cv2.dilate(dst, None)
flat_chess[dst > 0.01*dst.max()] = [255, 0, 0]
plt.imshow(flat_chess)
plt.show()


gray_real = np.float32(gray_real_chess)
dst_real = cv2.cornerHarris(src=gray_real, blockSize=2, ksize=3, k=0.04)
dst_real = cv2.dilate(dst_real, None)
real_chess[dst_real > 0.01*dst_real.max()] = [255, 0, 0]
plt.imshow(real_chess)
plt.show()


# Shi-Tomasi
real_chess = cv2.imread('../data/real_chessboard.jpg')
real_chess = cv2.cvtColor(real_chess, cv2.COLOR_BGR2RGB)

flat_chess = cv2.imread('../data/flat_chessboard.png')
flat_chess = cv2.cvtColor(flat_chess, cv2.COLOR_BGR2RGB)

gray_flat = cv2.cvtColor(flat_chess, cv2.COLOR_BGR2GRAY)
gray_real_chess = cv2.cvtColor(real_chess, cv2.COLOR_BGR2GRAY)

# Flat
corners = cv2.goodFeaturesToTrack(gray_flat, 64, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(flat_chess, (x, y), 3, (255, 0, 0), -1)

plt.imshow(flat_chess)
plt.show()

# Real
corners = cv2.goodFeaturesToTrack(gray_real_chess, 120, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(real_chess, (x, y), 3, (255, 0, 0), -1)

plt.imshow(real_chess)
plt.show()
